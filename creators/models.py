from marshmallow_sqlalchemy import ModelSchema
from comics.models import Comics, ComicsSchema
from app import db
from marshmallow import fields

creator_comics = db.Table('creator_comics',
                          db.Column('creator_id', db.Integer, db.ForeignKey('creator.id')),
                          db.Column('comics_id', db.Integer, db.ForeignKey('comics.id')))


class Creator(db.Model):
    __tablename__ = 'creator'
    id = db.Column(db.Integer(), primary_key=True)
    firstName = db.Column(db.String(100))
    middleName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    suffix = db.Column(db.String(100))
    fullName = db.Column(db.String(100))
    modified = db.Column(db.DateTime())
    comics = db.relationship(Comics, secondary=creator_comics, backref=db.backref('creators', lazy=True))

    def __init__(self, id, firstName, middleName, lastName, suffix, fullName, modified, comics):
        self.id = id
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.suffix = suffix
        self.fullName = fullName
        self.modified = modified
        self.comics = comics
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class CreatorSchema(ModelSchema):
    class Meta:
        model = Creator
        sqla_session = db.session

    id = fields.Integer()
    firstName = fields.String(required=True)
    middleName = fields.String(required=True)
    lastName = fields.String(required=True)
    suffix = fields.String(required=True)
    fullName = fields.String(required=True)
    modified = fields.String(required=True)
    comics = fields.Nested(ComicsSchema, many=True)
