from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from datetime import datetime

class SearchHistory(db.Model, SerializerMixin):
    __tablename__ = "search_history"
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", back_populates="search_history")

    @validates("query")
    def validate_query(self, key, query):
        if not isinstance(query, str):
            raise ValueError("Query must be a string")
        if len(query) > 255:
            raise ValueError("Query exceeds the maximum length of 255 characters.")
        return query

    def __repr__(self):
        return f"<SearchHistory {self.query} {self.timestamp}>"