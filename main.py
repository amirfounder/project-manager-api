from flask import Flask, request
from src.controllers.project_controller import delete_project_controller, get_project_by_id_controller, get_projects_controller, post_project_controller, put_project_controller
from src.data.core import setup_schema

from src.utils.constants import FLASK_PROJECTS_ID_ENDPOINT, FLASK_PROJECTS_ENDPOINT
from src.controllers.utils import *

app = Flask(__name__)


@app.route(FLASK_PROJECTS_ID_ENDPOINT, methods=['GET', 'PUT', 'DELETE'])
def projects_controller_1(id):

    if request.method == 'GET':
        return get_project_by_id_controller(request, id)

    if request.method == 'PUT':
        return put_project_controller(request, id)

    if request.method == 'DELETE':
        return delete_project_controller(id)


@app.route(FLASK_PROJECTS_ENDPOINT, methods=['GET', 'POST'])
def projects_controller_2():

    if request.method == 'GET':
        return get_projects_controller(request)

    if request.method == 'POST':
        return post_project_controller(request)


if __name__ == '__main__':
    setup_schema()
    app.run(debug=True)
