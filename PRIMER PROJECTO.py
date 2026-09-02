
producto_nombre = "Ninguno"
producto_precio = 0
while True:
    print ("menu de opciones")
    print("1. ver producto")
    print ("2. Guardar nuevo producto")
    print ("3. Salir")
    print("4. Aplicar descuento")
    opcion = input("Elige una opción (1 , 2 , 3 o 4): ")
    if opcion == "1":
        print("\nProducto actual:", producto_nombre)
        print("Precio: $", producto_precio)
    elif opcion == "2":
        producto_nombre = input("Ingresa el nombre del producto: ")
        producto_precio = input("Ingresa el precio: ")
        print("¡Producto guardado con éxito!")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    elif opcion == "4":
        precio_num = float(producto_precio)
        if precio_num > 0:
            monto_descuento = float(input("¿cuanto dinero desea descontar?"))
            if monto_descuento <= precio_num:
                precio_num = precio_num - monto_descuento
                producto_precio = precio_num
                print(f"¡Se aplicó un descuento de ${monto_descuento}!")
            else:
                print(f"el descuento no puede sser mayor que el precio actual" )
        else:
            print(" no hay un precio valido para aplicar descuento ")
    else:
        print("Opción no válida, intenta de nuevo.")
   
    
        
