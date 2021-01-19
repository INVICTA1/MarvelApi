from app import db
import json


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
        return 'id: ' + str(self.id) + ' title: ' + self.title




class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    available = db.Column(db.Integer)
    collectionURI = db.Column(db.String(140))
    returned = db.Column(db.Integer)
    comic_id = db.Column(db.Integer, db.ForeignKey('comics.id'))


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
