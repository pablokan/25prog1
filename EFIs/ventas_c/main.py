from clases import Queso, Fiambre
from funciones import registrar_venta

def main():
    # Stock inicial
    productos = [
        Queso("Gouda", 2500, 10, "media maduración"),
        Queso("Brie", 3200, 5, "suave"),
        Fiambre("Jamón Cocido", 1800, 8, "fino"),
        Fiambre("Salame", 2200, 12, "grueso")
    ]

    ventas = []

    while True:
        print("\n=== TIENDA DE ALMACÉN ===")
        print("1. Registrar venta")
        print("2. Ver ventas realizadas")
        print("3. Salir")

        opcion = input("Elija opción: ")

        if opcion == "1":
            venta = registrar_venta(productos)
            if venta:
                ventas.append(venta)
                print("\nVenta registrada con éxito:")
                print(venta)
        elif opcion == "2":
            if ventas:
                print("\n--- HISTORIAL DE VENTAS ---")
                for v in ventas:
                    print(v, "\n")
            else:
                print("No hay ventas registradas.")
        elif opcion == "3":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
