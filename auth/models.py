from flask import current_app
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from . import db, login_manager
import json


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column("email", db.String(50), index=True,
                      unique=True, nullable=False)
    password_hash = db.Column("passwordHash", db.String(128), nullable=False)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    @classmethod
    def get_user(cls, email=None):
        user = cls.query.filter_by(email=email).first(
        )
        return user if user else False

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def create_user(cls, email, password):
        if not cls.get_user(email=email):
            user = cls(email=email)
            user.password = password
            db.session.add(user)
            db.session.commit()
            return user
        return False

    @classmethod
    def login(cls, email, password):
        user = cls.get_user(email=email)
        if user and user.verify_password(password):
            auth_token = user.generate_auth_token()
            return user, auth_token
        return None, None

    def generate_auth_token(self, expires_in=3600):
        s = Serializer(current_app.config.get(
            'SECRET_KEY'), expires_in=expires_in)
        return s.dumps({'id': str(self.id)}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config.get('SECRET_KEY'))
        try:
            data = s.loads(token)
        except SignatureExpired:
            return "Token Expired. Please Log in"
        except BadSignature:
            return "Bad Token. Please Log in"
        user = User.query.get(data['id'])
        return user

    def __repr__(self):
        return "<User {}>".format(self.email)

    def profile(self):
        return {'email': self.email}


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
