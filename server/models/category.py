from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Define a relationship with the Product model
    products = db.relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category {self.name}>"
