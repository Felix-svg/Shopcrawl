import React, { useState, useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

const Products = () => {
  let [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/products")
      .then((resp) => {
        if (!resp.ok) {
          throw new Error("Error fetching data");
        }
        return resp.json();
      })
      .then((data) => {
        setProducts(data.products);
        console.log(data);
      })
      .catch((error) => console.error(error));
  }, []);

  return (
    <div className="container">
      <div className="row">
        {products.map((product) => (
          <div key={product.id} className="col-lg-4 col-md-6 col-sm-12 mb-4 mt-4">
            <div className="card h-100">
              <img
                src={product.image_src}
                className="card-img-top"
                alt={product.name}
                style={{ height: '80px', objectFit: 'cover' }}
              />
              <div className="card-body d-flex flex-column" style={{ height: '120px' }}>
                <h5 className="card-title" style={{ fontSize: '1rem' }}>{product.name}</h5>
                <p className="card-text" style={{ fontSize: '0.9rem' }}>{product.description}</p>
                <div className="mt-auto d-flex justify-content-center">
                  <a href={product.source} target="_blank" rel="noopener noreferrer" className="btn btn-link" style={{ fontSize: '0.9rem' }}>
                    Buy here
                  </a>
                </div>
              </div>
              <div className="card-footer">
                <small className="text-muted" style={{ fontSize: '0.8rem' }}>Price: {product.price}</small>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Products;
