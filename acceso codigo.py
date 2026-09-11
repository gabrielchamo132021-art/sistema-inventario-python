permitidos = 0
denegados = 0
print("sistema de acceso")
while True:
    try:
        edad= int(input("ingrese su edad ( o un numero negativo para salir) "))
    except ValueError:
        print (" porfavor ingrese un numero valido" )
        continue
    if edad <0:
        break
    if edad >=18:
        print ("acceso permitido")
        permitidos += 1
    else:
        print("acceso denegado menor de edad")
        denegados += 1
              
print("\n--- Resumen Final ---")
print(f"Total accesos permitidos: {permitidos}")
print(f"Total accesos denegados: {denegados}")
              
    
