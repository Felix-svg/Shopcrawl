import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Footer from './components/Footer';
import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
        <div>
            <Routes>
              <Route path="/" element={
                <>
                  <Navbar/>
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