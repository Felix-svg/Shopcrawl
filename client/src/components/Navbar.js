import React from 'react';
import { Link } from 'react-router-dom';
import logo from './images/logo-png.jpg'; // Ensure the path is correct
import 'bootstrap/dist/css/bootstrap.min.css';

function Navbar({ loggedIn }) {
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
        <nav className="navbar navbar-expand-lg navbar-light bg-white shadow-sm">
            <div className="container">
                <Link className="navbar-brand" to="/" style={{ marginRight: 'auto', marginLeft: 'auto' }}>
                    <img src={logo} alt="Logo" style={{ height: '60px' }} />
                </Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse justify-content-center" id="navbarNav">
                    <ul className="navbar-nav">
                        {[
                            { text: 'Home', path: '/' },
                            { text: 'Rank Products', path: '/rank-products' },
                            { text: 'Products', path: '/products' },
                            { text: 'About', path: '/about' },
                            { text: 'Contact', path: '/contact' }
                        ].map(({ text, path }) => (
                            <li key={text} className="nav-item mx-3">
                                <Link 
                                    className="nav-link" 
                                    to={path} 
                                    style={{ color: '#90AEAD', fontWeight: 'bold' }}
                                    onMouseEnter={handleMouseEnter}
                                    onMouseLeave={handleMouseLeave}
                                >
                                    {text}
                                </Link>
                            </li>
                        ))}
                    </ul>
                </div>
                {!loggedIn ? (
                    <div className="ms-auto">
                        <Link to="/login">
                            <button 
                                className="btn" 
                                style={{ 
                                    backgroundColor: '#90AEAD', 
                                    color: 'black', 
                                    padding: '0.375rem 1.5rem', // Increased padding for a wider button
                                }}
                                onMouseEnter={handleButtonMouseEnter}
                                onMouseLeave={handleButtonMouseLeave}
                            >
                                Login
                            </button>
                        </Link>
                    </div>
                ) : null}
            </div>
        </nav>
    );
}

export default Navbar;
