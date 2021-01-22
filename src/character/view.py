from flask import Blueprint, request, jsonify, make_response
from src.character.models import CharacterSchema, Character
from src.character import service

characters = Blueprint('characters', __name__)

character_schema = CharacterSchema()
characters_schema = CharacterSchema(many=True)


@characters.route('/characters', methods=['GET'])
def get_characters() -> str:
    get_characters = service.get_characters()
    result = characters_schema.dump(get_characters)
    return jsonify(result)


@characters.route('/characters/<id>', methods=['GET'])
def get_character_by_id(id: int) -> dict:
    get_character = Character.query.get(id)
    result = character_schema.dump(get_character)
    return jsonify(result)


@characters.route('/characters', methods=['Post'])
def add_character() -> dict:
    data = request.get_json(force=True)
    get_character = character_schema.load(data)
    character_object = service.add_character(get_character)
    result = character_schema.dump(character_object)
    return make_response(jsonify({"character": result}), 201)


@characters.route('/characters/<id>', methods=['PUT'])
def update_character_by_id(id):
    data = request.get_json(force=True)
    get_character = Character.query.get(id)
    get_character = service.update_character_by_id(data, get_character)
    result = character_schema.dump(get_character)
    return make_response(jsonify({"comic": result}))


@characters.route('/characters/<id>', methods=['DELETE'])
def delete_character_by_id(id):
    result = service.delete_character_by_id(id)
    return make_response(jsonify(status=result))
