// client/src/components/ProductList.js

import React, { useEffect, useState } from 'react';
import ProductCard from './ProductCard';
import axios from 'axios';

function ProductList() {
  const [products, setProducts] = useState({ amazon: [], alibaba: [] });

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/products')
      .then(response => {
        const allProducts = response.data.products;
        console.log('Fetched products:', allProducts); // Debugging line
        const amazonProducts = allProducts.filter(product => product.source === 'amazon');
        const alibabaProducts = allProducts.filter(product => product.source === 'alibaba');
        setProducts({ amazon: amazonProducts, alibaba: alibabaProducts });
      })
      .catch(error => {
        console.error('There was an error fetching the products!', error);
      });
  }, []);

  const listStyle = {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: '10px' // Add gap between cards
  };

  const sectionStyle = {
    width: '100%',
    padding: '10px',
    borderTop: '1px solid #ddd',
    marginTop: '10px'
  };

  const sectionTitleStyle = {
    fontSize: '1.2em',
    marginBottom: '10px',
    textAlign: 'center'
  };

  return (
    <div>
      <div style={sectionStyle}>
        <h2 style={sectionTitleStyle}>Amazon Products</h2>
        <div style={listStyle}>
          {products.amazon.map((product, index) => (
            <ProductCard key={index} product={product} />
          ))}
        </div>
      </div>
      <div style={sectionStyle}>
        <h2 style={sectionTitleStyle}>Alibaba Products</h2>
        <div style={listStyle}>
          {products.alibaba.map((product, index) => (
            <ProductCard key={index} product={product} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default ProductList;
