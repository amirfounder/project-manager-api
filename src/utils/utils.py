from datetime import date, datetime
import json


def serialize_datetime(obj):
    
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    
    message: str
    message = 'Could not serialize type: %s' % type(obj)

    raise TypeError(message)


def serialize(obj) -> str:
    return json.dumps(obj, default=serialize_datetime)
