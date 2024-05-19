import React from "react";
import { useState } from "react";


const InformationPanel = () => {
    const [showInformation, setShowInformation] = useState(false)

    const toggleInformation = () =>{
        setShowInformation(!showInformation)
    }

    return (
        <div className="container mt-3">
          <h2>How the Ranking Works</h2>
          {/* <p>Click on the button to toggle between showing and hiding content.</p> */}
          <button
            type="button"
            className={`btn ${showInformation ? "btn-light" : "btn-dark"}`}
            onClick={toggleInformation}
          >
            {showInformation ? "Hide Details" : "View Details"}
          </button>
          {showInformation && (
            <div className="information-content">
              <ul>
                <li>
                  Our tool ranks products from different e-commerce websites by applying Marginal Benefit and Cost Benefit formulas to factors such as Product Pricing and Consumer ratings.
                </li>
                <li>
                  The results include the product name, price, rating, cost benefit, and marginal benefit based on ranks.
                  <ul>
                    <li>
                      The higher the marginal benefit, the better it is to buy more of the product.
                    </li>
                    <li>
                      The higher the cost benefit, the better it is to buy a more pricey product.
                    </li>
                    <li>
                      If the marginal benefit is negative, it means there will not be a substantial benefit in purchasing more of the product; hence, you could explore other factors or products instead or adjust their importance. A positive marginal benefit indicates that increasing the quantity of products would provide a greater benefit.
                    </li>
                    <li>
                      A negative cost benefit is a signal that the cost outweighs the benefit of purchasing the product.
                    </li>
                  </ul>
                </li>
                <li>
                  Cost Benefit is the result of the price difference between products on different e-commerce websites. The price importance will determine this.
                </li>
                <li>
                  Marginal Benefit is the result of differences between factors such as price, ratings, based on your price and rating importance input.
                </li>
              </ul>
            </div>
          )}
        </div>
      );
      
  }
  
  export default InformationPanel;