from src.data.core import build_session
from src.data.entities import EntityBase


def get_from_db(entity_type: type[EntityBase]):
    session = build_session()

    entities: list[entity_type]
    entities = session.query(entity_type).all()

    return entities


def get_by_id_from_db(entity_type: type[EntityBase], id: int):
    session = build_session()

    entity: entity_type
    entity = session.query(entity_type).get(id)

    return entity


def post_to_db(entity_type: type[EntityBase], entity_to_create: dict):
    entity: entity_type
    entity = entity_type().from_dict(entity_to_create)

    session = build_session()
    session.add(entity)
    session.commit()

    return entity