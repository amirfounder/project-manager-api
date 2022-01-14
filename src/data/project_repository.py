from src.data.entities import Project
from src.data.core import build_session


def create_project(project_to_create: dict):
    
    project = Project()
    project.name = project_to_create.get('name')

    session = build_session()
    session.add(project)
    session.commit()

    return project