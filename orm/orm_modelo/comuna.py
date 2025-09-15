from sqlalchemy import Column, Integer, String
from orm_modelo.base import BaseModel


class Comuna(BaseModel):
    id_comuna = Column(Integer, primary_key=True)
    codigo_comuna = Column(String(5))
    nombre_comuna = Column(String(50))
