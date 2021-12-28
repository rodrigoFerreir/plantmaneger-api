from marsh import ma

from models.enviroment import EnviromentModel


class EnviromentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EnviromentModel
        load_instance = True
