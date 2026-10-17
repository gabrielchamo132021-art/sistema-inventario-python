import json
import os

ARCHIVO_DB = "inventario.json"

def cargar_datos():
    """Carga el inventario desde el archivo JSON del disco duro."""
    if os.path.exists(ARCHIVO_DB):
        try:
            with open(ARCHIVO_DB, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            print("[AVISO] El archivo JSON está corrupto. Iniciando con inventario vacío.")
            return {}
    else:
        return {
            "p001": { "nombre": "laptop hp", "categoria": "computacion", "precio": 2500000.0, "precio_venta": 3500000.0, "stock": 5 },
            "p002": { "nombre": "laptop gamer", "categoria": "computacion", "precio": 3500000.0, "precio_venta": 4500000.0, "stock": 19 }
        }

def guardar_base_datos(inventario):
    """Guarda el diccionario actual en el archivo JSON del disco duro."""
    with open(ARCHIVO_DB, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)

def mostrar_inventario(inventario):
    """Muestra todos los productos registrados en forma de tabla."""
    if not inventario:
        print("\n[INFO] El inventario está vacío.")
        return

    print("\n" + "="*50)
    print(f"{'SKU':<8} | {'PRODUCTO':<15} | {'STOCK':<6} | {'PRECIO VENTA':<10}")
    print("="*50)
    for sku, datos in inventario.items():
        print(f"{sku:<8} | {datos['nombre']:<15} | {datos['stock']:<6} | ${datos['precio_venta']:<10,.2f}")
    print("="*50)

def main():
    """Controlador principal del sistema y menú interactivo."""
    inventario = cargar_datos()

    while True:
        print("\n=== SISTEMA DE INVENTARIO COMERCIAL ===")
        print("1. Ver inventario")
        print("2. Salir")

        opcion = input("Seleccione una opción (1-2): ").strip()

        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            print("\nSaliendo del sistema...")
            break
        else:
            print("[ERROR] Opción no válida.")

if __name__ == "__main__":
    main()
