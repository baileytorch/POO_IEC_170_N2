from orm_negocio.negocio_comuna import listado_comunas, crear_comuna, actualizar_comuna
from orm_negocio.negocio_direccion import listado_direcciones, guardar_direccion


def menu_principal():
    print('Menú Aplicación Biblioteca')
    print('==========================')
    print('[1] Listado Comunas')
    print('[2] Listado Direcciones')
    print('[3] Agregar Dirección')
    print('[0] Salir')

    while True:
        respuesta = ''
        opcion = input('Ingrese su opción [0-3]')

        if opcion == '1':
            listado_comunas()
        elif opcion == '2':
            listado_direcciones()
        elif opcion == '3':
            respuesta = guardar_direccion()
        elif opcion == '0':
            break
        else:
            print('Opción NO corresponde...')
        print(respuesta)


menu_principal()
