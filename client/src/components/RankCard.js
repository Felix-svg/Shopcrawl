import React from 'react';
import './RankCard.css';

const truncateText = (text, maxLength) => {
  if (text.length <= maxLength) {
    return text;
  }
  return text.slice(0, maxLength) + '...';
};


  

const RankProductCard = ({ rank, product, benefitType }) => {
  const truncatedSource = truncateText(product.source, 30); // Truncate to 30 characters

  return (
    <div className="card" id='rankcard'>
      <div className="card-body" id='r-cardbody'>
          <h5 className="card-title" id='title'>Rank {rank}</h5>
          <p><strong>Product Name:</strong> {product.product_name}</p>
      
          <p className="card-text" id='text'><strong>Price:</strong> ${product.product_price}</p>
          <p className="card-text" id='text'><strong>Rating:</strong> {product.product_rating}</p>
          <p className="card-text" id='text'>
            <strong>Source:</strong>
            <a href={product.source} target="_blank" rel="noopener noreferrer">
              {truncatedSource}
            </a>
          </p>
          {benefitType === 'Marginal Benefit' && (
            <p className="card-text" id='text'><strong>Marginal Benefit:</strong> {product.marginal_benefit}</p>
          )}
          {benefitType === 'Cost Benefit' && (
            <p className="card-text" id='text'><strong>Cost Benefit:</strong> {product.cost_benefit}</p>
          )}
        
      </div>
    </div>
  );
};

export default RankProductCard;
