from flask import Blueprint, request, jsonify, make_response
from src.creators.models import CreatorSchema, Creator
from src.creators import service

creators = Blueprint('creators', __name__)
creator_schema = CreatorSchema()
creators_schema = CreatorSchema(many=True)


@creators.route('/creators', methods=['GET'])
def get_creators():
    get_creators = Creator.query.all()
    result = creators_schema.dump(get_creators)
    return jsonify(result)


@creators.route('/creators/<id>', methods=['GET'])
def get_creators_by_id(id):
    get_creator = Creator.query.get(id)
    result = creator_schema.dump(get_creator)
    return jsonify(result)


@creators.route('/creators', methods=['POST'])
def add_creators():
    data = request.get_json(force=True)
    get_creator = creator_schema.load(data)
    creator_object = service.add_creator(get_creator)
    result = creator_schema.dump(creator_object)
    return make_response(jsonify({"creator": result}), 201)


@creators.route('/creators/<id>', methods=['PUT'])
def update_creator_by_id(id):
    data = request.get_json(force=True)
    get_creator = Creator.query.get(id)
    if data and get_creator:
        update_creator = service.update_creator_by_id(data, get_creator)
        result = creator_schema.dump(update_creator)
        return jsonify({"creator": result}, 201)
    else:
        return jsonify(status=404)


@creators.route('/creators/<id>', methods=['DELETE'])
def delete_creator_by_id(id):
    result = service.delete_creator_by_id(id)
    return make_response(jsonify(status=result))
