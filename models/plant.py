from dababase import db


class PlantModel(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    about = db.Column(db.Text(), nullable=True)
    photo = db.Column(db.String(255), nullable=False, unique=True)
    times = db.Column(db.Integer, nullable=False)
    repeat_every = db.Column(db.String(40), nullable=False)
    enviroments = db.Column(db.String(), nullable=True)

    def __init__(self, name, about, photo, times, repeat_every, enviroments) -> None:
        self.name = name
        self.about = about
        self.photo = photo
        self.times = times
        self.repeat_every = repeat_every
        self.enviroments = enviroments

    def __repr__(self) -> str:
        return f'PlantModel(name={self.name}, about={self.about}, photo={self.photo}, times={self.times}, repeat_every={self.repeat_every}, enviroments={self.enviroments})'

    def json(self, ):
        return {
            'name': self.name,
            'about': self.about,
            'photo': self.photo,
            'enviroment': [self.enviroments],
            'frequency': {
                'times': self.times,
                'repeat_every': self.repeat_every
            }
        }

    @classmethod
    def findByName(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def findById(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def findAll(cls):
        return cls.query.all()

    def saveToDB(self, ):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()
