import React from 'react';
import SearchBar from './SearchBar'; 
import watches from "../components/images/men accesories 2.jpg";  // Ensure the path is correct

function Home() {
    return (
        <div style={{ backgroundImage: `url(${watches})`, backgroundSize: 'cover', backgroundRepeat: 'no-repeat', height: '100vh' }}>
            <SearchBar />
        </div>
    );
}

export default Home;
