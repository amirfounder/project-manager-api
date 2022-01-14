from venv import create
from src.data.project_repository import create_project


def get_projects_service():
    return 'got'

def get_project_by_id_service():
    return 'got by id'

def create_project_service():
    project = create_project({'name': 'lol'})
    project = project.to_dict()
    
    return project

def update_project_service():
    return 'updated'

def delete_project_service():
    return 'deleted'