# clases.py

class Producto:
    """Clase base para todos los productos de la tienda."""
    def __init__(self, nombre, precio_por_kg, stock_inicial_kg):
        self.nombre = nombre
        self.precio_por_kg = precio_por_kg
        self.stock_kg = stock_inicial_kg

    def obtener_info(self):
        """Devuelve un diccionario con la información del producto."""
        return {
            "nombre": self.nombre,
            "precio_por_kg": self.precio_por_kg,
            "stock_kg": self.stock_kg
        }

    def actualizar_stock(self, cantidad_kg):
        """Resta la cantidad vendida al stock. Devuelve True si es exitoso, False si no hay suficiente stock."""
        if self.stock_kg >= cantidad_kg:
            self.stock_kg -= cantidad_kg
            return True
        return False

# HERENCIA: Queso y Fiambre heredan de Producto
class Queso(Producto):
    """Producto específico: Queso, con atributo adicional de maduración."""
    def __init__(self, nombre, precio_por_kg, stock_inicial_kg, maduracion):
        super().__init__(nombre, precio_por_kg, stock_inicial_kg)
        self.maduracion = maduracion

    def obtener_info(self):
        """Sobrescribe el método para incluir la maduración."""
        info = super().obtener_info()
        info['maduracion'] = self.maduracion
        return info

class Fiambre(Producto):
    """Producto específico: Fiambre, con atributo adicional de origen."""
    def __init__(self, nombre, precio_por_kg, stock_inicial_kg, origen):
        super().__init__(nombre, precio_por_kg, stock_inicial_kg)
        self.origen = origen

    def obtener_info(self):
        """Sobrescribe el método para incluir el origen."""
        info = super().obtener_info()
        info['origen'] = self.origen
        return info

class Venta:
    """Representa una única venta (Composición con Producto)."""
    def __init__(self, producto, cantidad_kg):
        self.producto = producto  # COMPOSICIÓN: Venta "tiene un" Producto
        self.cantidad_kg = cantidad_kg
        self.precio_unitario = producto.precio_por_kg
        self.monto_total = self.cantidad_kg * self.precio_unitario

    def obtener_detalle(self):
        """Devuelve el detalle de la venta."""
        return {
            "producto": self.producto.nombre,
            "cantidad_kg": self.cantidad_kg,
            "precio_kg": f"$ {self.precio_unitario:.2f}",
            "total": f"$ {self.monto_total:.2f}"
        }

class Tienda:
    """Clase principal que gestiona el inventario y las ventas."""
    def __init__(self):
        self.inventario = {} # Diccionario: {nombre_producto: objeto_producto}
        self.registro_ventas = []

    def agregar_producto(self, producto):
        """Agrega un producto al inventario."""
        self.inventario[producto.nombre] = producto

    def realizar_venta(self, nombre_producto, cantidad_kg):
        """Procesa la venta y registra el movimiento."""
        if nombre_producto not in self.inventario:
            print(f"❌ Error: El producto '{nombre_producto}' no existe.")
            return False

        producto = self.inventario[nombre_producto]

        # Intentar actualizar el stock
        if producto.actualizar_stock(cantidad_kg):
            # Si se pudo, crear y registrar la venta
            venta = Venta(producto, cantidad_kg)
            self.registro_ventas.append(venta)
            print(f"✅ Venta exitosa: {cantidad_kg:.2f} kg de {nombre_producto}. Total: {venta.obtener_detalle()['total']}")
            return True
        else:
            print(f"⚠️ Stock insuficiente. Solo quedan {producto.stock_kg:.2f} kg de {nombre_producto}.")
            return False