from orm_data.conexion import Session
from orm_modelo.direccion import Direccion
from sqlalchemy import func
from orm_negocio.negocio_comuna import buscar_comuna

from prettytable import PrettyTable

sesion = Session()


def listado_direcciones():
    listado_direcciones = sesion.query(Direccion).all()
    tabla_direcciones = PrettyTable()
    tabla_direcciones.field_names = [
        'Id', 'Calle', 'Número', 'Departamento', 'Comuna']
    for direccion in listado_direcciones:
        tabla_direcciones.add_row(
            [direccion.id_direccion, direccion.calle, direccion.numero, direccion.departamento, direccion.id_comuna])
    print(tabla_direcciones)


def guardar_direccion():
    direccion = Direccion()
    direccion.calle = input('Calle: ')  # type: ignore
    direccion.numero = input('Número: ')  # type: ignore
    direccion.departamento = input('Departamento: ')  # type: ignore

    buscar_comuna_direccion = input('Nombre Comuna: ')
    comuna = buscar_comuna(buscar_comuna_direccion)
    if comuna:
        direccion.id_comuna = comuna.id_comuna
    else:
        print('Comuna NO encontrada...')

    sesion.add(direccion)
    try:
        sesion.commit()
        mensaje = 'Su dirección se ha agregado con éxito!'
    except Exception as error:
        sesion.rollback()
        mensaje = f'Error al guardar su dirección: {error}'
    finally:
        sesion.close()
    return mensaje
