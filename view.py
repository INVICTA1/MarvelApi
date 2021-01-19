from app import db
from flask import Blueprint
from models import *
from typing import Optional

comics = Blueprint('comics', __name__)
import service


@comics.route('/characters', methods=['GET'])
def get_comics():
    comics = service.get_comics()
    # надо сделать сереализацию на преобразование данных
    return comics[0].title


# т к данный метод может что то вернуть либо ничего не вернуть, то в этом случае нужно вернуть другой тип объекта
# Optional(Comics)

@comics.route('/characters/<id>', methods=['GET'])
def get_comics_by_id(id: int) -> Optional[Comics]:
    comics = Comics.query.get(id)
    return comics.diamondCode

# print(get_comics())
# comic: Optional[Comics] = get_comics_by_id(2)
# if comic:
#     print(comic)
