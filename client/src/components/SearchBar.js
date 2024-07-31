import React, { useState } from "react";
import useAxios from "./useAxios"; // Adjust the import path accordingly
import { useNavigate } from "react-router-dom";
import "./SearchBar.css";

const SearchBar = () => {
  const axiosInstance = useAxios();
  const [query, setQuery] = useState("");
  const navigate = useNavigate();
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setIsLoading(true);
    try {
      const response = await axiosInstance.get(`/search?q=${query}`);
      setIsLoading(false);
      if (response.data) {
        navigate("/results", {
          state: {
            alibaba: response.data.alibaba,
            amazon: response.data.amazon,
            jumia: response.data.jumia
          },
        });
      } else {
        setError("No data returned from API");
      }
    } catch (error) {
      console.error("Error fetching data:", error);
      setError("Error fetching data. Please try again later.");
      setIsLoading(false);
    }
  };

  return (
    <div className="search-bar-container">
      <form onSubmit={handleSubmit} className="search-form">
        <input
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search products"
          className="search-input"
          disabled={isLoading}
        />
        {!isLoading && (
          <button
            type="submit"
            className="search-button"
            disabled={isLoading}
          >
            Search
          </button>
        )}
      </form>
      {error && <p className="error-message">{error}</p>}
      {isLoading && (
        <div className="animation-container">
          {[...Array(36).keys()].map((index) => (
            <div key={index} className={`baton-${index}`}>
              <div className="metronome">
                <div className="baton"></div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default SearchBar;