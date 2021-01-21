from app import db, ma
from marshmallow_sqlalchemy import ModelSchema


class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    available = db.Column(db.Integer)
    collectionURI = db.Column(db.String(140))
    returned = db.Column(db.Integer)
    comic_id = db.Column(db.Integer, db.ForeignKey('comics.id'))


class CharacterSchema(ModelSchema):
    class Meta:
        model = Character
        sqla_session = db.session
