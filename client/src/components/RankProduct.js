import React, { useState } from 'react';
import axios from 'axios';
import RankProductCard from './RankCard';
import InformationPanel from './InfoPanel';

const RankProduct = () => {
  const [productName, setProductName] = useState('');
  const [priceImportance, setPriceImportance] = useState('');
  const [ratingImportance, setRatingImportance] = useState('');
  const [productsMb, setProductsMb] = useState([]);
  const [productsCb, setProductsCb] = useState([]);
  const [calculating, setCalculating] = useState(false);
  const [error, setError] = useState('');
  const [rankingType, setRankingType] = useState('mb');
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 10;

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

  const fetchRankedProducts = async (requestData) => {
    setCalculating(true);
    console.log('Request Data:', requestData); // Debugging: log request data
    try {
      const response = await axios.post('https://shopcrawl-server.onrender.com/rank_products', requestData);
      console.log('Response Data:', response.data); // Debugging: log response data
      if (response.status === 200) {
        const { ranked_products_mb, ranked_products_cb } = response.data;
        setProductsMb(ranked_products_mb);
        setProductsCb(ranked_products_cb);
        setError('');
      } else {
        setError('Failed to fetch ranked products.');
      }
      setCalculating(false);
    } catch (error) {
      console.error('Error fetching ranked products:', error); // Debugging: log error details
      setError('Failed to fetch ranked products. Please try again later.');
      setCalculating(false);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const requestData = {
      product_name: productName,
      product_price: parseFloat(priceImportance),
      product_rating: parseFloat(ratingImportance),
    };
    fetchRankedProducts(requestData);
  };

  const handlePageChange = (newPage) => {
    setCurrentPage(newPage);
  };

  const renderProducts = (products) => {
    const startIndex = (currentPage - 1) * itemsPerPage;
    const selectedProducts = products.slice(startIndex, startIndex + itemsPerPage);
    return (
      <div className="row mt-4" style={{ marginLeft: '50px', marginRight: '50px' }}>  
        {selectedProducts.map((product, index) => (
          <div key={index} className="col-lg-6 col-md-4 mb-4">
            <RankProductCard
              rank={startIndex + index + 1}
              product={product}
              benefitType={rankingType === 'mb' ? 'Marginal Benefit' : 'Cost Benefit'}
            />
          </div>
        ))}
      </div>
    );
    
  };

  const renderPagination = (totalItems) => {
    const totalPages = Math.ceil(totalItems / itemsPerPage);
    return (
      <div className="d-flex justify-content-center mt-4">
        <nav>
          <ul className="pagination">
            <li className={`page-item ${currentPage === 1 ? 'disabled' : ''}`}>
              <button className="page-link" onClick={() => handlePageChange(currentPage - 1)}>
                Prev
              </button>
            </li>
            {[...Array(totalPages)].map((_, index) => (
              <li
                key={index}
                className={`page-item ${currentPage === index + 1 ? 'active' : ''}`}
                onClick={() => handlePageChange(index + 1)}
              >
                <button className="page-link">
                  {index + 1}
                </button>
              </li>
            ))}
            <li className={`page-item ${currentPage === totalPages ? 'disabled' : ''}`}>
              <button className="page-link" onClick={() => handlePageChange(currentPage + 1)}>
                Next
              </button>
            </li>
          </ul>
        </nav>
      </div>
    );
  };

  return (
    <section style={{ backgroundColor: "#90AEAD", padding: "4px" }}>
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
                <div className="mb-3 mt-4">
                  <label htmlFor="rankingType" className="form-label">
                    Select Ranking Type:
                  </label>
                  <select
                    className="form-select"
                    id="rankingType"
                    name="rankingType"
                    value={rankingType}
                    onChange={(e) => setRankingType(e.target.value)}
                  >
                    <option value="mb">Marginal Benefit</option>
                    <option value="cb">Cost Benefit</option>
                  </select>
               </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <h2 className='text-center mt-5'>Ranked Products</h2>

      {calculating && <p className="text-center mt-4">Calculating...</p>}
      {error && <p className="text-center mt-4 text-danger">{error}</p>}

      {rankingType === 'mb' && productsMb.length > 0 && (
        <>
          {renderProducts(productsMb)}
          {renderPagination(productsMb.length)}
        </>
      )}

      {rankingType === 'cb' && productsCb.length > 0 && (
        <>
          {renderProducts(productsCb)}
          {renderPagination(productsCb.length)}
        </>
      )}

      {!calculating && productsMb.length === 0 && productsCb.length === 0 && (
        <p className="text-center mt-4">No ranked products to display.</p>
      )}
    </section>
  );
};

export default RankProduct;
