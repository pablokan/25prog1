from .pelicula import Pelicula
from .asiento import Asiento

class Boleto: 
    def __init__ (self, pelicula: Pelicula, asiento: Asiento, horario: str, sala: int, precio: float)-> None: 
        self.pelicula = pelicula 
        self.asiento = asiento
        self.horario = horario
        self.sala = sala
        self.precio = precio        

    @property
    def horario(self):
        return self._horario

    @horario.setter
    def horario(self, nuevohorario: str):
        if isinstance (nuevohorario, str): 
             self._horario = nuevohorario
        else:
           raise TypeError ("Debes ingresar el horario en formato string")

    @property 
    def sala(self):
        return self._sala

    @sala.setter
    def sala(self, nuevasala: int):
        if isinstance (nuevasala,int): 
            self._sala = nuevasala
        else: 
            raise TypeError ("Debes ingresar la sala en formato entero")

    @property 
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevoprecio: int | float):
        if not isinstance (nuevoprecio,(int, float)):
            raise TypeError ("Debes ingresar el precio en formato entero o decimal")
        if nuevoprecio < 0:
            raise ValueError('El precio no puede ser negativo.')
        self._precio = float(nuevoprecio)

    def obtener_precio(self):
        return self.precio

    def __str__(self):
        return (
            f"---------------BOLETO---------------\n"
            f"PELICULA: {self.pelicula.nombre}\n"
            f"DURACIÓN: {self.pelicula.duracion}\n"
            f"GENERO: {self.pelicula.genero}\n"
            f"ASIENTO: {self.asiento.fila} {self.asiento.numero}\n"
            f"HORARIO: {self.horario}\n"
            f"PRECIO: ${self.precio:.2f}\n"
            f"SALA: {self.sala}\n"
            f"------------------------------------"
        )





