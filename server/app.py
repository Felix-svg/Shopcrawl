from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_cors import CORS
from scrape import search_amazon, search_alibaba
from routes.search import Search, SearchHistoryResource

# Create a Flask app instance
app = Flask(__name__)
CORS(app, origins="http://localhost:3000")

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

# Configure the database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the Flask-Restful API
api = Api(app)

# Import routes after app creation
from routes.home import Home
from routes.products import Products, ProductByID
from routes.categories import Categories, CategoryByID
from routes.login import Login
from routes.signup import Signup
from routes.search import Search
from server.routes.SearchHistoryResource import Search_history
from routes.users import Users, UserByID

# Add the db instance to the Flask app
db.init_app(app)

# Define resource classes for Amazon and Alibaba products
class AmazonProducts(Resource):
    def get(self, product_name):
        products = search_amazon(product_name)
        return jsonify(products)

class AlibabaProducts(Resource):
    def get(self, product_name):
        products = search_alibaba(product_name)
        return jsonify(products)

# Add routes for Amazon and Alibaba products
api.add_resource(AmazonProducts, "/amazon/products/<string:product_name>")
api.add_resource(AlibabaProducts, "/alibaba/products/<string:product_name>")

# Register routes with the API
api.add_resource(Home, "/")
api.add_resource(Products, "/products")
api.add_resource(ProductByID, "/products/<int:id>")
api.add_resource(Categories, "/categories")
api.add_resource(CategoryByID, "/categories/<int:id>")
api.add_resource(Login, "/login")
api.add_resource(Signup, "/signup")
api.add_resource(Search, "/search")
api.add_resource(Search_history, "/search_history")
api.add_resource(Users, "/users")
api.add_resource(UserByID, "/users/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
