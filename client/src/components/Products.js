import { useState, useEffect } from "react";

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
              <div className="card-body">
                <h5 className="card-title">{product.name}</h5>
                <p className="card-text">{product.description}</p>
              </div>
              <div className="card-footer">
                <small className="text-muted">Price: {product.price}</small>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Products;