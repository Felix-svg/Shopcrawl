import re
from config import db, bcrypt
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from datetime import datetime


class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    _password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Define the relationship with SearchHistory
    search_history = db.relationship("SearchHistory", back_populates="user")

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password hashes may not be viewed.")

    @password_hash.setter
    def password_hash(self, password):
        if not self.validate_password(password):
            raise ValueError("Password must include at least one number, one uppercase letter, one lowercase letter, and one special character.")
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))

    @validates("email")
    def validate_email(self, key, email):
        if "@" not in email:
            raise ValueError("Email must include @")
        return email

    @staticmethod
    def validate_password(password):
        if (len(password) < 8 or
            not re.search(r"[A-Z]", password) or
            not re.search(r"[a-z]", password) or
            not re.search(r"\d", password) or
            not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
            return False
        return True

    def __repr__(self):
        return f"<User {self.username}>"
