from flask import Flask, Blueprint
from flask_restx import Api
from marsh import ma
from dababase import db

from marshmallow import ValidationError


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc='/doc', title='Plant Maneger API')
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        self.plant_ns = self.plant_ns()

        super().__init__()

    def plant_ns(self, ):
        return self.api.namespace(name='Plants', description='Plant related operate', path='/')

    def run(self, ):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
        )


server = Server()
