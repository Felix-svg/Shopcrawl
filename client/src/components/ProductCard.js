// client/src/components/ProductCard.js

import React from 'react';

function ProductCard({ product }) {
  const cardStyle = {
    border: '1px solid #ddd',
    borderRadius: '5px',
    padding: '10px',
    margin: '10px',
    textAlign: 'center',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    transition: 'transform 0.2s',
    width: '200px' // Reduce the width of the card
  };

  const imageStyle = {
    width: '100%',
    height: '150px', // Adjust height to fit smaller card
    objectFit: 'cover',
    borderBottom: '1px solid #ddd',
    marginBottom: '10px'
  };

  const nameStyle = {
    fontSize: '1em',
    marginBottom: '5px'
  };

  const priceStyle = {
    color: '#007BFF',
    fontSize: '0.9em',
    marginBottom: '5px'
  };

  const ratingStyle = {
    color: '#FFD700'
  };

  return (
    <div style={cardStyle}>
      <img src={product.image_src} alt={product.product_name} style={imageStyle} />
      <h3 style={nameStyle}>{product.name}</h3>
      <p style={priceStyle}>Price: {product.price}</p>
      <p style={ratingStyle}>Rating: {product.rating}</p>
    </div>
  );
}

export default ProductCard;
