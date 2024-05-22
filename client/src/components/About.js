import React from 'react';
import './About.css';

const About = () => (
  <div className="container p-4 text">
    <div className="row">
      <div className="col">
        <h1>About Shopcrawl</h1>
        <section className="company-overview">
          <p>
            Shopcrawl is revolutionizing the online shopping experience by providing a sophisticated tool for automatically computing the marginal benefit (MB) and cost benefit (CB) analysis of products across different e-shops. By considering factors such as shipping costs, consumer ratings, quality, and price, Shopcrawl helps consumers make informed purchasing decisions.
          </p>
        </section>
      </div>
    </div>
    <div className="row">
      <div className="col">
        <section className="how-it-works">
          <h2>How It Works</h2>
          <p>
            Using advanced algorithms and real-time data extraction from various e-commerce platforms, Shopcrawl indexes product information and applies MB and CB formulas to rank products effectively. Our service ensures that you get the best value for your money by comparing offerings from multiple stores.
          </p>
        </section>
      </div>
    </div>
    <div className="row">
      <div className="col">
        <section className="technology">
          <h2>Our Technology</h2>
          <p>
            Our platform leverages a robust tech stack including React for the frontend, Python Flask for the backend, and PostgreSQL for data management. We prioritize mobile-friendly designs and employ rigorous testing frameworks to ensure a seamless user experience.
          </p>
        </section>
      </div>
    </div>
  </div>
);

export default About;
