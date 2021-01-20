from flask import Blueprint, request, jsonify, make_response
from models import *
import service
from models import ComicsSchema
import json

comics = Blueprint('comics', __name__)

comic_schema = ComicsSchema()
comics_schema = ComicsSchema(many=True)


@comics.route('/characters', methods=['GET'])
def get_comics() -> str:
    comics = service.get_comics()
    result = comics_schema.dump(comics)
    return jsonify(result)


# т к данный метод может что то вернуть либо ничего не вернуть, то в этом случае нужно вернуть другой тип объекта
# Optional(Comics)

@comics.route('/characters/<id>', methods=['GET'])
def get_comics_by_id(id: int) -> dict:
    comic = Comics.query.get(id)
    result = comic_schema.dump(comic)
    return jsonify(result)


@comics.route('/characters', methods=['Post'])
def add_comics() -> dict:
    data = request.get_json(force=True)
    comic = comic_schema.load(data)
    comic_object = service.add_comics(comic)
    result = comic_schema.dump(comic_object)
    return make_response(jsonify({"comic": result}), 201)


@comics.route('/characters/<id>', methods=['PUT'])
def update_comics_by_id(id) :
    data = request.get_json(force=True)
    get_comic = Comics.query.get(id)
    get_comic = service.update_comics_by_id(data,get_comic)
    result = comic_schema.dump(get_comic)
    return make_response(jsonify({"comic": result}), 201)

    # comic = comic_schema.load(data)
    # result = comic_schema.dump(comic.create())
    # return make_response(jsonify({"comic": result}), 201)
