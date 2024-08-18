from config import app, api, jwt


from routes.home import Home
from routes.products import Products, ProductByID
from routes.categories import Categories, CategoryByID
from routes.login import Login
from routes.signup import Signup
from routes.search import search
from routes.search_history import SearchHistoryResource
from routes.users import UserByID
from routes.rank_products import RankProducts
from routes.reset_password import reset_password, forgot_password
from routes.refresh_token import refresh
from models.token_blocklist import Tokenblocklist


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = Tokenblocklist.query.filter_by(jti=jti).first()
    return token is not None

# Routes
api.add_resource(Home, "/")
api.add_resource(Products, "/products")
api.add_resource(ProductByID, "/products/<int:id>")
api.add_resource(Categories, "/categories")
api.add_resource(CategoryByID, "/categories/<int:id>")
api.add_resource(Login, "/login")
api.add_resource(Signup, "/signup")
api.add_resource(SearchHistoryResource, "/search_history")
api.add_resource(UserByID, "/users/<int:id>")
api.add_resource(RankProducts, "/rank_products")

app.add_url_rule("/search", view_func=search, methods=["GET"])
app.add_url_rule("/forgot-password", view_func=forgot_password, methods=["POST"])
app.add_url_rule("/reset-password/<token>", view_func=reset_password, methods=["POST"])
app.add_url_rule("/refresh", view_func=refresh, methods=["POST"])

if __name__ == "__main__":
    app.run()
