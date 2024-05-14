from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class SearchHistory(db.Model, SerializerMixin):
    __tablename__ = "search_history"
    id = Column(Integer, primary_key=True)
    query = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))  # Add this line
    user = relationship("User", back_populates="search_history")

    def __repr__(self):
        return f"<SearchHistory {self.query}>"
