import React, { useState } from 'react';
import axios from 'axios';
import RankProductCard from './RankedDisplay';
import InformationPanel from './InfoPanel';

const RankProduct = () => {
  const [productName, setProductName] = useState('');
  const [priceImportance, setPriceImportance] = useState('');
  const [ratingImportance, setRatingImportance] = useState('');
  const [rankedProducts, setRankedProducts] = useState([]);
  const [calculating, setCalculating] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const [productsPerPage] = useState(10);

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
    setCurrentPage(1);

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

  const indexOfLastProduct = currentPage * productsPerPage;
  const indexOfFirstProduct = indexOfLastProduct - productsPerPage + 1;
  const currentProducts = rankedProducts.slice(indexOfFirstProduct - 1, indexOfLastProduct);

  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber)
  }

  const renderPaginationItems = () => {
    const totalProducts = rankedProducts.length;
    const pageNumbers = Math.ceil(totalProducts / productsPerPage);

    const paginationItems = [];

    let startPage = currentPage - 5;
    let endPage = currentPage + 4;

    if (startPage < 1) {
      startPage = 1
      endPage = Math.min(10, pageNumbers)
    }

    if (endPage > pageNumbers) {
      startPage = Math.max(1, pageNumbers - 9)
      endPage = pageNumbers
    }

    // Previous page button
    paginationItems.push(
      <li className={`page-item ${currentPage === 1 ? 'disabled' : ''}`} key="previous">
        <button
          className="page-link text-white bg-dark"
          onClick={() => handlePageChange(currentPage - 1)}
        >
          Previous
        </button>
      </li>
    );

    // Page numbers
    for (let i = startPage; i <= endPage; i++) {
      paginationItems.push(
        <li
          key={i}
          className={`page-item ${currentPage === i ? 'active' : ''}`}
          onClick={() => handlePageChange(i)}
        >
          <button
            className={`page-link ${currentPage === i ? 'bg-black text-white' : 'text-dark'}`}
          >
            {i}
          </button>
        </li>
      );
    }

    // Next page button
    paginationItems.push(
      <li className={`page-item ${currentPage === pageNumbers ? 'disabled' : ''}`} key="next">
        <button
          className="page-link text-white bg-dark"
          onClick={() => handlePageChange(currentPage + 1)}
        >
          Next
        </button>
      </li>
    );

    return paginationItems;
  };

  return (
    <section style={{ backgroundColor : "#90AEAD" }}>
      <div className="container">
        <h2 className="text-center my-4">Rank Products</h2>
        <div className="row">
          <div className="col-md-4">
            <InformationPanel />
          </div>
          <div className="col-md-8">
            <div className="row justify-content-center">
              <div className="col-md-8">
                <form onSubmit={handleSubmit}>
                  <div className="mb-3">
                    <label htmlFor="productName" className="form-label">
                      Product Name:
                    </label>
                    <input
                      type="text"
                      className="form-control"
                      id="productName"
                      name="productName"
                      value={productName}
                      onChange={handleInputChange}
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="priceImportance" className="form-label">
                      Price Importance (0-1):
                    </label>
                    <input
                      type="number"
                      className="form-control"
                      id="priceImportance"
                      name="priceImportance"
                      step="0.1"
                      min="0"
                      max="1"
                      value={priceImportance}
                      onChange={handleInputChange}
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="ratingImportance" className="form-label">
                      Rating Importance (0-1):
                    </label>
                    <input
                      type="number"
                      className="form-control"
                      id="ratingImportance"
                      name="ratingImportance"
                      step="0.1"
                      min="0"
                      max="1"
                      value={ratingImportance}
                      onChange={handleInputChange}
                    />
                  </div>
                  <button type="submit" className="btn btn-dark">
                    Rank Products
                  </button>
                </form>
              </div>
            </div>
          </div>
        </div>
    
        <h2 className="text-center mt-4">Ranked Products:</h2>
    
        {calculating ? (
          <p className="text-center">Calculating...</p>
        ) : rankedProducts.length > 0 ? (
          <>
            <div className="row row-cols-1 row-cols-md-2">
              {currentProducts.map((product, index) => (
                <RankProductCard key={index} product={product} index={index} indexOfFirstProduct={indexOfFirstProduct} />
              ))}
            </div>
            <ul className="pagination justify-content-center">
              {renderPaginationItems()}
            </ul>
          </>
        ) : (
          <p className="text-center">No ranked products to display.</p>
        )}
      </div>
    </section>
  );
}

export default RankProduct;