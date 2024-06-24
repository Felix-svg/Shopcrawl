import React from 'react';
import './RankCard.css';

const truncateText = (text, maxLength) => {
  if (text.length <= maxLength) {
    return text;
  }
  return text.slice(0, maxLength) + '...';
};

const RankProductCard = ({ rank, product, benefitType }) => {
  const truncatedSource = truncateText(product.source, 30);

  return (
    <div className='col mb-3 mt-3'>
      <div className="card border" style={{ borderRadius: '15px'}}>
        <div className="card-body">
          <h5 className="card-title"><strong>Rank {rank}</strong></h5>
          <p><strong>Product Name:</strong> {product.product_name}</p>
          <p className="card-text"><strong>Price:</strong> ${product.product_price}</p>
          <p className="card-text"><strong>Rating:</strong> {product.product_rating}</p>
          <p className="card-text">
            <strong>Source:</strong>
            <a href={product.source} target="_blank" rel="noopener noreferrer">
              {truncatedSource}
            </a>
          </p>
          {benefitType === 'Marginal Benefit' && (
            <p className="card-text"><strong>Marginal Benefit:</strong> {product.marginal_benefit}</p>
          )}
          {benefitType === 'Cost Benefit' && (
            <p className="card-text"><strong>Cost Benefit:</strong> {product.cost_benefit}</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default RankProductCard;
