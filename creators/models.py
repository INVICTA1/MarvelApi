from marshmallow_sqlalchemy import ModelSchema
from comics.models import Comics
from app import db

creator_comics = db.Table('creator_comics',
                             db.Column('creator_id',db.Integer,db.ForeignKey('creator.id')),
                             db.Column('comics_id',db.Integer,db.ForeignKey('comics.id')))

class Creator(db.Model):
    __tablename__='creator'
    id = db.Column(db.Integer(), primary_key=True)
    firstName = db.Column(db.String(100))
    middleName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    suffix = db.Column(db.String(100))
    fullName = db.Column(db.String(100))
    modified = db.Column(db.DateTime())
    comics =db.relationship(Comics,secondary=creator_comics,backref=db.backref('creators',lazy=True))

class CreatorSchema(ModelSchema):
    class Meta:
        model = Creator
        sqla_session = db.session