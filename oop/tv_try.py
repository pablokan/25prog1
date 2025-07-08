class Producto:
    def __init__(self, nombre, cantidad_inicial):
        if cantidad_inicial < 0:
            raise ValueError("La cantidad inicial no puede ser negativa.")
        self.nombre = nombre
        self.cantidad = cantidad_inicial

# Ejemplo de uso
try:
    # Esto funcionará correctamente
    producto_valido = Producto("Manzanas", 10)
    print(f"Producto '{producto_valido.nombre}' creado con cantidad {producto_valido.cantidad}.")

    # Esto lanzará un ValueError
    producto_invalido = Producto("Naranjas", -5)
except ValueError as e:
    print(e)