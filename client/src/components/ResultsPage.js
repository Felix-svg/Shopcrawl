import React from 'react';
import { useLocation, Link } from 'react-router-dom';

function ResultsPage() {
    const location = useLocation();
    const { alibaba, amazon } = location.state || { alibaba: [], amazon: [] };

    return (
        <div style={{ padding: '20px', maxWidth: '1200px', margin: 'auto' }}>
            <Link to="/" style={{ display: 'block', marginBottom: '20px', textDecoration: 'none', color: 'blue', fontSize: '18px', fontWeight: 'bold' }}>Go Back</Link>
            <div>
                <h2 style={{ color: '#333' }}>Alibaba Results</h2>
                <ResultsSection results={alibaba} style={{
                    backgroundColor: '#f0f0f0', // Light grey background for Alibaba results
                }} />
                <h2 style={{ color: '#002244' }}>Amazon Results</h2>
                <ResultsSection results={amazon} style={{
                    backgroundColor: '#d1e0e0', // Light blue background for Amazon results
                }} />
            </div>
        </div>
    );
}

const ResultsSection = ({ results, style }) => (
    <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center', ...style }}>
        {results.length > 0 ? results.map((result, index) => (
            <ResultCard key={index} result={result} />
        )) : <p>No results found.</p>}
    </div>
);

const ResultCard = ({ result }) => (
    <div style={{
        minWidth: '220px',
        maxWidth: '220px',
        height: '360px',  // Increased height to accommodate more content
        margin: '10px',
        padding: '15px',
        border: '1px solid #ccc',
        borderRadius: '10px',
        boxShadow: '0 2px 5px rgba(0,0,0,0.1)',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        backgroundColor: '#fff'
    }}>
        <img src={result.image_src} alt={result.product_name} style={{ height: '100px', width: '100%', objectFit: 'cover', marginBottom: '10px' }} />
        <div>
            <p style={{ margin: 0, fontWeight: 'bold', fontSize: '14px', textAlign: 'center' }}>{result.product_name}</p>
            <p style={{ margin: 0, fontSize: '12px', textAlign: 'center', fontWeight:'600' }}>Price: {result.product_price}</p>
            <p style={{ margin: 0, fontSize: '12px', textAlign: 'center', fontWeight:'600' }}>Rating: {result.product_rating}</p>
        </div>
    </div>
);

export default ResultsPage;
