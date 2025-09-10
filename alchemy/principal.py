from negocio.negocio_comuna import listado_comunas, crear_comuna, actualizar_comuna


def menu_principal():
    print('Menú Aplicación Biblioteca')
    print('==========================')
    print('[1] Listado Comunas')
    print('[2] Agregar Comuna')
    print('[3] Editar Comuna')
    print('[0] Salir')

    while True:
        respuesta = ''
        opcion = input('Ingrese su opción [0-3]')

        if opcion == '1':
            listado_comunas()
        elif opcion == '2':
            respuesta = crear_comuna()
        elif opcion == '3':
            respuesta = actualizar_comuna()
        elif opcion == '0':
            break
        else:
            print('Opción NO corresponde...')
        print(respuesta)


menu_principal()
