import React, { useState } from 'react';
import axios from 'axios';
import 'ionicons'

const SearchBar = () => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState({ alibaba: [], amazon: [] });
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null); // Reset error state before making a new request
        try {
            const response = await axios.get(`http://127.0.0.1:5000/search?q=${query}`);
            setResults(response.data); // Update results with the new data structure
        } catch (error) {
            console.error('Error fetching data:', error);
            setError('Error fetching data. Please try again later.');
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <form onSubmit={handleSubmit} style={{ marginBottom: '20px' }}>
                <div className="search-box">
                    <div className="search-input">
                        <input
                            type="search"
                            value={query}
                            onChange={(e) => setQuery(e.target.value)}
                            placeholder="Search our products, deals and more."
                            style={{ padding: '10px', width: '300px' }}
                        />
                    </div>
                    <span className="search-btn">
                        <button type="submit" style={{ padding: '10px 20px', marginLeft: '10px' }}>
                            <ion-icon name="search-sharp"></ion-icon>
                            Search
                        </button>
                    </span>
                </div>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
                <div>
                    <h2>Alibaba Results</h2>
                    {results.alibaba.length > 0 ? (
                        <ul style={{ listStyleType: 'none', padding: 0 }}>
                            {results.alibaba.map((result, index) => (
                                <li key={index} style={{ marginBottom: '10px' }}>
                                    <img src={`https:${result.image_src}`} alt={result.product_name} style={{ width: '50px', marginRight: '10px' }} />
                                    <a href="#" target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none', color: 'blue' }}>
                                        {result.product_name}
                                    </a>
                                    <p>{result.product_price}</p>
                                    <p>{result.product_rating}</p>
                                </li>
                            ))}
                        </ul>
                    ) : (
                        <p>No results found for Alibaba.</p>
                    )}
                </div>
                <div>
                    <h2>Amazon Results</h2>
                    {results.amazon.length > 0 ? (
                        <ul style={{ listStyleType: 'none', padding: 0 }}>
                            {results.amazon.map((result, index) => (
                                <li key={index} style={{ marginBottom: '10px' }}>
                                    <img src={result.image_src} alt={result.product_name} style={{ width: '50px', marginRight: '10px' }} />
                                    <a href="#" target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none', color: 'blue' }}>
                                        {result.product_name}
                                    </a>
                                    <p>{result.product_price}</p>
                                    <p>{result.product_rating}</p>
                                </li>
                            ))}
                        </ul>
                    ) : (
                        <p>No results found for Amazon.</p>
                    )}
                </div>
            </div>
        </div>
    );
};

export default SearchBar;