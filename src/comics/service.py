from src.comics.models import Comics
from src.comics import database


def get_comics() -> list:
    return database.get_comics()


def add_comics(comic):
    return database.add_comics(comic)


def update_comics_by_id(data, get_comic: Comics):
    if data.get('isbn'):
        get_comic.isbn = data['isbn']
    if data.get('issn'):
        get_comic.isbn = data['issn']
    return database.update_comics_by_id(get_comic)


def delete_comics_by_id(id):
    get_comic = Comics.query.get(id)
    if get_comic:
        database.delete_comics_by_id(get_comic)
        return 200
    else:
        return 404