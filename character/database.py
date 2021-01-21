from character.models import *


def get_characters() -> list:
    return Character.query.all()


def add_character(get_character: Character):
    return get_character.create()


def update_character_by_id(get_character: Character):
    db.session.add(get_character)
    db.session.commit()
    return get_character


def delete_character_by_id(get_character: Character):
    db.session.delete(get_character)
    db.session.commit()
