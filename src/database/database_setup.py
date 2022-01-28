from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.orm import registry
from sqlalchemy.orm.session import sessionmaker, Session as TSession
from sqlalchemy import Column as TColumn

from src.utils.constants import POSTGRESQL_CONNECTION_STRING

engine: Engine
engine = create_engine(POSTGRESQL_CONNECTION_STRING, echo=False)


Session: TSession
Session = sessionmaker(bind=engine)

mapper_registry = registry()

Base = mapper_registry.generate_base()


def setup_schema():
    mapper_registry.metadata.create_all(engine)
    sync_tables()


def build_session() -> TSession:
    session: TSession
    session = Session()
    session.expire_on_commit = False
    return session


def sync_tables():
    tables_dict = mapper_registry.metadata.tables
    table_names = tables_dict.keys()
    tables = [tables_dict[x] for x in table_names]

    for table in tables:
        sync_table(table)


def sync_table(table):
    session = build_session()
    tablename = table.name

    columns_query = \
        f'SELECT column_name, data_type ' \
        'FROM information_schema.columns ' \
        f'WHERE table_name = \'{tablename}\' \
        AND table_schema = \'public\''

    db_columns = session.execute(columns_query).all()
    db_column_names = [x[0] for x in db_columns]

    model_columns: list[TColumn]
    model_columns = list(table.columns)
    model_column_names = [x.key for x in model_columns]

    model_columns_length = len(model_columns)
    db_columns_length = len(db_columns)

    if model_columns_length == db_columns_length:
        return

    alter_query = 'ALTER TABLE {} '.format(tablename)
    column_statements = []

    if model_columns_length > db_columns_length:

        different_columns = [x for x in model_columns if x.key not in db_column_names]
        for column in different_columns:

            name = column.key
            datatype = column.type
            datatype_name = datatype.compile()

            '''
            PGSQL 'datetime' does not exist.
            Using 'timestamp' instead
            '''
            if datatype_name == 'DATETIME':
                with_timezone = datatype.timezone
                keyword = 'with' if with_timezone else 'without'
                datatype_name = 'TIMESTAMP {} time zone'.format(keyword)

            column_statements.append(
                'ADD COLUMN "{}" {}'.format(name, datatype_name))

    if db_columns_length > model_columns_length:

        diffs = [x for x in db_columns if x[0] not in model_column_names]
        for diff in diffs:

            name, _ = diff
            column_statements.append('DROP COLUMN {}'.format(name))

    alter_query += ', '.join(column_statements)

    session.execute(alter_query)
    session.commit()
