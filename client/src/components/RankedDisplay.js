import React from "react";
import { getWebsiteNameFromUrl } from "../utils";

const RankProductCard = ({ product, index, indexOfFirstProduct }) => { 

  return (
    <div className="col mb-4" key={index}>
      <div className="card">
        <div className="card-body">
          <h5 className="card-title">Rank {indexOfFirstProduct + index}</h5>
          <p className="card-text">
            <strong>Product 1:</strong> {product.product1.product_name}, Price: {product.product1.product_price}, Rating: {product.product1.product_rating}
            <br />
            Product 1 Source: {getWebsiteNameFromUrl(product.product1.product_source)}
            <br />
            <strong>Product 2:</strong> {product.product2.product_name}, Price: {product.product2.product_price}, Rating: {product.product2.product_rating}
            <br />
            Product 2 Source: {getWebsiteNameFromUrl(product.product2.product_source)}
            <br />
            <strong>Product 3:</strong> {product.product3.product_name}, Price: {product.product3.product_price}, Rating: {product.product3.product_rating}
            <br />
            Product 3 Source: {getWebsiteNameFromUrl(product.product3.product_source)}
            <br />
            <strong>Marginal Benefit:</strong> {product.marginal_benefit}
            <br />
            <strong>Cost Benefit:</strong> {product.cost_benefit}
          </p>
        </div>
      </div>
    </div>
  );
};

export default RankProductCard;
