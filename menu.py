

def menu_principal():
    print('Bibliohub')
    print('################\n')
    while True:
        print('[1] Gestion Biblioteca')
        print('[2] Gestion Usuarios')
        print('[3] Gestion Prestamos')
        print('[4] Salir')
        opcion_usuario = input('Seleccione una opción: ')
        if opcion_usuario == '1':
            print('opcion 1')
            break
        elif opcion_usuario == '2':
            print('opcion 2')
            break
        elif opcion_usuario == '3':
            print('opcion 3')
            break
        elif opcion_usuario == '4':
            print('Saliendo...')
            break
        else:
            print('Opción no válida')