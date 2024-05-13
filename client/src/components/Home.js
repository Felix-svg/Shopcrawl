import React from 'react';
import equipImage from "../components/images/Note-20-Ultra-5G-256GB.jpg";
import serImage from "../components/images/DISCOUNT.jpg";
import womenPerfumeImage from "../components/images/women perfume.jpg";

function Home() {
    const cardsInfo = [
        {
            title: "Beauty Essentials",
            description: "Explore our premium range of perfumes and makeup.",
            image: womenPerfumeImage
        },
        {
            title: "Refreshments",
            description: "Juices and other refreshing beverages for your enjoyment.",
            image: serImage
        },
        {
            title: "Tech Gadgets",
            description: "Latest tech to keep you up-to-date.",
            image: equipImage
        },
        {
            title: "Daily Deals",
            description: "Don't miss out on our special daily deals!",
            image: serImage
        },
        // Add more card information as needed
    ];

    return (
        <div style={{ backgroundColor: '#90AEAD', minHeight: '150vh', padding: '20px' }}>
            {/* Navbar */}
            <nav style={{ color: 'black', padding: '10px 20px' }}>
                <ul style={{ listStyle: 'none', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                    <li style={{ marginRight: '50px' }}>Home</li>
                    <li style={{ marginRight: '50px' }}>Products</li>
                    <li style={{ marginRight: '50px' }}>About</li>
                    <li style={{ marginRight: '50px' }}>Contact</li>
                    {/* Search Bar */}
                    <li style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center' }}>
                        <input type="text" placeholder="Search..." style={{ padding: '5px', borderRadius: '10px', border: '1px solid black', marginRight: '10px' }} />
                        <button style={{ padding: '5px 10px', backgroundColor: 'black', color: '#90AEAD', border: '1px solid black', borderRadius: '5px', cursor: 'pointer' }}>Search</button>
                    </li>
                </ul>
            </nav>

            {/* Cards */}
            <div style={{ display: 'flex', justifyContent: 'center', marginTop: '50px', flexWrap: 'wrap' }}>
                {cardsInfo.map((card, index) => (
                    <div key={index} style={{ margin: '0 20px 20px', width: '200px', backgroundColor: '#ffffff', borderRadius: '10px', padding: '20px', boxShadow: '0px 0px 10px rgba(0, 0, 0, 0.1)' }}>
                        <img src={card.image} alt={card.title} style={{ width: '100%', height: '200px', objectFit: 'cover', borderRadius: '10px' }} />
                        <h2>{card.title}</h2>
                        <p>{card.description}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Home;