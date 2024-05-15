import React from 'react';
import SearchBar from './SearchBar'; 

function Home() {
    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', backgroundColor: '#f0f0f0' }}>
            <SearchBar />
        </div>
    );
}

export default Home;
