import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';  // Ensure the path is correct
import Home from './components/Home';
import Footer from './components/Footer';

function App() {
  return (
    <Router>
        <div>
            <Navbar />  {/* Add Navbar here */}
            <Routes>
              <Route path="/" element={
                <>
                  <Home />
                  <Footer />
                </>
              } />
            </Routes>
        </div>
    </Router>
  );
}

export default App;
