from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from datetime import datetime



class SearchHistory(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    search_term = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    
    
    def __init__(self, user_id, product_id, search_term):
        self.user_id = user_id
        self.product_id = product_id
        self.search_term = search_term
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"SearchHistory(user_id={self.user_id}, product_id={self.product_id}, search_term='{self.search_term}', timestamp='{self.timestamp}')"

    @validates('user_id', 'product_id')
    def validate_id(self, key, value):
        if not isinstance(value, int):
            raise ValueError(f"{key} must be an integer")
        
        return value
    

    @validates('search_term')
    def validate_search_term(self, key, search_term):
        if not isinstance(search_term, str):
            raise ValueError('search term must be a string')
        
        if len(search_term) > 255:
            raise ValueError('search term exceeds the maximum length of 255 characters.')
        
        return search_term
    
    