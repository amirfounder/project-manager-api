from datetime import date, datetime
from flask import jsonify, Response


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