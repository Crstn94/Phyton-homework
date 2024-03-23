producto = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        id = (input('Introduce ID del producto: '))
        nombre = input('Introduce el nombre del producto: ')
        descripcion = input('Introduce la descripcion del producto: ')
        cantidad = int(input('Introduce la cantidad: '))
        precio = float(input('Introduce el precio del producto: '))
        producto[id] = {'nombre': nombre, 'descripcion': descripcion, 'cantidad': cantidad, 'precio': precio}
        print('Producto agregado exitosamente.')
    elif opcion == '2':
        id = input('Introduce ID del producto a eliminar: ')
        if id in producto:
            del producto[id]
            print('Producto eliminado exitosamente.')
        else:
            print('No existe el producto con el ID', id)
    elif opcion == '3':
        id = input('Introduce ID del producto a buscar: ')
        if id in producto:
            print('Detalles del producto con ID', id)
            for clave, valor in producto[id].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el producto con el ID', id)
    elif opcion == '4':
        print('Lista de productos')
        for id, detalles in producto.items():
            print('ID:', id)
            for clave, valor in detalles.items():
                print(clave.title() + ':', valor)
            print()  
    elif opcion == '5':
        id = input('Introduce ID del producto a editar: ')
        if id in producto:
            print('Editando producto con ID', id)
            print('¿Qué campo deseas editar?')
            print('(1) Nombre')
            print('(2) Descripción')
            print('(3) Cantidad')
            print('(4) Precio')
            campo = input('Elige una opción: ')
            if campo in ('1', '2', '3', '4'):
                nuevo_valor = input('Introduce el nuevo valor: ')
                if campo == '3' or campo == '4':
                    nuevo_valor = int(nuevo_valor) if campo == '3' else float(nuevo_valor)
                producto[id]['nombre'] = nuevo_valor if campo == '1' else producto[id]['nombre']
                producto[id]['descripcion'] = nuevo_valor if campo == '2' else producto[id]['descripcion']
                producto[id]['cantidad'] = nuevo_valor if campo == '3' else producto[id]['cantidad']
                producto[id]['precio'] = nuevo_valor if campo == '4' else producto[id]['precio']
                print('Producto editado exitosamente.')
            else:
                print('Opción no válida.')
        else:
            print('No existe el producto con el ID', id)
    opcion = input('Menú de opciones\n(1) Añadir producto\n(2) Eliminar producto\n(3) Buscar producto\n(4) Listar productos\n(5) Editar producto\n(6) Terminar\nElige una opción: ')

