from flask import abort
from src.utils.exceptions import throw_not_found
from src.utils.utils import responsify
from src.repository import get_by_id_from_db, get_from_db, post_to_db
from src.database.database_entities import EntityBase

def get_service(entity_type: type[EntityBase]):
    entities: list[entity_type]
    entities = get_from_db(entity_type)
    entities = [x.to_dict() for x in entities]

    return entities


def get_by_id_service(entity_type: type[EntityBase], id: int):
    entity: entity_type
    entity = get_by_id_from_db(entity_type, id)
    
    if entity is None:
        message = 'Could not find entity with id: %i' %id
        throw_not_found(message)
    
    entity = entity.to_dict()

    return entity


def post_service(entity_type: type[EntityBase], entity_to_create: dict):
    entity: entity_type
    entity = post_to_db(entity_type, entity_to_create)
    entity = entity.to_dict()

    return entity


def put_service():
    return 'updated'


def delete_service():
    return 'deleted'
