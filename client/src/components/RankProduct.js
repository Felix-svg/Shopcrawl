import React, { useState } from 'react';
import axios from 'axios';

const RankProduct = () => {
  const [productName, setProductName] = useState('');
  const [priceImportance, setPriceImportance] = useState('');
  const [ratingImportance, setRatingImportance] = useState('');
  const [rankedProducts, setRankedProducts] = useState([]);
  const [calculating, setCalculating] = useState(false);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    if (name === 'productName') {
      setProductName(value);
    } else if (name === 'priceImportance') {
      setPriceImportance(value);
    } else if (name === 'ratingImportance') {
      setRatingImportance(value);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    const requestData = {
      product_name: productName,
      product_price: parseFloat(priceImportance),
      product_rating: parseFloat(ratingImportance),
    };

    setCalculating(true);

    axios
      .post('http://127.0.0.1:5000/rank_products', requestData)
      .then((response) => {
        setRankedProducts(response.data);
        setCalculating(false);
      })
      .catch((error) => {
        console.error('Error:', error);
        setCalculating(false);
      });
  };

  return (
    <div>
      <h1>Rank Products</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Product Name:
          <input
            type="text"
            name="productName"
            value={productName}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <label>
          Price Importance (0-1):
          <input
            type="number"
            name="priceImportance"
            step="0.1"
            min="0"
            max="1"
            value={priceImportance}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <label>
          Rating Importance (0-1):
          <input
            type="number"
            name="ratingImportance"
            step="0.1"
            min="0"
            max="1"
            value={ratingImportance}
            onChange={handleInputChange}
          />
        </label>
        <br />
        <button type="submit">Rank Products</button>
      </form>

      <h2>Ranked Products:</h2>

      {calculating ? (
        <p>Calculating...</p>
      ) : rankedProducts.length > 0 ? (
        <ul>
          {rankedProducts.map((product, index) => (
            <li key={index}>
              <strong>Rank {index + 1}:</strong>
              <br />
              Product 1 Amazon: {product.product1.product_name}, Price: {product.product1.product_price}, Rating: {product.product1.product_rating}
              <br />
              Product 2 Alibaba: {product.product2.product_name}, Price: {product.product2.product_price}, Rating: {product.product2.product_rating}
              <br />
              Marginal Benefit: {product.marginal_benefit}
              <br />
              Cost Benefit: {product.cost_benefit}
              <br />
              <br />
            </li>
          ))}
        </ul>
      ) : (
        <p>No ranked products to display.</p>
      )}
    </div>
  );
};

export default RankProduct;
