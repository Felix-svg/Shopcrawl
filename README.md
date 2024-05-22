# Shopcrawl

## Overview
Shopcrawl enhances the online shopping experience by providing an advanced tool that computes the marginal benefit (MB) and cost-benefit (CB) analysis for products across multiple e-commerce platforms. This tool helps consumers make informed purchasing decisions by evaluating factors such as price, shipping costs, consumer ratings, and more through real-time data scraping.

# Problem Statement
In the dynamic world of online shopping, consumers frequently struggle to determine the optimal purchasing venue for products due to variations in pricing, shipping costs, consumer ratings, and payment options across platforms. Shopcrawl addresses this challenge by scraping data directly from these platforms, providing a robust MB and CB analysis to guide consumer choices.

# How It Works
### Data Retrieval
Initiates a data scraping sequence across selected e-commerce sites upon receiving a user's search query.

### Data Indexing
Indexes the scraped data in a structured temporary database for efficient retrieval and comparison.

### Analysis Application
Applies MB and CB calculations to the indexed data to assess each product’s overall value.

### Result Ranking
Ranks products based on the analysis and user preferences, ensuring the most beneficial options are highlighted.

## Features
Multi-Source Product Search**: Scrape and compare product data from multiple e-commerce platforms in real time.
Advanced Filtering: Users can adjust product rankings and displays based on personalized MB and CB criteria.
User Profiles: Supports account creation for personalized searches and preference saving.
History Tracking: Maintains a record of past searches for convenient reference and re-analysis.
Responsive Design: Mobile-friendly interface, ensuring ease of access on all devices.
Security: Implements stringent security protocols to safeguard user data during interactions.

## Technology Stack
Frontend: React, Redux Toolkit
Backend: Python Flask
Database: PostgreSQL
Design Tools: Figma
Testing: Jest, Minitests

## Setup and Installation

# Clone the repository
git clone https://github.com/Felix-svg/Shopcrawl.git

# Navigate to the project directory
cd shopcrawl

# Install dependencies for the client
cd client
npm install

# Install dependencies for the server
cd ../server
pip install -r requirements.txt

# Start the frontend
npm start # This will run on http://localhost:3000

# Start the backend
pipenv install
pipenv shell
flask db init
flask db migrate-m "message"
flask db upgrade head
python app.py
# Usage
Navigate to the project directory and start the client side first by running npm start. This will launch the frontend on http://localhost:3000.
Open another terminal and start the server by running flask run. This initiates the backend, which interacts with the frontend to deliver real-time data scraping functionality.
Enter a product name in the search bar on the homepage to see a comparative analysis across different platforms.

