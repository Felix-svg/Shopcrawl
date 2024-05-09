from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


class Category(db.model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"Category name: {self.name}, product Description: {self.description}."
    
    
    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            return ValueError('Name must be a string')
        
        if not 0 <= len (name) <= 200 :
            return ValueError('Category name must be between 0 and 200 characters')
        
        return name
    
    @validates('description')
    def validate_description(self, key, description):
        if not description:
            return ValueError('Product description cannot be empty') 
        
        return description   