# Shopcrawl

Shopcrawl is a web application designed to help users find the best deals on products by retrieving data from various e-commerce sites and ranking the products based on multiple factors such as price and rating. The goal is to provide users with a comprehensive comparison of products from popular e-commerce platforms like Alibaba, Amazon, and Jumia, ensuring they can make informed purchasing decisions.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [User Experience](#user-experience)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Product Search**: Users can search for products using keywords.
- **Data Retrieval**: Scrapes product data from Alibaba, Amazon, and Jumia.
- **Product Ranking**: Ranks products based on price and rating.
- **User Authentication**: Allows users to create accounts and log in.
- **Customized Ranking**: Logged-in users can choose to rank products based on their preferences (price or rating).
- **Product Links**: Direct links to purchase products from the respective e-commerce sites.

## Technologies Used

- **Backend**: Python, Flask
- **Web Scraping**: BeautifulSoup, Requests
- **Database**: SQLite (for development), PostgreSQL (for production)
- **Frontend**: HTML, CSS, JavaScript, React
- **Authentication**: JSON Web Tokens
- **API Documentation**: Swagger

## Installation

1. **Clone the repository:**

    ```bash
    git clone git@github.com:Felix-svg/Shopcrawl.git
    cd Shopcrawl
    ```

### Backend

To get started with the backend of Shopcrawl, follow these steps:

1. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    or pipenv install
    pipenv shell
    ```

2. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the database:**

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

4. **Run the backend server:**

    ```bash
    python3 app.py
    ```

The backend server will be available at `http://127.0.0.1:5000`.

### Frontend

To get started with the frontend of Shopcrawl, follow these steps:

1. **Navigate to the client directory:**

    ```bash
    cd client
    ```

2. **Install the dependencies:**

    ```bash
    npm install
    ```

3. **Run the frontend server:**

    ```bash
    npm start
    ```

The frontend will be available at `http://localhost:3000`.


## Usage

### Non-Logged-In Users

1. **Landing Page**: Visit the landing page and click the "Explore" button to view products stored in the database.
2. **Explore Products**: Browse through the products and click the "Buy Product" link to view the product on the associated e-commerce site.

### Logged-In Users

1. **Sign Up**: Create an account by providing the required details.
2. **Log In**: Log in using your credentials.
3. **Search for Products**: Enter keywords in the search bar and initiate a search.
4. **View Results**: See products retrieved from Alibaba, Amazon, and Jumia, ranked by price.
5. **Customized Ranking**: Choose to rank products based on price or rating and view the updated rankings.
6. **Purchase Product**: Click the "Buy" link to purchase a product from the respective e-commerce site.

## API Endpoints

### Swagger Documentation

The API documentation is available at `http://127.0.0.1:5000/apidocs`.

### Example Endpoints

- **GET /api/products**: Retrieve all products.
- **POST /api/search**: Search for products by keywords.
- **GET /api/product/id**: Retrieve details of a specific product.

## User Experience

### Non-Logged-In Users

1. **Landing Page**: Start at the landing page.
2. **Explore Button**: Click the "Explore" button.
3. **Product List**: View a list of products saved in the database.
4. **Buy Product**: Click "Buy Product" to visit the product on the respective e-commerce site.

### Logged-In Users

1. **Account Creation**: Create an account or log in.
2. **Search Products**: Use the search functionality to find products.
3. **View and Rank Products**: View the scraped products and rank them by price or rating.
4. **Purchase**: Click the "Buy" link to proceed with the purchase on the e-commerce site.

## Testing

To run tests, use the following command:

```bash
pytest
```
This will run the test suite located in the tests directory.

## Contributing
We welcome contributions to Shopcrawl. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/your-feature).
5. Create a Pull Request.

## License
This project is licensed under the MIT License. See the <a href="/LICENSE">LICENSE</a> file for details.
