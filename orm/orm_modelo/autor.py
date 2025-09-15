from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from orm_modelo.nacionalidad import Nacionalidad
from orm_modelo.base import BaseModel


class Autor(BaseModel):
    id_autor = Column(Integer, primary_key=True)
    nombre_autor = Column(String(100))
    pseudonimo = Column(String(100))
    habilitado = Column(Boolean)
    id_nacionalidad = Column(Integer, ForeignKey(
        'nacionalidad.id_nacionalidad'))
