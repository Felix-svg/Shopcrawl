import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Footer from './components/Footer';

function App() {
  return (
    <Router>
        <div>
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