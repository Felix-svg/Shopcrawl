import React, { useState } from 'react';
import axios from 'axios';

const RankProduct = () => {
    const [productName, setProductName] = useState('')
    const [userWeights, setUserWeights] = useState({
        'price importance':'',
        'rating importance':''
    })
    const [rankedProducts, setRankedProducts] = useState([])
    const [calculating, setCalculating] = useState(false);

    const handleInputChange = (event) => {
        setProductName(event.target.value)
    }

    const handleWeightChange = (event) => {
        const {name, value} = event.target
        setUserWeights(prevState => ({
            ...prevState,
            [name]: value
        }))
    }

    // const handleSearch = () => {
    //     setCalculating(true)

    //     axios.post("/rank_products", {product_name: productName, user_weights: userWeights})
    //         .then(response => {
    //             setRankedProducts(response.data)
    //             setCalculating(false)
    //         })
    //         .catch(error => {
    //             console.error('Error fetching ranked products:', error)
    //             setCalculating(false)

    //         })
    // }
    

    const handleSearch = () => {
        setCalculating(true);
    
        fetch("http://127.0.0.1:5000/rank_products", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                product_name: productName,
                user_weights: userWeights
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            setRankedProducts(data);
            setCalculating(false);
        })
        .catch(error => {
            console.error('Error fetching ranked products:', error);
            setCalculating(false);
        });
    }
    
    return (
        <div>
            <div>
                <label>Product Name:</label>
                <input
                    type="text"
                    value={productName}
                    onChange={handleInputChange}
                    placeholder="Enter product name"
                />
            </div>

            <div>
                <label>Price Importance between 0 and 1: </label>
                <input
                    type="text"
                    name="price importance"
                    value={userWeights['price importance']}
                    onChange={handleWeightChange}
                    placeholder="Enter level of importance"
                />
            </div>

            <div>
                <label>Rating Importance between 0 and 1: </label>
                <input
                    type="text"
                    name="rating importance"
                    value={userWeights['rating importance']}
                    onChange={handleWeightChange}
                    placeholder="Enter level of importance"
                />
            </div>

            <button onClick={handleSearch}>Search</button>

            {calculating && <p>Calculating ranking...</p>}

            <div>
                <h4>Ranked Products</h4>
                <ul>
                    {rankedProducts.map((product, index) => (
                        <li key={index}>
                            {product.product_name} - {product.product_price}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    )
}   


export default RankProduct;