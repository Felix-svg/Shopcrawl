import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import ProductCard from './components/ProcuctCard';

function App() {
  return (
    <Router>
        <div>
            <Routes>
              <Route path="/" element={
                <>
                  <Navbar/>
                  <ProductCard/>
                  <Footer />
                </>
              } />
            </Routes>
        </div>
    </Router>
  );
}

export default App;