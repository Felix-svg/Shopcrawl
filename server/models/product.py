from config import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime


class Product(db.Model, SerializerMixin):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    image_src = db.Column(db.String)
    source = db.Column(
        db.String
    )  # Store the source of the product (e.g., 'alibaba', 'amazon')
    rating = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Define the foreign key relationship with Category
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product {self.name} {self.price} {self.source} {self.timestamp}>"