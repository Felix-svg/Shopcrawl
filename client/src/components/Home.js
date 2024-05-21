import React from 'react';
import SearchBar from './SearchBar';
import "bootstrap/dist/css/bootstrap.min.css";
  
  const handleLogout = (navigate, onLogout) => {
    localStorage.removeItem("access_token");
    onLogout();
    navigate("/");
  };
  
  function Home() {
    return (
      <div className="d-flex flex-column align-items-center justify-content-center vh-100" style={{backgroundColor:"#90AEAD"}}>
        <div className="mb-3 w-100" style={{ maxWidth: '600px' }}>
          <SearchBar />
        </div>
      </div>
    );
  }
  
  export { handleLogout };
  export default Home;