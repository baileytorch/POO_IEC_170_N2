from sqlalchemy import Column, Integer, String
from orm_modelo.base import BaseModel


class Nacionalidad(BaseModel):
    id_nacionalidad = Column(Integer, primary_key=True)
    pais = Column(String(50))
    nacionalidad = Column(String(50))
