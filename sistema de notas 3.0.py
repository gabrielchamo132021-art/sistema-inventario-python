estudiante = {"nombre": "ernesto", "codigo": 1, "notas": []}
def XY():
    while True:
        X = input("ingrese nota de estudiante: ")
        if X.lower() == "fin":
            return None
        try:
            Y = float(X)
            if Y >= 0.0 and Y <= 5.0:
                return Y
            else:
                print("ingrese notas dentro del campo de 0.0 y 5.0")
        except ValueError:
            print("ingrese un numero valido por favor")
def Z(lista):
    if not lista:
        return 0.0
    return sum(lista)/ len(lista)
def v (promedio):
    if promedio > 3.0 or promedio == 3.0:
        return "aprobado"
    else:
        return "reprobado. activacion de sistema de seguimiento y recuperacion"
print("sistema de notas. escriba fin o variaciones para recibir su resultado")
mis_notas= []
while True:
    nota_registrada = XY()
    if nota_registrada is None:
        break
    estudiante["notas"].append(nota_registrada)
    print("Notas actuales:", estudiante["notas"])
if estudiante["notas"]:
    promedio = Z(estudiante["notas"])
    print("\n--- RESULTADOS FINALES ---")
    print("El promedio es:", promedio)
    print("Total de notas ingresadas:", len(estudiante["notas"]))
    print("La nota más alta fue:", max(estudiante["notas"]))
    estado = v(promedio)
    print("Estado del estudiante:", estado)
else:
    print("No se registraron notas.")
