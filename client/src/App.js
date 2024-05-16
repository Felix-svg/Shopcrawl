// client/src/App.js

import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Footer from './components/Footer';
import ResultsPage from './components/ResultsPage'; // Make sure the path is correct
import Login from './components/Login';
import Signup from './components/Signup';
import ProductList from './components/ProductList';

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
    <Router>
      <Navbar /> {/* Navbar on every page */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/results" element={<ResultsPage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/products" element={<ProductList />} /> {/* Correctly nested ProductList component */}
      </Routes>
      <Footer /> {/* Footer on every page */}
    </Router>
  );
}

export default App;
