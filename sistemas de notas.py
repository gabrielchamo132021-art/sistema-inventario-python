notas = []
aprobados = 0
desaprobados = 0
print("sistemas de notas")
while True:
    try:
        entrada = input("ingrese las notas( o un numero negativo para salir) ").replace(",", ".")
        nota = float(entrada)
    except ValueError:
        print (" porfavor ingrese un numero valido" )
        continue
    if nota < 0.0:
        break
    if nota > 5.0:
        print ("Nota inválida. Debe ser entre 0.0 y 5.0")
        continue
    notas.append(nota)
    if nota >= 3.0:
        print("nota aprovada")
        aprobados += 1
    else:
        print("nota repropada")
        desaprobados += 1
print("\n--- Resumen Final ---")
if len(notas) > 0:
    print(f"Total notas ingresadas: {len(notas)}")
    print(f"Notas aprobadas: {aprobados}")
    print(f"Notas reprobadas: {desaprobados}")
    print(f"Promedio general: {sum(notas) / len(notas):.2f}")
    print(f"Nota más alta: {max(notas)}")
    print(f"Nota más baja: {min(notas)}")
else:
    print("No se ingresaron calificaciones.")

