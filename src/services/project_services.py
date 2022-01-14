from src.data.entities import Project
from src.data.project_repository import create_project


def get_projects_service():
    return 'got'

def get_project_by_id_service():
    return 'got by id'

def post_project_service(project_to_create: dict):
    
    project: Project
    project = create_project(project_to_create)
    
    project = project.to_dict()
    
    return project

def put_project_service():
    return 'updated'

def delete_project_service():
    return 'deleted'