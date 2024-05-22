import React from 'react';
import { useLocation, Link } from 'react-router-dom';
import './ResultsPage.css';

function ResultsPage() {
    const location = useLocation();
    const { alibaba = [], amazon = [], jumia = [] } = location.state || {};

    return (
        <div className="results-container">
            <Link to="/search" className="back-link">Go Back</Link>
            <div>
                <h2 className="results-heading" style={{ color: '#002244' }}>Alibaba Results</h2>
                <ResultsSection results={alibaba} style={{
                    backgroundColor: '#d1e0e0',
                }} />
                <h2 className="results-heading" style={{ color: '#002244' }}>Amazon Results</h2>
                <ResultsSection results={amazon} style={{
                    backgroundColor: '#d1e0e0',
                }} />
                <h2 className="results-heading" style={{ color: '#002244' }}>Jumia Results</h2>
                <ResultsSection results={jumia} style={{
                    backgroundColor: '#d1e0e0',
                }} />
            </div>
        </div>
    );
}

const ResultsSection = ({ results = [], style }) => (
    <div className="results-section" style={style}>
        {results.length > 0 ? results.map((result, index) => (
            <ResultCard key={index} result={result} />
        )) : <p>No results found.</p>}
    </div>
);

const ResultCard = ({ result }) => (
    <div className="result-card">
        <img src={result.image_src} alt={result.product_name} className="result-image" />
        <div className="result-details">
            <p className="result-name">{result.product_name}</p>
           <strong><p className="result-price">Price: {result.product_price}</p></strong> 
            <p className="result-rating">
                {result.product_rating === null ? "No rating found" : `Rating: ${result.product_rating}`}
            </p>
            <a href={result.source} target="_blank" rel="noopener noreferrer">
                Buy here
            </a>
        </div>
    </div>
);

export default ResultsPage;
