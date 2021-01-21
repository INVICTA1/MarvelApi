from app import db, ma
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from datetime import datetime
from character.models import CharacterSchema


class Comics(db.Model):
    __tablename__ = 'comics'
    id = db.Column(db.Integer, primary_key=True)
    digitalId = db.Column(db.Integer)
    title = db.Column(db.String(140))
    issueNumber = db.Column(db.Integer)
    variantDescription = db.Column(db.String(140))
    description = db.Column(db.Text)
    modified = db.Column(db.DateTime)
    isbn = db.Column(db.String(140))
    upc = db.Column(db.Integer)
    diamondCode = db.Column(db.String(140))
    ean = db.Column(db.String(140))
    issn = db.Column(db.String(140))
    format = db.Column(db.String(140))
    pageCount = db.Column(db.Integer)
    resourceURI = db.Column(db.String(140))
    characters = db.relationship("Character")

    def __str__(self) -> str:
        return 'id: {0} title: {1}'.format(self.id, self.title)

    def __init__(self, id, digitalId, title, issueNumber, variantDescription, modified, description, isbn, upc,
                 diamondCode, ean,
                 issn, format, pageCount, resourceURI, characters=[]):
        self.id = id
        self.digitalId = digitalId
        self.title = title
        self.issueNumber = issueNumber
        self.variantDescription = variantDescription
        self.description = description
        self.modified = datetime.now()
        self.isbn = isbn
        self.upc = upc
        self.diamondCode = diamondCode
        self.ean = ean
        self.issn = issn
        self.format = format
        self.pageCount = pageCount
        self.resourceURI = resourceURI
        self.characters = characters

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class ComicsSchema(ModelSchema):
    class Meta:
        model = Comics
        sqla_session = db.session

    id = fields.Integer()
    digitalId = fields.Integer()
    title = fields.String(required=True)
    issueNumber = fields.Integer()
    variantDescription = fields.String(required=True)
    description = fields.String(required=True)
    modified = fields.DateTime(default=datetime.now())
    isbn = fields.String(required=True)
    upc = fields.Integer()
    diamondCode = fields.String(required=True)
    ean = fields.String(required=True)
    issn = fields.String(required=True)
    format = fields.String(required=True)
    pageCount = fields.Integer()
    resourceURI = fields.String(required=True)
    characters = fields.Nested(CharacterSchema, many=True)

# class UrlsComics(db.Model):
#     type = db.Column(db.String(140))
#     url = db.Column(db.String(240))
#
#
# class SeriesComics(db.Model):
#     resourceURI = db.Column(db.String(140))
#     name = db.Column(db.String(140))
#
#
# class VariantsComics(db.Model, SeriesComics):
#     pass
#
#
# class DatesComics(db.Model):
#     type = db.Column(db.String(140))
#     date = db.Column(db.DateTime)
#
# class PricesComics(db.Model):
#     type = db.Column(db.String(140))
#     date = db.Column(db.DateTime)
#
#
#
# class ResultCharacter(db.Model):
#     __tablename__ = 'characters_result'
#     result = db.Column(db.Text)


# class Character(db.Model):
#     __tablename__ = 'characters'
#     id = db.Column(db.Integer, primary_key=True)
#     offset = db.Column(db.Integer)
#     limit = db.Column(db.Integer)
#     total = db.Column(db.Integer)
#     count = db.Column(db.Integer)
# result = relationship('', backref="")
