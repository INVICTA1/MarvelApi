from src.comics.models import *


def get_comics() -> list:
    return Comics.query.all()


def add_comics(comic: Comics):
    return comic.create()


def update_comics_by_id(get_comic: Comics):
    db.session.add(get_comic)
    db.session.commit()
    return get_comic


def delete_comics_by_id(get_comic: Comics):
    db.session.delete(get_comic)
    db.session.commit()
