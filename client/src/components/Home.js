import React from 'react';
import SearchBar from './SearchBar'; 

function Home() {
    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', backgroundColor: '#90AEAD' }}>
            <SearchBar />
        </div>
    );
}

export default Home;
