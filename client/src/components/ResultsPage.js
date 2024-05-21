import React from 'react';
import { useLocation, Link } from 'react-router-dom';
import './ResultsPage.css';

function ResultsPage() {
    const location = useLocation();
    const { alibaba, amazon } = location.state || { alibaba: [], amazon: [] };

    return (
        <div className="results-container">
            <Link to="/" className="back-link">Go Back</Link>
            <div>
                <h2 className="results-heading" style={{ color: '#333' }}>Alibaba Results</h2>
                <ResultsSection results={alibaba} style={{
                    backgroundColor: '#f0f0f0', // Light grey background for Alibaba results
                }} />
                <h2 className="results-heading" style={{ color: '#002244' }}>Amazon Results</h2>
                <ResultsSection results={amazon} style={{
                    backgroundColor: '#d1e0e0', // Light blue background for Amazon results
                }} />
            </div>
        </div>
    );
}

const ResultsSection = ({ results, style }) => (
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
            <p className="result-price">Price: {result.product_price}</p>
            <p className="result-rating">Rating: {result.product_rating}</p>
        </div>
    </div>
);

export default ResultsPage;