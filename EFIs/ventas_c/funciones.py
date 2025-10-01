from clases import Venta

def mostrar_productos(productos):
    print("\n--- LISTA DE PRODUCTOS ---")
    for i, p in enumerate(productos, 1):
        print(f"{i}. {p}")

def registrar_venta(productos):
    venta = Venta()
    while True:
        mostrar_productos(productos)
        opcion = input("\nSeleccione producto (0 para terminar): ")
        if opcion == "0":
            break
        try:
            idx = int(opcion) - 1
            cantidad = int(input("Cantidad: "))
            if productos[idx].stock >= cantidad:
                venta.agregar_item(productos[idx], cantidad)
                print("Producto agregado a la venta.")
            else:
                print("No hay suficiente stock.")
        except (ValueError, IndexError):
            print("Opción inválida.")
    return venta if venta.items else None
