from datetime import date, datetime
from flask import jsonify, Response, Request
from src.database.database_entities import EntityBase
from inflector import Inflector


def convert_to_snake_case(data: str):
    inflector = Inflector()
    data = inflector.underscore(data)
    
    return data


def convert_request_body_to_snakecase(data: dict):
    data_items = data.items()
    data = {}

    for key, value in data_items:
        key_underscore = convert_to_snake_case(key)
        data[key_underscore] = value
    
    return data


def responsify(res: dict | list):
    responsified = dict | list[dict]

    if isinstance(res, dict):
        responsified = responsify_dict(res)
    
    elif isinstance(res, list):
        responsified = responsify_list(res)
    
    else:
        message: str
        message = 'You should not be sending anything but a dict or list back from a REST API'

        raise TypeError(message)
    
    response: Response
    response = jsonify(responsified)
    
    return response


def responsify_list(iter: list) -> list:
    responsified = [responsify_dict(x) for x in iter]
    responsified = tuple(responsified)

    return responsified


def responsify_dict(obj: dict) -> dict:
    response: dict
    response = {}

    for key, value in obj.items():
        
        if isinstance(value, datetime):
            value: datetime | date
            value = value.isoformat()
        
        response[key] = value
    
    return response


def build_query_string(request: Request):
    query: str
    path: str
    full_path: str

    path = request.path
    full_path = request.full_path
    
    query = full_path[len(path):]

    return query


def build_query_object(query_string: str):
    obj: dict
    obj = {}

    query_string_params: str
    query_string_params = query_string[1:]

    if query_string_params == '':
        return obj
    
    query_string_params = query_string_params.split('&')
    query_string_param_items = [tuple(x.split('=')) for x in query_string_params]

    for key, value in query_string_param_items:
        obj[key] = value

    return obj


def filter_query_object(entity_type: type[EntityBase], query_object: dict):
    filtered_obj: dict
    filtered_obj = {}

    column_names: list[str]
    column_names = entity_type.get_column_names()
    column_names = [x.lower() for x in column_names]

    query_object_items = query_object.items()
    query_object_items = list(query_object_items)

    for key, value in query_object_items:

        key = key.lower()
        
        try:
            value = int(value)
        except ValueError:
            pass
        
        if key in column_names:
            filtered_obj[key] = value

    return filtered_obj
