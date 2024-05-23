from flask import Flask, render_template
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import Swagger
import os


app = Flask(__name__)

app.secret_key = "138ff724cdb6b3ec36782dc7fe1bb6ad7075a2830842c5bc5e839a4d8c8edef6"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

# @app.errorhandler(404)
# def not_found(e):
#     return render_template("index.html")

api = Api(app)
bcrypt = Bcrypt(app)

CORS(app)

swagger = Swagger(app)

jwt = JWTManager(app)
