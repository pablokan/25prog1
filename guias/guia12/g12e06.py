
class Punto2D:
    """
    Representa un punto en un plano bidimensional (x, y).
    Los objetos de esta clase son inmutables una vez creados.
    """

    def __init__(self, x, y):
        """
        Inicializa una nueva instancia de Punto2D.

        Args:
            x (float): La coordenada en el eje x.
            y (float): La coordenada en el eje y.
        """
        # Usamos un guion bajo para indicar que son atributos "privados"
        # y no deben ser modificados directamente.
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        """Obtiene la coordenada x del punto."""
        return self._x

    @property
    def y(self):
        """Obtiene la coordenada y del punto."""
        return self._y

    def __str__(self):
        """
        Retorna una representación del punto fácil de leer para el usuario.
        Se invoca al usar print() o str().
        """
        return f"Punto(x={self.x}, y={self.y})"

    def __repr__(self):
        """
        Retorna una representación inequívoca del objeto, útil para desarrolladores.
        Idealmente, debería ser código Python válido para recrear el objeto.
        Se invoca al usar repr() o al mostrar el objeto en la consola.
        """
        return f"Punto2D({self.x}, {self.y})"

    def __add__(self, otro_punto):
        """
        Sobrecarga el operador de suma (+).
        Permite sumar dos objetos Punto2D.

        Args:
            otro_punto (Punto2D): El otro punto a sumar.

        Returns:
            Punto2D: Un nuevo objeto Punto2D resultado de la suma.
        """
        # Es una buena práctica verificar que estamos sumando objetos compatibles.
        if not isinstance(otro_punto, Punto2D):
            raise TypeError('Los operandos tienen que ser puntos')

        # Se crea y retorna un nuevo punto con las coordenadas sumadas.
        nuevo_x = self.x + otro_punto.x
        nuevo_y = self.y + otro_punto.y
        return Punto2D(nuevo_x, nuevo_y)

# --- Bloque de demostración ---

# 1. Crear dos instancias (objetos) de la clase Punto2D.
punto1 = Punto2D(1.5, 4.0)
punto2 = Punto2D(3.5, -1.5)
punto3 = 1

# 2. Sumar los dos puntos. Esto llama internamente a punto1.__add__(punto2).
punto_resultado = punto1 + punto2
try:
    suma_fallida = punto1 + punto3
except TypeError as e:
    print(f"Error: {e}")

# 3. Imprimir los puntos.
#    La función print() utiliza automáticamente el método __str__ de los objetos.
print(f"Punto 1: {punto1}")
print(f"Punto 2: {punto2}")
print(f"Resultado de la suma: {punto_resultado}")
print("-" * 20) # Separador para mayor claridad

# 4. Imprimir la representación para desarrolladores (__repr__) de uno de los puntos.
#    Para ello, usamos la función repr().
print(f"Representación __repr__ del punto 1: {repr(punto1)}")
print(f"Representación __repr__ del resultado: {repr(punto_resultado)}")

