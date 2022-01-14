from src.data.entities import Project
from src.data.project_repository import create_project, select_project_by_id, select_projects


def get_projects_service():
    projects: list[Project]
    projects = select_projects()
    projects = [x.to_dict() for x in projects]

    return projects


def get_project_by_id_service(id: int):
    project: Project
    project = select_project_by_id(id)
    project = project.to_dict()
    
    return project


def post_project_service(project_to_create: dict):
    project: Project
    project = create_project(project_to_create)
    project = project.to_dict()

    return project


def put_project_service():
    return 'updated'


def delete_project_service():
    return 'deleted'
