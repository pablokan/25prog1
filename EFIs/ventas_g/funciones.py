# funciones.py

def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n" + "="*30)
    print("      🧀 Almacén POO 🥓")
    print("="*30)
    print("1. Mostrar Inventario/Stock")
    print("2. Realizar Venta")
    print("3. Mostrar Registro de Ventas")
    print("4. Salir")
    print("="*30)

def inicializar_inventario(tienda):
    """Crea los productos iniciales y los agrega a la tienda."""
    from clases import Queso, Fiambre

    # Creación de objetos con HERENCIA
    queso_tybo = Queso("Queso Tybo", 8.50, 15.0, "Media") # $8.50/kg
    jamon_crudo = Fiambre("Jamón Crudo", 18.00, 8.5, "España") # $18.00/kg
    salamin = Fiambre("Salame Milan", 12.75, 10.0, "Local") # $12.75/kg
    queso_parm = Queso("Queso Parmesano", 9.90, 7.2, "Larga") # $9.90/kg

    tienda.agregar_producto(queso_tybo)
    tienda.agregar_producto(jamon_crudo)
    tienda.agregar_producto(salamin)
    tienda.agregar_producto(queso_parm)

    print("Inventario inicial cargado con éxito. ¡Bienvenido!")

def mostrar_inventario(tienda):
    """Muestra el estado actual del stock y precios."""
    print("\n--- INVENTARIO Y STOCK ACTUAL ---")
    if not tienda.inventario:
        print("El inventario está vacío.")
        return

    print(f"{'Nombre':<20} | {'Precio/Kg (USD)':<15} | {'Stock (Kg)':<10} | {'Info Extra':<15}")
    print("-" * 65)
    for producto in tienda.inventario.values():
        info = producto.obtener_info()
        extra = info.get('maduracion', info.get('origen', 'N/A'))
        print(f"{info['nombre']:<20} | $ {info['precio_por_kg']:<13.2f} | {info['stock_kg']:<10.2f} | {extra:<15}")

def mostrar_ventas(tienda):
    """Muestra el historial de ventas registradas."""
    print("\n--- REGISTRO DE VENTAS ---")
    if not tienda.registro_ventas:
        print("Aún no se ha realizado ninguna venta.")
        return

    total_acumulado = 0
    print(f"{'Producto':<20} | {'Kg Vendidos':<13} | {'Precio/Kg':<10} | {'Total (USD)':<12}")
    print("-" * 60)
    for i, venta in enumerate(tienda.registro_ventas, 1):
        detalle = venta.obtener_detalle()
        total_acumulado += venta.monto_total
        print(f"{i}. {detalle['producto']:<17} | {detalle['cantidad_kg']:<13.2f} | {detalle['precio_kg']:<10} | {detalle['total']:<12}")

    print("-" * 60)
    print(f"{'TOTAL ACUMULADO':<45} | $ {total_acumulado:<10.2f}")