import database
from models import Comics


def get_comics() -> list:
    # дергнуть database
    return database.get_comics()


def add_comics(comic):
    return database.add_comics(comic)


def update_comics_by_id(data, get_comic: Comics):
    if data.get('isbn'):
        get_comic.isbn = data['isbn']
    if data.get('issn'):
        get_comic.isbn = data['issn']
    return database.update_comics_by_id(get_comic)


