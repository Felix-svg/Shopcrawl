import React from 'react';
import { useNavigate } from 'react-router-dom';
import SearchBar from './SearchBar';
import "bootstrap/dist/css/bootstrap.min.css";

function Home({ onLogout }) {
  const navigate = useNavigate();
  
  const handleLogout = () => {
    localStorage.removeItem("access_token");
    onLogout();
    navigate("/");
  };

  return (
    <div className="d-flex flex-column align-items-center justify-content-center vh-100 " style={{backgroundColor:"#90AEAD"}}>
      <div className="mb-3 w-100" style={{ maxWidth: '600px' }}>
        <SearchBar />
      </div>
      <button 
        onClick={handleLogout} 
        className="btn btn-dark mt-3"
        style={{ width: '100%', maxWidth: '200px' }}
      >
        Logout
      </button>
    </div>
  );
}

export default Home;