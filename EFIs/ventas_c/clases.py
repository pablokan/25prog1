from datetime import datetime

class Producto:
    """Clase base para un producto de almacén"""
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"


# Herencia: Queso y Fiambre son tipos de Producto
class Queso(Producto):
    def __init__(self, nombre, precio, stock, maduracion):
        super().__init__(nombre, precio, stock)
        self.maduracion = maduracion

    def __str__(self):
        return f"Queso {self.nombre} ({self.maduracion}) - ${self.precio:.2f} (Stock: {self.stock})"


class Fiambre(Producto):
    def __init__(self, nombre, precio, stock, tipo_corte):
        super().__init__(nombre, precio, stock)
        self.tipo_corte = tipo_corte

    def __str__(self):
        return f"Fiambre {self.nombre} (Corte: {self.tipo_corte}) - ${self.precio:.2f} (Stock: {self.stock})"


# Composición: una venta tiene productos
class Venta:
    def __init__(self):
        self.items = []
        self.fecha = datetime.now()

    def agregar_item(self, producto, cantidad):
        if producto.reducir_stock(cantidad):
            subtotal = producto.precio * cantidad
            self.items.append((producto.nombre, cantidad, subtotal))
            return True
        return False

    def total(self):
        return sum(sub for _, _, sub in self.items)

    def __str__(self):
        detalle = "\n".join([f"{n} x{c} = ${s:.2f}" for n, c, s in self.items])
        return f"Venta del {self.fecha.strftime('%d/%m/%Y %H:%M')}\n{detalle}\nTOTAL: ${self.total():.2f}"
