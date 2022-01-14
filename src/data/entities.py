from datetime import datetime
from sqlalchemy import Column, String, BigInteger, DateTime, Table
from src.data.core import Base


class EntityBase(object):
    created_at = Column(DateTime(True))
    updated_at = Column(DateTime(True))

    def __init__(self) -> None:
        super().__init__()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    

    def to_dict(self):
        result: dict
        result = {}

        table: Table
        table = self.__getattribute__('__table__')

        if table is None:
            return {}
        
        columns: list[Column]
        columns = table.columns

        for column in columns:
            name = column.name
            value = self.__getattribute__(name)
            result[name] = value
        
        return result


class Project(EntityBase, Base):
    __tablename__ = 'projects'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)


class Card(EntityBase, Base):
    __tablename__ = 'cards'

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    description = Column(String)