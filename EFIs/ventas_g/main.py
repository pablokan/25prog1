# main.py

from clases import Tienda
from funciones import (
    mostrar_menu,
    inicializar_inventario,
    mostrar_inventario,
    mostrar_ventas
)

def ejecutar_venta(tienda):
    """Función para gestionar la entrada de datos de una venta."""
    print("\n--- NUEVA VENTA ---")
    mostrar_inventario(tienda)

    nombre = input("Ingrese el nombre del producto a vender: ").strip()

    try:
        cantidad_str = input("Ingrese la cantidad en Kilogramos (ej: 0.500): ").strip().replace(',', '.')
        cantidad = float(cantidad_str)
        if cantidad <= 0:
            print("❌ La cantidad debe ser positiva.")
            return
    except ValueError:
        print("❌ Entrada inválida. Por favor, ingrese un número para la cantidad.")
        return

    # Llamada al método de la clase Tienda
    tienda.realizar_venta(nombre, cantidad)

def main():
    """Función principal de la aplicación."""
    # 1. Instanciación de la clase principal
    mi_tienda = Tienda()

    # 2. Cargar datos iniciales
    inicializar_inventario(mi_tienda)

    # 3. Bucle principal de la aplicación
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_inventario(mi_tienda)

        elif opcion == '2':
            ejecutar_venta(mi_tienda)

        elif opcion == '3':
            mostrar_ventas(mi_tienda)

        elif opcion == '4':
            print("\n👋 ¡Gracias por usar la aplicación de Almacén! ¡Hasta pronto!")
            break

        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()