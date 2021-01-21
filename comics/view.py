from flask import Blueprint, request, jsonify, make_response
from comics.models import ComicsSchema, Comics
from comics import service

comics = Blueprint('comics', __name__)

comic_schema = ComicsSchema()
comics_schema = ComicsSchema(many=True)


@comics.route('/comics', methods=['GET'])
def get_comics() -> str:
    comics = service.get_comics()
    result = comics_schema.dump(comics)
    return jsonify(result)



@comics.route('/comics/<id>', methods=['GET'])
def get_comics_by_id(id: int) -> dict:
    get_comic = Comics.query.get(id)
    result = comic_schema.dump(get_comic)
    return jsonify(result)


@comics.route('/comics', methods=['Post'])
def add_comics() -> dict:
    data = request.get_json(force=True)
    get_comic = comic_schema.load(data)
    comic_object = service.add_comics(get_comic)
    result = comic_schema.dump(comic_object)
    return make_response(jsonify({"comic": result}), 201)


@comics.route('/comics/<id>', methods=['PUT'])
def update_comics_by_id(id):
    data = request.get_json(force=True)
    get_comic = Comics.query.get(id)
    get_comic = service.update_comics_by_id(data, get_comic)
    result = comic_schema.dump(get_comic)
    return make_response(jsonify({"comic": result}))


@comics.route('/comics/<id>', methods=['DELETE'])
def delete_comics_by_id(id):
    result = service.delete_comics_by_id(id)
    return make_response(jsonify(status=result))
