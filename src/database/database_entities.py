from datetime import datetime
from sqlalchemy import Column as TableColumn, Integer, String, BigInteger, DateTime, Table, ForeignKey
from src.database.database_setup import Base


class EntityBase(object):
    id = TableColumn(BigInteger, primary_key=True)
    created_at = TableColumn(DateTime(True))
    updated_at = TableColumn(DateTime(True))

    def __init__(self) -> None:
        super().__init__()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @classmethod
    def get_column_names(cls):
        columns: list[TableColumn]
        columns = cls.get_columns()

        column_names: list[str]
        column_names = [x.name for x in columns]

        return column_names

    @classmethod
    def get_columns(cls: type[Base]):
        table: Table
        table = cls.__getattribute__(cls, '__table__')

        if table is None:
            return []

        columns: list[TableColumn]
        columns = table.columns

        return columns

    def to_dict(self):
        result: dict
        result = {}

        columns: list[TableColumn]
        columns = self.get_columns()

        for column in columns:
            name = column.name
            value = self.__getattribute__(name)
            result[name] = value

        return result

    def from_dict(self, obj: dict):
        for key, value in obj.items():
            if hasattr(self, key):
                setattr(self, key, value)

        return self


class Project(EntityBase, Base):
    __tablename__ = 'projects'

    tag = TableColumn(String)
    name = TableColumn(String)
    description = TableColumn(String)


class Column(EntityBase, Base):
    __tablename__ = 'columns'

    project_id = TableColumn(BigInteger, ForeignKey(Project.id))
    name = TableColumn(String)
    order = TableColumn(Integer)


class Card(EntityBase, Base):
    __tablename__ = 'cards'

    project_id = TableColumn(BigInteger, ForeignKey(Project.id))
    column_id = TableColumn(BigInteger, ForeignKey(Column.id))
    order = TableColumn(Integer)
    name = TableColumn(String)
    description = TableColumn(String)
