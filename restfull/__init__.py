from flask import Flask, request
from flask_restful import Resource, Api, abort
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required
import secrets


app = Flask(__name__)
api = Api(app)
app.config["JWT_SECRET_KEY"] = secrets.token_hex(16)
jwt = JWTManager(app)

