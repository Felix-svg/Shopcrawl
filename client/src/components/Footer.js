import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faInstagram, faFacebook, faTwitter } from '@fortawesome/free-brands-svg-icons';

function Footer() {
    // Style object for the footer
    const footerStyle = {
        backgroundColor: 'black',
        color: 'white',
        textAlign: 'left',  // Changed from 'center' to 'left'
        padding: '10px',
        width: '100%'
    };

    // Style object for social media icons
    const iconStyle = {
        color: 'white',
        margin: '0 10px'
    };

    return (
        <footer style={footerStyle}>
            <p>Shopping Premium.</p>
            <p>Tel: +254798560345, +254734567982</p>
            <div>
                <a href="https://www.instagram.com/k.e.m.u.n.t.o/" target="_blank" rel="noopener noreferrer" style={iconStyle}>
                    <FontAwesomeIcon icon={faInstagram} size="lg" />
                </a>
                <a href="https://www.facebook.com/kemunto/" target="_blank" rel="noopener noreferrer" style={iconStyle}>
                    <FontAwesomeIcon icon={faFacebook} size="lg" />
                </a>
                <a href="https://www.twitter.com" target="_blank" rel="noopener noreferrer" style={iconStyle}>
                    <FontAwesomeIcon icon={faTwitter} size="lg" />
                </a>
                <p>© 2024</p>
            </div>
        </footer>
    );
}

export default Footer;
