from app import db
from models import *
from typing import Optional


def get_comics() -> list:
    comics = Comics.query.all()
    return comics


# т к данный метод может что то вернуть либо ничего не вернуть, то в этом случае нужно вернуть другой тип объекта
# Optional(Comics)
def get_comics_by_id(id: int) -> Optional[Comics]:
    comics = Comics.query.get(id)
    return comics


print(get_comics())
comic: Optional[Comics] = get_comics_by_id(2)
if comic:
    print(comic)