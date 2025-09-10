from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Nacionalidad(Base):
    __tablename__ = 'comuna'
    id_nacionalidad = Column(Integer, primary_key=True)
    pais = Column(String(50))
    nacionalidad = Column(String(50))
