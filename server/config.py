from dotenv import load_dotenv
from flask import Flask
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flasgger import Swagger
import os

load_dotenv()


app = Flask(__name__)

app.config["SECRET_KEY"] = '9k4c6nO9LF05gq8BAGKbo20BD1sgJGeBF97Tmu7nR20'
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_USE_TLS"] = True
app.config["JWT_SECRET_KEY"] = 'wzsbrK9wGvOqH6FSYWgv9xCju_ZrU6rbUEIEVuB7fqA'

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
bcrypt = Bcrypt(app)

CORS(app)

swagger = Swagger(app)

jwt = JWTManager(app)

mail = Mail(app)
