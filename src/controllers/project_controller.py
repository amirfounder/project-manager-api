from flask import Request
from src.controllers.utils import responsify
from src.services import *


def get_projects_controller(request: Request):
    projects: list[dict]
    projects = get_projects_service()

    response_body = responsify(projects)
    
    response_status = 200

    return response_body, response_status


def get_project_by_id_controller(request: Request, id: int):
    request_body: dict
    request_body = request.json
    
    projects: dict
    projects = get_project_by_id_service(request_body, id)

    response_body = responsify(projects)
    response_status = 200

    return response_body, response_status


def post_project_controller(request: Request):
    request_body: dict
    request_body = request.json

    project: dict
    project = post_project_service(request_body)

    body = responsify(project)
    status = 201

    return body, status


def put_project_controller(request: Request, id: int):
    request_body: dict
    request_body = request.json

    project: dict
    project = put_project_service(request_body, id)

    response_body = responsify(project)
    response_status = 200
    
    return response_body, response_status
    

def delete_project_controller(id: int):

    delete_project_service(id)
    response_status = 204

    return response_status
