def ingreso_de_notas():
    while True:
        ingreso = input("Ingrese nota de estudiante: ")
        if ingreso.lower() == "fin":
            return None
        try:
            nota = float(ingreso)
            if 0.0 <= nota <= 5.0:
                return nota  
            else:
                print("Ingrese notas dentro del rango de 0.0 y 5.0")
        except ValueError:
            print("Ingrese un número válido por favor")
def nota_final(lista):
    if not lista:
        return 0.0
    return sum(lista) / len(lista)

def evaluar_estado(promedio):
    if promedio >= 3.0:
        return "aprobado"
    else:
        return "reprobado. Activación de sistema de seguimiento y recuperación"
print("Sistema de notas. Escriba 'fin' para recibir su resultado.")
mis_notas = []
while True:
    nota_registrada = ingreso_de_notas()
    if nota_registrada is None:
        break
    mis_notas.append(nota_registrada)
print("Notas registradas:", mis_notas)
if mis_notas:
    promedio = nota_final(mis_notas)
    print("El promedio es:", promedio)
    print("Total de notas ingresadas:", len(mis_notas))
    print("La nota más alta fue:", max(mis_notas))
    
    estado = evaluar_estado(promedio)
    print("Estado del estudiante:", estado)
else:
    print("No se ingresaron notas.")

 
