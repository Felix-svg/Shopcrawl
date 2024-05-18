// Comparison.js

import React from 'react';

function Comparison({ comparisonData }) {
  return (
    <div>
      <h2>Comparison</h2>
      <table>
        <thead>
          <tr>
            <th>Product</th>
            <th>Price</th>
            {/* Add more columns for other attributes */}
          </tr>
        </thead>
        <tbody>
          {comparisonData && comparisonData.map((product, index) => (
            <tr key={index}>
              <td>{product.name}</td>
              <td>{product.price}</td>
              <td>{product.image}</td>
              <td>{product.source}</td>
              <td>{product.rating}</td>


              {/* Add more cells for other attributes */}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Comparison;
