import re
import secrets

from flask import Blueprint, Response, abort, g, jsonify
from flask_httpauth import HTTPTokenAuth
from flask_restful import Api, Resource, reqparse, request

from .models import User

auth_ = HTTPTokenAuth(scheme="Bearer")

user_app = Blueprint('user_app', __name__)
api = Api(user_app)


class SignupAPI(Resource):
    model = User
    userParser = reqparse.RequestParser()
    userParser.add_argument('email', type=str, nullable=False)
    userParser.add_argument('password', type=str, nullable=False)

    def post(self):
        """
        Creates new user
        Parameters:
            -email (str)
            -password (str)
        """
        args = self.userParser.parse_args()
        email = args['email']
        password = args['password']

        if not (email and password):
            abort(400, "Some Parameter(s) are missing")
        if not validate_email(email):
            abort(400, "Invalid Email supplied")

        user = self.model.create_user(email=email,
                                      password=password)
        if not user:
            abort(409, "account found on platform, create_user unsuccessful.")
        g.user = user
        return {'status': 'success',
                'message': 'Account Created, proceed to login',
                }


class LoginAPI(Resource):
    model = User
    userParser = reqparse.RequestParser()
    userParser.add_argument('email', type=str, nullable=False)
    userParser.add_argument('password', type=str, nullable=False)

    def post(self):
        args = self.userParser.parse_args()
        response_object = {'status': 'Failed',
                           'message': 'Incorrect email or password'}
        
        email, password = args['email'], args['password']
        user, auth_token = self.model.login(email, password)
        
        if user:
            response_object = jsonify({'status': 'Success',
                                       'message': 'Login successful',
                                       'auth_token': auth_token
                                       })
        g.user = user
        return response_object


class Home(Resource):
    @auth_.login_required
    def get(self):
        return "Welcome {}".format(g.user.email)


@auth_.verify_token
def verify_token(token):
    user = User.verify_auth_token(token)

    if isinstance(user, str):
        abort(400, {"error": user})
    g.user = user
    return True

def validate_email(email):
    email_regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(email_regex,email)):
        return True
    return False

api.add_resource(SignupAPI, '/signup')
api.add_resource(LoginAPI, '/login')
api.add_resource(Home, '/')
