from flask import Flask, request

from src.utils.constants import FLASK_PROJECTS_ID_ENDPOINT, FLASK_PROJECTS_ENDPOINT
from src.services import *

app = Flask(__name__)


@app.route(FLASK_PROJECTS_ID_ENDPOINT, methods=['GET', 'PUT', 'DELETE'])
def projects_controller_1(id):

    if request.method == 'GET':
        get_project_by_id_service(id)

    if request.method == 'PUT':
        return update_project_service(id)

    if request.method == 'DELETE':
        return delete_project_service(id)


@app.route(FLASK_PROJECTS_ENDPOINT, methods=['GET', 'POST'])
def projects_controller_2():

    if request.method == 'GET':
        return get_projects_service()

    if request.method == 'POST':
        return create_project_service()


if __name__ == '__main__':
    app.run(debug=True)
