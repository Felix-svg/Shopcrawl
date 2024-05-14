import React, { useState, useEffect } from 'react';
import fetchdata from '../utils/fetchdata.js';

const Products = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const data = await fetchdata();
                setProducts(data);
                setLoading(false);
            } catch (error) {
                console.error('Error fetching data:', error);
                setError('Failed to load products');
                setLoading(false);
            }
        };

        fetchProducts();
    }, []);

    if (loading) return <div style={{ textAlign: 'center', fontSize: '24px', color: '#555' }}>Loading...</div>;
    if (error) return <div style={{ textAlign: 'center', fontSize: '24px', color: 'red', fontWeight: 'bold' }}>{error}</div>;

    return (
        <div style={{ padding: '20px' }}>
            <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center' }}>
                {products.map((product) => (
                    <div key={product.id} style={cardStyle} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
                        <img src={product.image} alt={product.title} style={imageStyle} />
                        <div style={cardContentStyle}>
                            <h2 style={{ fontSize: '16px', color: '#333', marginBottom: '5px' }}>{product.title}</h2>
                            <p style={{ fontSize: '14px', color: '#666', marginBottom: '10px' }}>{product.description}</p>
                            <p style={{ fontSize: '14px', fontWeight: 'bold', color: '#333' }}>${product.price}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

// Styles
const cardStyle = {
    margin: '5px',
    width: '250px',
    boxShadow: '0 2px 5px rgba(0,0,0,0.1)',
    borderRadius: '5px',
    overflow: 'hidden',
    backgroundColor: '#f5f5f5',
    border: '1px solid #ccc',
    transition: 'transform 0.2s, box-shadow 0.2s'
};

const imageStyle = {
    width: '100%',
    height: '160px', 
    objectFit: 'cover'
};

const cardContentStyle = {
    padding: '10px'
};

// Handlers for hover effect
function handleMouseEnter(e) {
    e.currentTarget.style.transform = 'scale(1.05)';
    e.currentTarget.style.boxShadow = '0 4px 8px rgba(0,0,0,0.2)';
}

function handleMouseLeave(e) {
    e.currentTarget.style.transform = 'scale(1)';
    e.currentTarget.style.boxShadow = '0 2px 5px rgba(0,0,0,0.1)';
}

export default Products;
