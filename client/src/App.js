import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate
} from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import About from "./components/About";
import Footer from "./components/Footer";
import ResultsPage from "./components/ResultsPage";
import Login from "./components/Login";
import Signup from "./components/Signup";
import RankProduct from "./components/RankProduct";
import LandingPage from "./components/LandingPage";
import Products from "./components/Products";
import NotFound from "./components/NotFound";
import ForgotPassword from "./components/ForgotPassword";
import PasswordResetForm from "./components/PasswordResetForm";

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
      <div>
        <Navbar loggedIn={loggedIn} onLogout={handleLogout} />
        <Routes>
          {/* Route for non-logged-in users */}
          {!loggedIn && (
            <Route path="/" element={<LandingPage />} />
          )}
          {/* Route for logged-in users */}
          {loggedIn && (
            <Route path="/" element={<Navigate to="/search" />} />
          )}
          <Route path="/login" element={<Login onLogin={handleLogin} />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/search" element={<Home />} />
          <Route path="/results" element={<ResultsPage />} />
          <Route path="/rank-products" element={<RankProduct />} />
          <Route path="/products" element={<Products />} />
          <Route path="/about" element={<About />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />
          <Route path="/reset-password" element={<PasswordResetForm />}/>
          {/* Not Found route */}
          <Route path="*" element={<NotFound loggedIn={loggedIn} />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
