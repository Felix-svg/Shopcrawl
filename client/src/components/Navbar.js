import React, { useState } from 'react';

const NavBar = () => {
    const [searchTerm, setSearchTerm] = useState('');

    const handleSearchChange = (event) => {
        setSearchTerm(event.target.value);
    };

    const handleSearchSubmit = () => {
        alert('Search for: ' + searchTerm); 
    };

    return (
        <div style={{ backgroundColor: '#90AEAD', minHeight: '15vh' }}>
            <nav style={{ color: 'black', padding: '10px 20px' }}>
                <ul style={{
                    listStyle: 'none',
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center'
                }}>
                    <li style={{ marginRight: '50px' }}>Home</li>
                    <li style={{ marginRight: '50px' }}>Products</li>
                    <li style={{ marginRight: '50px' }}>About</li>
                    <li style={{ marginRight: '50px' }}>Contact</li>
                    <li style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center' }}>
                        <input
                            type="text"
                            placeholder="Search..."
                            style={{ padding: '5px', borderRadius: '10px', border: '1px solid black', marginRight: '10px' }}
                            value={searchTerm}
                            onChange={handleSearchChange}
                        />
                        <button
                            style={{
                                padding: '5px 10px',
                                backgroundColor: 'black',
                                color: '#90AEAD',
                                border: '1px solid black',
                                borderRadius: '5px',
                                cursor: 'pointer'
                            }}
                            onClick={handleSearchSubmit}
                        >
                            Search
                        </button>
                    </li>
                </ul>
            </nav>
        </div>
    );
};

export default NavBar;
