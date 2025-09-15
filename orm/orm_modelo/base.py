from sqlalchemy.orm import declarative_base, declared_attr
from sqlalchemy.sql import func
from typing import Type, Any


class BaseClass:
    __abstract__ = True
    __name__: str

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


Base: Type[Any] = declarative_base(cls=BaseClass)


class BaseModel(Base):
    __abstract__ = True
