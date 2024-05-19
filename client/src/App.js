import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Navigate, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Footer from "./components/Footer";
import ResultsPage from "./components/ResultsPage"; // Make sure the path is correct
import Login from "./components/Login";
import Signup from "./components/Signup";
import RankProduct from "./components/RankProduct";
import LandingPage from "./components/LandingPage";
import Products from "./components/Products";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (token) {
      setLoggedIn(true);
    }
  }, []);

  const handleLogin = (token) => {
    localStorage.setItem("access_token", token);
    setLoggedIn(true);
  };

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    setLoggedIn(false);
  };

  return (
    <Router>
    <div  className="">
      <Navbar loggedIn={loggedIn} />
      <Routes>
         
            <Route path="/" element={<LandingPage />} />
            <Route path="/login" element={<Login onLogin={handleLogin} />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="*" element={<Navigate to="/" />} />
            <Route path="/products" element={<Products />} />
            <Route
              path="/search"
              element={<Home onLogout={handleLogout} />}
            />
            <Route path="/results" element={<ResultsPage />} />
            <Route path="/rank-products" element={<RankProduct />} />
            <Route path="*" element={<Navigate to="/search" />} />
      </Routes>
      <Footer />
    </div>
  </Router>
  );
}

export default App;
