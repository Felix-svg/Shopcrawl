import React from 'react';
import { Slide } from 'react-slideshow-image';
import 'react-slideshow-image/dist/styles.css';
import juiceImage from "../components/images/Juices-and-Other-Drinks-scaled.jpg";
import perfumeImage from "../components/images/perfume.jpg";
import makeup2 from "../components/images/makeup2.jpg";
import womenImage from "../components/images/Mumias-Sugar-Company.jpg";
import equipImage from "../components/images/Note-20-Ultra-5G-256GB.jpg";
import serImage from "../components/images/DISCOUNT.jpg";
import womenPerfumeImage from "../components/images/women perfume.jpg";

function Home() {
    const images = [
        juiceImage, perfumeImage, makeup2, womenImage, equipImage, serImage
    ];

    const cardImages = [
        [womenPerfumeImage, makeup2, perfumeImage],
        [juiceImage, serImage, womenImage],
        [equipImage, serImage, perfumeImage],
        [womenImage, juiceImage, makeup2],
        [womenImage, makeup2, perfumeImage],
        [juiceImage, serImage, equipImage],
        [womenPerfumeImage, equipImage, serImage],
        [womenImage, womenPerfumeImage, perfumeImage],
        [womenImage, womenPerfumeImage, perfumeImage],
        [womenImage, womenPerfumeImage, perfumeImage]
    ];

    return (
        <div style={{ backgroundColor: '#90AEAD', minHeight: '90vh', padding: '20px' }}>
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

            {/* Slideshow */}
            <div style={{ position: 'relative', width: '100%', height: '400px', overflow: 'hidden' }}>
                <Slide easing="ease" duration={2000} transitionDuration={500} infinite={true} indicators={true} arrows={false} autoplay={true}>
                    {images.map((each, index) => (
                        <div key={index} className="each-slide" style={{ position: 'relative', width: '100%', height: '600px', backgroundSize: 'cover', backgroundPosition: 'center', backgroundImage: `url(${each})` }}>
                            {/* Overlay */}
                            <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', backgroundColor: 'rgba(144, 238, 144, 0.5)' }}></div>
                        </div>
                    ))}
                </Slide>

                {/* Sale Banner */}
                <div style={{ position: 'absolute', top: '50%', left: '30%', transform: 'translate(-50%, -50%)', color: 'black', textAlign: 'left', zIndex: 20, fontSize: '1.5rem', padding: '20px', borderRadius: '15px' }}>
                    <h1>UP TO 60% OFF!</h1>
                    <h3>DON'T MISS OUT ON SPECIAL ITEMS ON SALE.</h3>
                    <button style={{ marginTop: '20px', padding: '10px 20px', backgroundColor: '#90AEAD', color: 'black', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>Shop Now</button>
                </div>
            </div>

            {/* Cards */}
            <div style={{ display: 'flex', justifyContent: 'center', marginTop: '50px', flexWrap: 'wrap' }}>
                {cardImages.map((cards, index) => (
                    <div key={index} style={{ margin: '0 20px 20px', width: '200px', backgroundColor: '#ffffff', borderRadius: '10px', padding: '20px', boxShadow: '0px 0px 10px rgba(0, 0, 0, 0.1)' }}>
                        <Slide easing="ease" duration={2000} transitionDuration={500} infinite={true} indicators={true} arrows={false} autoplay={true}>
                            {cards.map((image, index) => (
                                <div key={index} className="each-slide" style={{ width: '100%', height: '100%' }}>
                                    <img src={image} alt={`Slide ${index}`} style={{ width: '100%', height: '100%', objectFit: 'cover', borderRadius: '10px' }} />
                                </div>
                            ))}
                        </Slide>
                        <h2>Food Items {index + 1}</h2>
                        <p>Description of card {index + 1}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Home;
