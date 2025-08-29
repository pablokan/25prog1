# g13e01.py

class Punto2D:
    _contador_puntos: int = 0

    def __init__(self, x: float, y: float) -> None:
        self._x: float = x
        self._y = y
        Punto2D._contador_puntos += 1

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @classmethod
    def obtener_total_puntos(cls):
        return cls._contador_puntos

    def __str__(self):
        return f"Punto(x={self.x}, y={self.y})"

    def __repr__(self):
        return f"Punto2D({self.x}, {self.y})"

    def __add__(self, otro_punto):
        if isinstance(otro_punto, Punto2D):
            return Punto2D(self.x + otro_punto.x, self.y + otro_punto.y)
        else:
            raise TypeError("Solo se pueden sumar objetos Punto2D")

# Pruebas
p1 = Punto2D(2, 3)
p2 = Punto2D(4, 5)
p3 = p1 + p2
print(p3)
print(f"Total de puntos creados: {Punto2D.obtener_total_puntos()}")