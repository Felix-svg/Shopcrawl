import React from 'react';
import { useNavigate } from 'react-router-dom';
import SearchBar from './SearchBar'; 

function Home({onLogout}) {
    const navigate = useNavigate()
    const handleLogout = () => {
        localStorage.removeItem("access_token");
        onLogout();
        navigate("/")
      };
    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', backgroundColor: '#90AEAD' }}>
            <SearchBar />
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default Home;
