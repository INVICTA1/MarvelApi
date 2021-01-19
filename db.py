from models import *


def get_comics() -> list:
    return Comics.query.all()
