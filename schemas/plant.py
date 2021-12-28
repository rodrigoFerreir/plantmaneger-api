from flask_sqlalchemy import model
from marshmallow_sqlalchemy import load_instance_mixin
from marsh import ma

from models.plant import PlantModel


class PlantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PlantModel
        load_instance = True
