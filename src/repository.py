from typing import Any
from src.database.database_setup import build_session
from src.database.database_entities import EntityBase
from sqlalchemy.orm import Query
from sqlalchemy import func



def get_from_db(entity_type: type[EntityBase]):
    session = build_session()

    entities: list[entity_type]
    entities = session.query(entity_type).all()
    session.close()

    return entities


def get_with_filter_from_db(entity_type: type[EntityBase], query_object: dict):
    session = build_session()

    query: Query
    query = session.query(entity_type)

    query_object_items: list[tuple[str, Any]]
    query_object_items = query_object.items()
    
    for key, value in query_object_items:
        attribute = getattr(entity_type, key)

        comparator_left = attribute
        comparator_right = func.lower(value) if type(value) is str else value
        comparator = comparator_left == comparator_right

        query = query.filter(comparator)

    entities: list[entity_type]
    entities = query.all()
    session.close()

    return entities


def get_by_id_from_db(entity_type: type[EntityBase], id: int):
    session = build_session()

    entity: entity_type
    entity = session.query(entity_type).get(id)
    session.close()

    return entity


def post_to_db(entity_type: type[EntityBase], entity_to_create: dict):
    entity: entity_type
    entity = entity_type().from_dict(entity_to_create)

    session = build_session()
    session.add(entity)
    session.commit()
    session.close()

    return entity