from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from modelo.nacionalidad import Nacionalidad

Base = declarative_base()


class Autor(Base):
    __tablename__ = 'autor'
    id_autor = Column(Integer, primary_key=True)
    nombre_autor = Column(String(100))
    pseudonimo = Column(String(100))
    habilitado = Column(Boolean)
    id_nacionalidad = Column(Integer, ForeignKey(
        Nacionalidad.id_nacionalidad))  # type: ignore
