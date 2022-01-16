from flask import Request
from src.utils.utils import responsify
from src.database.database_entities import EntityBase
from src.services import *


def get_controller(entity_type: type[EntityBase]):
    entities: list[entity_type]
    entities = get_service(entity_type)

    response = responsify(entities)
    response.status = 200

    return response


def get_controller_with_filter(entity_type: type[EntityBase], query_object: dict):
    entities: list[entity_type]
    entities = get_with_filter_service(entity_type, query_object)

    response = responsify(entities)
    response.status = 200

    return response


def get_by_id_controller(entity_type: type[EntityBase], id: int):
    entity: dict
    entity = get_by_id_service(entity_type, id)

    response = responsify(entity)
    response.status = 200

    return response


def post_controller(entity_type: type[EntityBase], request: Request):
    request_body: dict
    request_body = request.json

    entity: dict
    entity = post_service(entity_type, request_body)

    response = responsify(entity)
    response.status = 201

    return response


def put_controller(request: Request, id: int):
    request_body: dict
    request_body = request.json

    project: dict
    project = put_service(request_body, id)

    response_body = responsify(project)
    response_status = 200
    
    return response_body, response_status
    

def delete_controller(id: int):

    delete_service(id)
    response_status = 204

    return response_status