from data.conexion import Session
from modelo.comuna import Comuna
from sqlalchemy import func

sesion = Session()

listado_comunas = sesion.query(Comuna).all()
for comuna in listado_comunas:
    print(comuna)
