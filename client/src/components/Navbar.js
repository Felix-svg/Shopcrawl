import React from 'react';

function Navbar() {
    return (
        <nav style={{ backgroundColor: '#F5F5F5', padding: '20px 20px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)', fontFamily: 'Arial, sans-serif' }}>
            <ul style={{ listStyle: 'none', display: 'flex', justifyContent: 'center', alignItems: 'center', margin: 0 }}>
                <li style={{ marginRight: '30px', padding: '10px 20px', fontSize: '16px', fontWeight: 'bold', transition: 'background-color 0.3s ease', borderRadius: '5px' }}>
                    <a href="#" style={{ color: '#333', textDecoration: 'none', display: 'block', padding: '2px 5px' }}
                       onMouseEnter={(e) => e.target.style.backgroundColor = '#E0E0E0'}
                       onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}>Home</a>
                </li>
                <li style={{ marginRight: '30px', padding: '10px 20px', fontSize: '16px', fontWeight: 'bold', transition: 'background-color 0.3s ease', borderRadius: '5px' }}>
                    <a href="#" style={{ color: '#333', textDecoration: 'none', display: 'block', padding: '2px 5px' }}
                       onMouseEnter={(e) => e.target.style.backgroundColor = '#E0E0E0'}
                       onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}>Products</a>
                </li>
                <li style={{ marginRight: '30px', padding: '10px 20px', fontSize: '16px', fontWeight: 'bold', transition: 'background-color 0.3s ease, color 0.3s ease', borderRadius: '5px' }}>
                    <a href="#" style={{ color: '#333', textDecoration: 'none', display: 'block', padding: '2px 5px' }}
                       onMouseEnter={(e) => e.target.style.backgroundColor = '#E0E0E0'}
                       onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}>About</a>
                </li>
                <li style={{ marginRight: '30px', padding: '10px 20px', fontSize: '16px', fontWeight: 'bold', transition: 'background-color 0.3s ease, color 0.3s ease', borderRadius: '5px' }}>
                    <a href="#" style={{ color: '#333', textDecoration: 'none', display: 'block', padding: '2px 5px' }}
                       onMouseEnter={(e) => e.target.style.backgroundColor = '#E0E0E0'}
                       onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}>Contact</a>
                </li>
                {/* Search Bar */}
                <li style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center', borderRadius: '20px', backgroundColor: 'white', padding: '0 10px', boxShadow: '0 2px 2px rgba(0,0,0,0.1)' }}>
                    <input type="text" placeholder="Search..." style={{ padding: '10px', border: 'none', outline: 'none', fontSize: '16px', width: '200px', height: '38px' }} />
                    <button style={{ padding: '10px 15px', backgroundColor: '#E0E0E0', color: 'black', border: 'none', borderRadius: '10px', cursor: 'pointer', transition: 'background-color 0.3s ease', height: '38px' }}>
                        Search
                    </button>
                </li>
            </ul>
        </nav>
    );
}

export default Navbar;
