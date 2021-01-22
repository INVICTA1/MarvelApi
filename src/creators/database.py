from src.creators.models import Creator
from src.app import db


def get_creators() -> list:
    return Creator.query.all()


def add_creator(get_creator: Creator):
    return get_creator.create()


def update_creator_by_id(get_creator: Creator):
    db.session.add(get_creator)
    db.session.commit()
    return get_creator


def delete_creator_by_id(get_creator: Creator):
    db.session.delete(get_creator)
    db.session.commit()
