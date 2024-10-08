import React, { useState, useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

const Products = () => {
  let [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("https://shopcrawl-server.onrender.com/products")
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
          <div key={product.id} className="col-lg-4 col-md-6 mb-4 mt-4">
            <div className="card h-100">
              <img
                src={product.image_src}
                className="card-img-top"
                alt={product.name}
              />
              <div className="card-body d-flex flex-column">
                <p className="card-title">{product.name}</p>
                <p className="card-text">{product.description}</p>
                <div className="mt-auto d-flex justify-content-center">
                  <a
                    href={product.source}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="btn btn-link"
                  >
                    Buy here
                  </a>
                </div>
              </div>
              <div className="card-footer">
                <strong>
                  <small className="text-muted">Price: {product.price}</small>
                </strong>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Products;
