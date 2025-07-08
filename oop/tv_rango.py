import datetime
from webbrowser import get

class Producto:
    def __init__(self, nombre, año_fabricacion):
        self.nombre = nombre
        self.set_año_fabricacion(año_fabricacion)

    @property

    def get_año_fabricacion(self):
        return self.__año_fabricacion

    def set_año_fabricacion(self, valor):
        año_actual = datetime.date.today().year
        if not (2000 <= valor <= año_actual):
            raise ValueError(f"El año de fabricación debe estar entre 2000 y {año_actual}.")
        self.__año_fabricacion = valor

# --- Ejemplo de uso ---

# Creación de un objeto válido
producto_valido = Producto("Laptop", 2023)
print(f"Producto: {producto_valido.nombre}, Año: {producto_valido.get_año_fabricacion()}")
# Salida: Producto: Laptop, Año: 2023

# Intentar crear un objeto con un año fuera de rango
try:
    producto_invalido = Producto("Teléfono antiguo", 1995)
except ValueError as e:
    print(e)
    # Salida: El año de fabricación debe estar entre 2000 y 2025.

# Intentar modificar el atributo a un valor fuera de rango
try:
    producto_valido.set_año_fabricacion(2050)
except ValueError as e:
    print(e)
    # Salida: El año de fabricación debe estar entre 2000 y 2025.