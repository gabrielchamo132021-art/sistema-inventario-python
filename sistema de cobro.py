import json
import os

archivo_json = "datos.json"

def ingreso_datos():
    """Carga los datos desde el archivo JSON del disco duro."""
    if os.path.exists(archivo_json):
        try:
            with open(archivo_json, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            print("[ALERTA] El archivo JSON está corrupto. Iniciando con datos vacíos")
            return {}
    else:
        return {
            "p001": { 
                "nombre": "ramiro",
                "estado": "pendiente de pago",
                "capital": 5000000,
                "pago": 100000,
                "dia de pago": "20 de cada mes" 
            },
            "p002": { 
                "nombre": "enrique",
                "estado": "pendiente de pago",
                "capital": 40000000,
                "pago": 500000,
                "dia de pago": "19 de cada mes" 
            }
        }

def guardar_datos(datos, ruta_archivo):
    """Guarda el diccionario actual en el archivo JSON del disco duro."""
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def mostrar_datos(datos):
    """Muestra todos los registros de los deudores en forma de tabla."""
    if not datos:
        print("\n[INFO] El registro está vacío.")
        return

    print("\n" + "="*70)
    print(f"{'SKU':<8} | {'NOMBRE':<15} | {'ESTADO':<18} | {'PAGO':<10}")
    print("="*70)
    for sku, info in datos.items():
        print(f"{sku:<8} | {info['nombre']:<15} | {info['estado']:<18} | ${info['pago']:<9}")
    print("="*70)

def menu():
    """Controlador principal del sistema y menú interactivo."""
    datos = ingreso_datos()
    while True:
        print("\n=== SISTEMA DE COBRO ===")
        print("1. Ver deudores")
        print("2. Salir")
        
        opcion = input("Seleccione una opción (1-2): ").strip()

        if opcion == "1":
            mostrar_datos(datos)
        elif opcion == "2":
            print("\nSaliendo del sistema...")
            break
        else:
            print("[ERROR] Opción no válida.")

if __name__ == "__main__":
    menu()  
        
