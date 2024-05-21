import React from 'react';
import { useLocation, Link } from 'react-router-dom';
import './ResultsPage.css';

function ResultsPage() {
    const location = useLocation();
    const { alibaba = [], amazon = [], jumia = [] } = location.state || {};

    return (
        <div className="results-container">
            <Link to="/" className="back-link">Go Back</Link>
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
    <div className="card ms-2 me-2 mt-2 mb-2 p-3" style={{ width: '16rem' }}>
        <img src={result.image_src} alt={result.product_name} className="card-img-top" />
        <div className="card-body d-flex flex-column justify-content-between">
            <div>
                <h5 className="card-title mb-2">{result.product_name}</h5>
                <p className="card-text mb-2">Price: {result.product_price}</p>
                <p className="card-text mb-2">
                    {result.product_rating === null ? "No rating found" : `Rating: ${result.product_rating}`}
                </p>
                <p className="card-text mb-2">
                    {result.product_description || "No description available"}
                </p>
            </div>
            <a href={result.source} target="_blank" rel="noopener noreferrer" className="btn btn-link mt-3">
                Buy here
            </a>
        </div>
    </div>
);

export default ResultsPage;
