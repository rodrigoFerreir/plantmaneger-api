from flask import request
from flask_restx import Resource, fields

from models.plant import PlantModel
from schemas.plant import PlantSchema

from server.instance import server

plant_ns = server.plant_ns

plant_schema = PlantSchema()
plant_list_schema = PlantSchema(many=True)

item = plant_ns.model('Plant', {
    'name': fields.String(description='Plant name'),
    'about': fields.String(description='Plant about'),
    'photo': fields.String(description='Plant photo'),
    'times': fields.Integer(defaut=0),
    'repeat_every': fields.String(description='Plant repeat every'),
    'enviroments': fields.String(description='Plant enviroments'),

})


class Plant(Resource):
    def get(self, id):
        plant_data = PlantModel.findById(id)
        if plant_data:
            return plant_schema.dump(plant_data), 200
        return {'message': "Item not found."}, 404

    @plant_ns.expect(item)
    def put(self, id):
        plant_data = PlantModel.findById(id)
        if plant_data:
            plant_json = request.get_json()

            plant_data.name = plant_json['name'] or plant_data.name
            plant_data.about = plant_json['about'] or plant_data.about
            plant_data.photo = plant_json['photo'] or plant_data.photo
            plant_data.times = plant_json['times'] or plant_data.times
            plant_data.repeat_every = plant_json['repeat_every'] or plant_data.repeat_every
            plant_data.enviroments = plant_json['enviroments'] or plant_data.enviroments

            plant_data.saveToDB()
            return plant_schema.dump(plant_data), 200
        return {'message': 'Plant not found'}, 404

    def delete(self, id):
        plant_data = PlantModel.findById(id)
        if plant_data:
            plant_data.deleteFromDB()
            return {'message': 'Plant deleted'}, 204
        return {'message': 'Plant not found'}, 404


class PlantList(Resource):
    def get(self):
        plant_data = PlantModel.findAll()
        if plant_data:
            return plant_list_schema.dump(plant_data), 200
        return {'message': 'Not found'}

    @plant_ns.expect(item)
    @plant_ns.doc('Create item')
    def post(self,):
        plant_json = request.get_json()
        plant_data = plant_schema.load(plant_json)

        plant_data.saveToDB()

        return plant_schema.dump(plant_data), 201
