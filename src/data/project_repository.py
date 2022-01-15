from src.data.entities import Project
from src.data.core import build_session


def create_project(project_to_create: dict):
    project = Project()
    project.from_dict(project_to_create)

    session = build_session()
    session.add(project)
    session.commit()

    return project


def delete_project(project_id: int):
    pass


def update_project(project_to_update: dict, id: int):
    pass


def select_projects():
    session = build_session()

    projects: dict[Project]
    projects = session.query(Project).all()

    return projects


def select_project_by_id(id: int):
    session = build_session()
    
    project = session.query(Project).get(id)
    
    return project