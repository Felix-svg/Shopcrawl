
#!/usr/bin/env python3
from config import app, api


# Routes
from routes.home import Home
from routes.products import Products, ProductByID
from routes.categories import Categories, CategoryByID
from routes.login import Login
from routes.signup import Signup
from routes.search import Search
from routes.search_history import Search_history
from routes.users import Users, UserByID

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
