# Inicializacion del inventario
Inventario = {
    'Manzanas': {'cantidad': 50, 'precio': 1.50},
    'Leche': {'cantidad': 20, 'precio': 2.75},
    'Pan': {'cantidad': 10, 'precio': 3.00}}
while True:
    print("\n--- Menu de Gestion de Inventarios ---")
    print("1. Añadir Producto")
    print("2. Actualizar Stock")
    print("3. Eliminar Producto")
    print("4. Ver Inventario")
    print("5. Buscar Producto")
    print("6. Resumen de Inventario")
    print("7. Salir")
    print("---------------------------------------")
    opcion = input("Seleccione una opcion: ")
    if opcion == '1':
        print("\n--- Añadir Nuevo Producto ---")
        NombreProducto = input("ingrese el nombre del producto: "
                               ).strip().capitalize()
        if NombreProducto in Inventario:
            print(f"Error: El producto '{NombreProducto}' ya existe en"
                  " el inventario.")
        else:
            print(f"Nombre '{NombreProducto}' disponible")
        # Solicitud de producto.
            while True:
                try:
                    Cantidad = int(input("Ingrese la cantidad inicial: "))
                    if Cantidad < 0:
                        print("La cantidad no puede ser negativa, intente"
                              " nuevamente.")
                    else:
                        break
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero "
                          "entero.")
        # Solicitud de precio.
            while True:
                try:
                    Precio = float(input("Ingrese el precio unitario: "))
                    if Precio < 0:
                        print("El precio no puede ser negativo. Intente de"
                              " nuevo.")
                    else:
                        break
                except ValueError:
                    print("Entrada invalida. Por favor ingrese un numero para"
                          " el precio.")
        # Almacenamiento de producto
            Inventario[NombreProducto] = {'cantidad': Cantidad,
                                          'precio': Precio}
            print(f"Producto '{NombreProducto}' añadido exitosamente.")
    elif opcion == '2':
        print("\n--- Actualizar Stock de Producto ---")
        NombreAActualizar = input("Ingrese el nombre del producto"
                                  "a actualizar: ").strip().capitalize()
        if NombreAActualizar not in Inventario:
            print(f"Error: El producto '{NombreAActualizar}' no se encuentra"
                  " en el inventario.")
        else:
            print(f"Producto '{NombreAActualizar}' encontrado. Cantidad"
                  f" actual: {Inventario[NombreAActualizar]['cantidad']}.")
        # Ingresar nueva cantidad
            while True:
                try:
                    NuevaCantidad = int(input("Ingrese la nueva cantidad "
                                              f"para '{NombreAActualizar}': "))
                    if NuevaCantidad < 0:
                        print("La cantidad no puede ser negativa. "
                              "Intente de nuevo.")
                    else:
                        break
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero"
                          " entero para la cantidad.")
        # Actualizar cantidad
            Inventario[NombreAActualizar]['cantidad'] = NuevaCantidad
            print(f"Stock de '{NombreAActualizar}' actualizado"
                  f" a {NuevaCantidad}.")
    elif opcion == '3':
        print("\n--- Logica para Eliminar el Producto ---")
        NombreAEliminar = input("Ingrese el nombre del producto"
                                " a eliminar: ").strip().capitalize()
        if NombreAEliminar not in Inventario:
            print(f"Error: El producto '{NombreAEliminar}' no se encuentra en"
                  " el inventario.")
        else:
            print(f"Producto '{NombreAEliminar}' encontrado.")
            # Confirmacion de eliminacion
            Confirmacion = input("¿Esta seguro de que desea eliminar"
                                 f" '{NombreAEliminar}' del inventario?"
                                 " (s/n): ").lower()
            if Confirmacion == 's':
                del Inventario[NombreAEliminar]
                print(f"Producto '{NombreAEliminar}' eliminado exitosamente.")
            else:
                print("Eliminacion cancelada.")
    elif opcion == '4':
        print("\n--- Ver Inventario ---")
        if not Inventario:
            print("El inventario esta vacio.")
        else:
            print("\n--- Inventario Actual ---")
            for nombre, detalles in Inventario.items():
                print(f"Nombre: {nombre}, Cantidad: {detalles['cantidad']},"
                      f" Precio: ${detalles['precio']:.2f}")
                print("--------------------------------\n")
    elif opcion == '5':
        print("\n--- Buscar Producto ---")
        TerminoBusqueda = input("Ingrese el nombre o parte del nombre del"
                                " producto a buscar: ").strip().lower()
        ProductosEncontrados = []
        for nombre, detalles in Inventario.items():
            if TerminoBusqueda in nombre.lower():
                ProductosEncontrados.append((nombre, detalles))
        if ProductosEncontrados:
            print("\n--- Resultados de la Busqueda ---")
            for nombre, detalles in ProductosEncontrados:
                print(f"Nombre: {nombre}, Cantidad: {detalles['cantidad']}, "
                      f"Precio: ${detalles['precio']:.2f}")
                print("--------------------------------\n")
        else:
            print("No se encontraron productos que coincidan "
                  f"con '{TerminoBusqueda}'")
    elif opcion == '6':
        print("\n--- Resumen de Inventario ---")
        # Valor total del inventario
        ValorTotalInventario = 0
        for detalles in Inventario.values():
            ValorTotalInventario += detalles['cantidad'] * detalles['precio']
        print(f"Valor Total del inventario: ${ValorTotalInventario:.2f}")
        # Productos con bajo stock
        UmbralBajoStock = 5
        ProductosBajoStock = []
        for nombre, detalles in Inventario.items():
            if detalles['cantidad'] < UmbralBajoStock:
                ProductosBajoStock.append(nombre)
        if ProductosBajoStock:
            print("Productos con bajo stock"
                  " (cantidad < {}): ".format(UmbralBajoStock))
            for p in ProductosBajoStock:
                print(f"- {p} (Cantidad: {Inventario[p]['cantidad']})")
        else:
            print("No hay productos con bajo stock.")
        # Uso de any() y all()
        AlgunProductoAgotado = any(detalles['cantidad'] == 0 for detalles in
                                   Inventario.values())
        if AlgunProductoAgotado:
            print("Advertencia! Hay al menos un producto agotado en "
                  "el inventario.")
        else:
            print("No hay productos agotados en el inventario (o "
                  "el inventario esta vacio.)")
    elif opcion == '7':
        print("Saliendo del programa. Hasta pronto!")
        break
    else:
        print("Opcion invalida. Por favor, intente de nuevo.")
