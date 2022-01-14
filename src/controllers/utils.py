from datetime import date, datetime


def responsify(res: dict | list):

    if isinstance(res, dict):
        return responsify_dict(res)
    
    if isinstance(res, list):
        return responsify_list(res)
    
    message: str
    message = 'You should not be sending anything but a dict or list back from a REST API'

    raise TypeError(message)


def responsify_list(iter: list) -> list:
    return [responsify_dict(x) for x in iter]


def responsify_dict(obj: dict) -> dict:
    response: dict
    response = {}

    for key, value in obj.items():
        
        if isinstance(value, datetime):
            value: datetime | date
            value = value.isoformat()
        
        response[key] = value
    
    return response