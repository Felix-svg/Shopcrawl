// ProductCard.js

import React from "react";

function ProductCard({ product }) {
  return (
    <div>
      <img src={product.image_src} alt={product.product_name} />
      <h3>{product.product_name}</h3>
      <p>Price: {product.product_price}</p>
      <p>Rating: {product.product_rating}</p>
    </div>
  );
}

export default ProductCard;
