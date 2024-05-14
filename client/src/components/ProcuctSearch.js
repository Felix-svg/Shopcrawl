import React, { useState } from 'react';
import ProductCard from './ProductCard';

function ProductSearch() {
  const [searchTerm, setSearchTerm] = useState('');
  const [products, setProducts] = useState([]);

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearch = () => {
    // Fetch products based on searchTerm. Here's a mocked fetch function:
    const fetchedProducts = mockFetchProducts(searchTerm);
    setProducts(fetchedProducts);
  };

  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={handleSearchChange}
        placeholder="Search products..."
      />
      <button onClick={handleSearch}>Search</button>
      <div>
        {products.map(product => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}

// Mock function to simulate fetching products
function mockFetchProducts(search) {
  // This would be replaced with an actual API call
  const allProducts = [
    { id: 1, name: 'Apple', image: 'path/to/apple.jpg', description: 'Fresh apples', price: 1.99 },
    { id: 2, name: 'Banana', image: 'path/to/banana.jpg', description: 'Organic bananas', price: 0.99 },
    { id: 3, name: 'Carrot', image: 'path/to/carrot.jpg', description: 'Crunchy carrots', price: 0.50 }
  ];

  return allProducts.filter(product => product.name.toLowerCase().includes(search.toLowerCase()));
}

export default ProductSearch;
