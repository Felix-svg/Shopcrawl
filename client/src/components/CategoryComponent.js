// CategoryComponent.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CategoryComponent = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    // Fetch categories from the backend when the component mounts
    fetchCategories();
  }, []);

  const fetchCategories = async () => {
    try {
      const response = await axios.get('https://shopcrawl-cjfb.onrender.com/categories');
      setCategories(response.data); // Assuming the backend returns an array of categories
    } catch (error) {
      console.error('Error fetching categories:', error);
    }
  };

  const handleClick = (categoryId) => {
    // Handle click event for category
    console.log('Category clicked:', categoryId);
    // You can navigate to a new page or perform other actions based on the category ID
  };

  return (
    <div>
      <h2>Categories</h2>
      <ul>
        {categories.map((category) => (
          <li key={category.id} onClick={() => handleClick(category.id)}>
            {category.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CategoryComponent;
