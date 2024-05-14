// App.js

import React, { useState } from 'react';
import ProductList from './components/ProductList';
import SearchBar from './components/SearchBar';
import CategoryComponent from './components/CategoryComponent'; // Import CategoryComponent

function App() {
  const [products, setProducts] = useState([]);

  const searchProducts = async (query) => {
    try {
      const response = await fetch(`http://localhost:5000/search?q=${query}`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setProducts(data); // Update products state with search results
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <SearchBar onSearch={searchProducts} />
      <CategoryComponent /> {/* Render CategoryComponent */}
      <ProductList products={products} />
    </div>
  );
}

export default App;
