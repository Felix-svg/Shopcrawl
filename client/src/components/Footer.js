import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFacebookF, faTwitter, faGooglePlusG, faInstagram } from '@fortawesome/free-brands-svg-icons';
import { faPhone } from '@fortawesome/free-solid-svg-icons';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer bg-light pt-4">
      <div className="container">
        <div className="row">
          <div className="col-md-4 col-sm-6 mb-4">
            <div className="single_footer single_footer_address">
              <h4>Page Links</h4>
              <ul className="list-unstyled">
                <li><a href="/home">Home</a></li>
                <li><a href="/products">Products</a></li>
                <li><a href="/about">About Us</a></li>
              </ul>
            </div>
          </div>
          <div className="col-md-4 col-sm-6 mb-4">
            <div className="single_footer single_footer_address">
              <h4>Follow Us</h4>
              <div className="social_profile">
                <ul className="list-inline">
                  <li className="list-inline-item">
                    <a href="https://www.facebook.com/" className="facebook">
                      <FontAwesomeIcon icon={faFacebookF} />
                    </a>
                  </li>
                  <li className="list-inline-item">
                    <a href="https://x.com/" className="twitter">
                      <FontAwesomeIcon icon={faTwitter} />
                    </a>
                  </li>
                  <li className="list-inline-item">
                    <a href="https://www.google.com/" className="google">
                      <FontAwesomeIcon icon={faGooglePlusG} />
                    </a>
                  </li>
                  <li className="list-inline-item">
                    <a href="https://www.instagram.com/" className="instagram">
                      <FontAwesomeIcon icon={faInstagram} />
                    </a>
                  </li>
                </ul>
                <p>
                  <a href="tel:+123456789">
                    <FontAwesomeIcon icon={faPhone} /> +123456789
                  </a>
                </p>
              </div>
            </div>
          </div>
          <div className="col-md-4 col-sm-12 mb-4">
            <div className="single_footer single_footer_about">
              <h4>About Us</h4>
              <p>
                We are committed to providing the best services and products to our customers. Our mission is to deliver high-quality solutions that meet the needs of our diverse client base. Join us on our journey to excellence and discover the difference we can make together.
              </p>
            </div>
          </div>
        </div>
        <div className="row">
          <div className="col-12 text-center">
            <p className="copyright">
              Copyright © 2024 <a href="#">Shopcrawl</a>.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
