from sqlalchemy import Column, Integer, String, ForeignKey
from orm_modelo.base import BaseModel


class Direccion(BaseModel):
    id_direccion = Column(Integer, primary_key=True)
    calle = Column(String(100))
    numero = Column(String(10))
    departamento = Column(String(10))
    id_comuna = Column(Integer, ForeignKey('comuna.id_comuna'))
