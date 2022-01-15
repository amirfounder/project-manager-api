from flask import Flask, request
from flask_cors import CORS
from src.controllers import *
from src.controllers.base_controller import *
from src.data import setup_schema
from src.data.entities import *
from src.utils import *

app = Flask(__name__)
CORS(app)


@app.route(FLASK_PROJECTS_ID_ENDPOINT, methods=['GET', 'PUT', 'DELETE'])
def projects_controller_1(id):

    if request.method == 'GET':
        return get_by_id_controller(Project, request, id)

    if request.method == 'PUT':
        return put_controller(Project, request, id)

    if request.method == 'DELETE':
        return delete_controller(Project, id)


@app.route(FLASK_PROJECTS_ENDPOINT, methods=['GET', 'POST'])
def projects_controller_2():

    if request.method == 'GET':

        if request.query_string == '':
            return get_controller(Project)

        else:
            return None
            
    if request.method == 'POST':
        return post_controller(Project, request)


if __name__ == '__main__':
    setup_schema()
    app.run(debug=True)
