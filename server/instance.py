from flask import Flask, Blueprint
from flask_restplus import Api
from config import database_credetial
import uuid

from db import db
from ma import ma

from marshmallow import ValidationError

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/doc', title='Api do app Calendario')
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = database_credetial
        self.app.config['SECRET_KEY'] = uuid.uuid4().hex
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        self.user_ns = self.user_ns()


    def user_ns(self, ):
        return self.api.namespace(name='Users', description='user related operations', path='/')


    def run(self):
        self.app.run(
            port=3000,
            debug=True,
            host='0.0.0.0'
        )

server = Server()
