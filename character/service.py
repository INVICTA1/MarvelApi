from character import database
from character.models import Character


def get_characters() -> list:
    return database.get_characters()


def add_character(get_character):
    return database.add_character(get_character)


def update_character_by_id(data, get_character: Character):
    if data.get('available'):
        get_character.available = data['available']
    if data.get('collectionURI'):
        get_character.collectionURI = data['collectionURI']
    return database.update_character_by_id(get_character)


def delete_character_by_id(id) :
    get_character = Character.query.get(id)
    if get_character:
        database.delete_character_by_id(get_character)
        return 200
    else:
        return 404