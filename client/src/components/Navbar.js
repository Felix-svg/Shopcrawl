import React from 'react';
import logo from '../components/images/logo-png.jpg';  // Ensure the path is correct

function Navbar() {
    const handleMouseEnter = (e) => {
        e.target.style.backgroundColor = '#E0E0E0';
        e.target.style.color = 'black';
    };

    const handleMouseLeave = (e) => {
        e.target.style.backgroundColor = 'transparent';
        e.target.style.color = '#333';
    };

    const handleButtonMouseEnter = (e) => {
        e.target.style.backgroundColor = 'black';
        e.target.style.color = '#90AEAD';
    };

    const handleButtonMouseLeave = (e) => {
        e.target.style.backgroundColor = '#90AEAD';
        e.target.style.color = 'black';
    };

    return (
        <nav style={{ backgroundColor: 'white', padding: '20px 20px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)', fontFamily: 'Arial, sans-serif', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div style={{ display: 'flex', alignItems: 'center' }}>
                <img src={logo} alt="Logo" style={{ height: '60px', marginRight: '20px' }} />
            </div>
            <ul style={{ listStyle: 'none', display: 'flex', justifyContent: 'center', alignItems: 'center', margin: 0, flex: 1 }}>
                {['Home', 'Products', 'About', 'Contact'].map((text) => (
                    <li key={text} style={{ margin: '0 30px', padding: '10px 20px', fontSize: '16px', fontWeight: 'bold', transition: 'background-color 0.3s ease, color 0.3s ease', borderRadius: '5px', textAlign: 'center' }}>
                        <a 
                            href="#" 
                            style={{ color: '#90AEAD', textDecoration: 'none', display: 'block', padding: '2px 5px' }}
                            onMouseEnter={handleMouseEnter}
                            onMouseLeave={handleMouseLeave}
                        >
                            {text}
                        </a>
                    </li>
                ))}
            </ul>
            <div style={{ display: 'flex', alignItems: 'center' }}>
                <button style={{ padding: '10px 20px', fontSize: '16px', fontWeight: 'bold', backgroundColor: '#90AEAD', color: 'black', border: 'none', borderRadius: '5px', cursor: 'pointer', transition: 'background-color 0.3s ease, color 0.3s ease' }}
                    onMouseEnter={handleButtonMouseEnter}
                    onMouseLeave={handleButtonMouseLeave}>
                    Login
                </button>
            </div>
        </nav>
    );
}

export default Navbar;
