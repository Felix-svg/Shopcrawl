import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faInstagram, faFacebook, faTwitter } from '@fortawesome/free-brands-svg-icons';

function Footer() {
    return (
        <footer style={{ backgroundColor: 'black', color: 'white', textAlign: 'center', padding: '10px', width: '100%' }}>
            <p> Shoping Premium. </p>
            <p>Tel: +254798560345 +254734567982</p>
            <div>
                <a href="https://www.instagram.com/k.e.m.u.n.t.o/" target="_blank" rel="noopener noreferrer" style={{ color: 'white', margin: '0 10px' }}>
                    <FontAwesomeIcon icon={faInstagram} size="lg" />
                </a>
                <a href="https://www.facebook.com/kemunto/" target="_blank" rel="noopener noreferrer" style={{ color: 'white', margin: '0 10px' }}>
                    <FontAwesomeIcon icon={faFacebook} size="lg" />
                </a>
                <a href="https://www.twitter.com" target="_blank" rel="noopener noreferrer" style={{ color: 'white', margin: '0 10px' }}>
                    <FontAwesomeIcon icon={faTwitter} size="lg" />
                </a>
                <p>© 2024 </p>
            </div>
        </footer>
    );
}

export default Footer;
