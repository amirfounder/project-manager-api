from flask import Flask, request
from flask_cors import CORS
from src.controllers import *
from src.database import setup_schema
from src.database.database_entities import *
from src.utils import *
from src.utils.utils import build_query_object, build_query_string, filter_query_object

app = Flask(__name__)
CORS(app)


def handle_request_with_id(entity_type: type[EntityBase], request: Request, id: str):
    id = int(id)
    if request.method == 'GET':
        return get_by_id_controller(entity_type, id)

    if request.method == 'PUT':
        return put_controller(entity_type, request, id)

    if request.method == 'DELETE':
        return delete_controller(entity_type, id)


def handle_request(entity_type: type[EntityBase], request: Request):
    if request.method == 'GET':
        
        query_string = build_query_string(request)
        query_object = build_query_object(query_string)
        query_object = filter_query_object(entity_type, query_object)

        query_object_items = query_object.items()

        if len(query_object_items) == 0:
            return get_controller(entity_type)
        
        else:
            return None

    if request.method == 'POST':
        return post_controller(entity_type, request)


@app.route('/columns/<id>', methods=['GET', 'PUT', 'DELETE'])
def columns_controller_with_id(id):
    return handle_request_with_id(Column, request, id)


@app.route('/columns', methods=['GET', 'POST'])
def columns_controller():
    return handle_request(Column, request)


@app.route('/projects/<id>', methods=['GET', 'PUT', 'DELETE'])
def projects_controller_with_id(id):
    return handle_request_with_id(Project, request, id)


@app.route('/projects', methods=['GET', 'POST'])
def projects_controller():
    return handle_request(Project, request)


@app.route('/cards/<id>', methods=['GET', 'PUT', 'DELETE'])
def cards_controller_with_id(id):
    return handle_request_with_id(Card, request, id)


@app.route('/cards', methods=['GET', 'POST'])
def cards_controller():
    return handle_request(Card, request)


if __name__ == '__main__':
    setup_schema()
    app.run(debug=True)
