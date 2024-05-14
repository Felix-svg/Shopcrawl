import React, { useState } from 'react';
import axios from 'axios';

const SearchBar = () => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.get(`https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&tab=all&SearchText={sunglasses}`);
            setResults(response.data.data); // Assuming response contains formatted data
        } catch (error) {
            console.error('Error fetching data:', error);
            setError('Error fetching data. Please try again later.');
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Search for products..."
                />
                <button type="submit">Search</button>
            </form>
            {error && <p>{error}</p>}
            <ul>
                {results.map((result) => (
                    <li key={result.id}>
                        <a href={result.link}>{result.name}</a>
                        <p>{result.price}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default SearchBar;
