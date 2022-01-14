from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.orm import registry
from sqlalchemy.orm.session import sessionmaker, Session as TSession

from src.utils.constants import POSTGRESQL_CONNECTION_STRING

engine: Engine
engine = create_engine(POSTGRESQL_CONNECTION_STRING, echo=False)


Session: TSession
Session = sessionmaker(bind=engine)

mapper_registry = registry()

Base = mapper_registry.generate_base()


def setup_schema():
    mapper_registry.metadata.create_all(engine)


def build_session() -> TSession:
    session: TSession
    session = Session()
    session.expire_on_commit = False
    return session
