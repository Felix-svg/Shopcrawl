import React from 'react';
import 'ionicons';
import './SearchBar.css';

const SearchBar = () => {
  return (
    <div className="search-box">
      <div className="search-input">
        <input type="search" placeholder="Search our products, deals and more." />
      </div>
      <span className="search-btn">
        <button>
          <ion-icon name="search-sharp"></ion-icon>
          Search
        </button>
      </span>
    </div>
  );
}

export default SearchBar;
