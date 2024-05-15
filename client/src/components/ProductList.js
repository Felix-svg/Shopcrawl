// ProductList.js

import React from 'react';
import ProductCard from './ProductCard';

function ProductList({ products }) {
  return (
    <div>
      {products.map((product, index) => (
        <ProductCard key={index} product={product} />
      ))}
    </div>
  );
}

export default ProductList;
