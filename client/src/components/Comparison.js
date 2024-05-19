import React from 'react';
import './Comparison.css';

function Comparison({ comparisonData }) {
  return (
    <div className="comparison-container">
      <h2>Comparison</h2>
      <div className="table-responsive">
        <table className="table">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Image</th>
              <th>Source</th>
              <th>Rating</th>
              {/* Add more columns for other attributes */}
            </tr>
          </thead>
          <tbody>
            {comparisonData && comparisonData.map((product, index) => (
              <tr key={index}>
                <td>{product.name}</td>
                <td>{product.price}</td>
                <td><img src={product.image} alt={product.name} className="product-image" /></td>
                <td>{product.source}</td>
                <td>{product.rating}</td>
                {/* Add more cells for other attributes */}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Comparison;