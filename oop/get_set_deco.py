class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        """Getter para el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        """Setter para el precio del producto con validación."""
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print("El precio no puede ser negativo.")

mi_producto = Producto("Laptop", 1200)
print(mi_producto.precio) # Parece un atributo, pero llama al getter
mi_producto.precio = -100 # Parece una asignación directa, pero llama al setter con validación
print(mi_producto.precio)