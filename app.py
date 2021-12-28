from flask import app, jsonify
from marshmallow import ValidationError

from marsh import ma
from dababase import db
from resources.plantController import Plant, PlantList

from server.instance import server

api = server.api
app = server.app


@app.before_first_request
def createTables():
    db.create_all()


api.add_resource(Plant, '/plants/<int:id>')
api.add_resource(PlantList, '/plants')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
