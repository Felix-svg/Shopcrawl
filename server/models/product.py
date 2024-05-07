from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


class Product(db.Model, SerializerMixin):
    pass
