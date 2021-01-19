from models import *


def get_comics() -> list:
    return Comics.query.all()


def add_comics(comic) :
    print(comic)
    return comic.create
