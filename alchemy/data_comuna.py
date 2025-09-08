from data.conexion import Session
from modelo.comuna import Comuna
from sqlalchemy import func

from prettytable import PrettyTable

sesion = Session()

# Instancia de clase
nueva_comuna = Comuna()

# nueva_comuna.id_comuna = 15
nueva_comuna.codigo_comuna = input('Ingrese código de comuna: ')
nueva_comuna.nombre_comuna = input('Ingrese nombre de comuna: ')

sesion.add(nueva_comuna)
try:
    sesion.commit()
    print('Su comuna se ha agregado con éxito!')
except Exception as error:
    sesion.rollback()
    print('Error al guardar su comiuna: {error}')
finally:
    sesion.close()

listado_comunas = sesion.query(Comuna).all()
table = PrettyTable()
table.field_names = ["Id", "Código Comuna", "Nombre Comuna"]

# comuna_busqueda = input('Ingrese comuna a buscar: ')
# comuna = sesion.query(Comuna).filter_by(nombre_comuna=comuna_busqueda).first()
# print(type(comuna))
# if comuna:
#     table.add_row(
#         [comuna.id_comuna, comuna.codigo_comuna, comuna.nombre_comuna])

for comuna in listado_comunas:
    table.add_row(
        [comuna.id_comuna, comuna.codigo_comuna, comuna.nombre_comuna])

print(table)
