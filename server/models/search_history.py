from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


class SearchHistory(db.Model, SerializerMixin):
    pass
