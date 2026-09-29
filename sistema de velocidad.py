velocidad= 0
suma_velocidad= 0.0
total = 0
excesos = 0
velocidad_maxima = 0  
print ("sistema de velocidades")
while True:
        entrada = input("ingrese velocidad:")
        
        if entrada == "fin":
            break 
        try:
            velocidad = float(entrada)
            if velocidad >=0.00:
                suma_velocidad += velocidad
                total += 1
            if velocidad > velocidad_maxima:
                velocidad_maxima = velocidad
            if velocidad> 30:
                excesos += 1
            else:
                print ("solo numeros positivos porfavor")
        except ValueError:
            print (" porfavor ingrese un numero valido" )
if total > 0:
    promedio =  suma_velocidad / total
    print(f"Total de velocidad ingresadas: {total}")
    print(f"El promedio final es: {promedio:.2f}")
    print(f"Velocidad máxima registrada: {velocidad_maxima} m/s")
    print(f"Lecturas que superaron los 30 m/s: {excesos}")
else:
    print("No se ingresó ninguna nota válida.")
