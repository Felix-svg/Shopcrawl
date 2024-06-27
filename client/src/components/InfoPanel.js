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
                Our tool ranks products from various e-commerce websites based on Marginal Benefit and Cost Benefit formulas, considering factors such as Product Pricing and Consumer Ratings.
              </li>
              <li>
                The results include product names, prices, ratings, and rankings based on cost benefit and marginal benefit.
                <ul>
                  <li>
                    A higher Marginal Benefit indicates greater benefit from purchasing more of the product.
                  </li>
                  <li>
                    The product with the highest price does not necessarily have the highest cost benefit. The cost benefit is a balance between the cost and the perceived benefits.
                  </li>
                  <li>
                    A lower Marginal Benefit suggests limited benefit in buying more of the product; in such cases, consider exploring other products or adjusting the importance of factors. A positive Marginal Benefit implies greater benefit from increasing product quantity.
                  </li>
                  <li>
                    Negative Cost Benefit suggests that the cost outweighs the benefit of purchasing the product.
                  </li>
                </ul>
              </li>
              <li>
                Cost Benefit is the difference between total benefits and costs of products from e-commerce sites, influenced by the input of price importance.
              </li>
              <li>
                Marginal Benefit is the ratio of total additional benefit to total probable additional goods consumed, influenced by your input for Price and Rating importance.
              </li>
              <li>
                For optimal results, input floating-point values for price and rating that sum up to 1.
              </li>
            </ul>
          </div>
          )}
        </div>
      );
      
  }
  
  export default InformationPanel;