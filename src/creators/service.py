from src.creators.models import Creator
from src.creators import database
from datetime import datetime

def get_creators() -> list:
    return database.get_creators()


def add_creator(get_creator):
    return database.add_creator(get_creator)


def update_creator_by_id(data, get_creator: Creator):
    if data.get('firstName'):
        get_creator.firstName = data['firstName']
    if data.get('middleName'):
        get_creator.middleName = data['middleName']
    if data.get('lastName'):
        get_creator.lastName = data['lastName']
    if data.get('suffix'):
        get_creator.suffix = data['suffix']
    if data.get('fullName'):
        get_creator.fullName = data['fullName']
    get_creator.modified = datetime.now()
    return database.update_creator_by_id(get_creator)


def delete_creator_by_id(id):
    get_creator = Creator.query.get(id)
    if get_creator:
        database.delete_creator_by_id(get_creator)
        return 200
    else:
        return 404