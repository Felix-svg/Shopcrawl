import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const SearchBar = () => {
    const [query, setQuery] = useState('');
    const navigate = useNavigate();
    const [error, setError] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [barHeight, setBarHeight] = useState([1, 1.5, 2, 1.5, 1]); // Initial heights for each bar

    useEffect(() => {
        let animationFrame;
        if (isLoading) {
            const animateBars = () => {
                setBarHeight(prevHeights => prevHeights.map(h => h === 2 ? 1 : h + 0.5));
                animationFrame = requestAnimationFrame(animateBars);
            };
            animateBars();
        } else {
            cancelAnimationFrame(animationFrame);
        }
        return () => cancelAnimationFrame(animationFrame);
    }, [isLoading]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        setIsLoading(true);
        try {
            const response = await axios.get(`http://127.0.0.1:5000/search?q=${query}`);
            setIsLoading(false);
            if (response.data) {
                navigate('/results', { state: { alibaba: response.data.alibaba, amazon: response.data.amazon } });
            } else {
                setError("No data returned from API");
            }
        } catch (error) {
            console.error('Error fetching data:', error);
            setError('Error fetching data. Please try again later.');
            setIsLoading(false);
        }
    };

    return (
        <div style={{ padding: '20px', maxWidth: '1200px', margin: 'auto' }}>
            <form onSubmit={handleSubmit} style={{ display: 'flex', justifyContent: 'center', marginBottom: '20px' }}>
                <input
                    type="search"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Search our products, deals and more."
                    style={{ flex: 1, padding: '10px', marginRight: '10px', border: '1px solid #ccc', borderRadius: '5px' }}
                    disabled={isLoading}
                />
                <button type="submit" style={{ backgroundColor: 'black', color: '#90AEAD', border: 'none', borderRadius: '5px', padding: '10px 20px', cursor: 'pointer' }} disabled={isLoading}>
                    {isLoading ? 'Loading...' : 'Search'}
                </button>
            </form>
            {error && <p style={{ color: 'red', textAlign: 'center' }}>{error}</p>}
            {isLoading && (
                <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '50px', margin: '20px' }}>
                    {barHeight.map((height, index) => (
                        <div key={index} style={{
                            backgroundColor: '#90AEAD',
                            width: '10px',
                            height: `${height * 15}px`, // Convert scale factor to px
                            margin: '0 2px',
                            transition: 'height 0.5s'
                        }} />
                    ))}
                </div>
            )}
        </div>
    );
};

export default SearchBar;
