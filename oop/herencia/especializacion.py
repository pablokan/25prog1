class Vehiculo:
    def __init__(self, color, velocidad):
        self.color = color
        self.velocidad = velocidad

    def es_veloz(self):
        msg = 'es veloz' if self.velocidad > 100 else 'es lento'
        return msg

class Bicicleta(Vehiculo):
    def __init__(self, color, velocidad, tipo):
        super().__init__(color, velocidad)
        self.tipo = tipo

class Auto(Vehiculo):
    def __init__(self, color, velocidad, cilindrada, puertas):
        super().__init__(color, velocidad)
        self.cilindrada = cilindrada
        self.puertas = puertas

class Moto(Vehiculo):
    def __init__(self, color, velocidad, cilindrada, tipo):
        super().__init__(color, velocidad)
        self.cilindrada = cilindrada
        self.tipo = tipo

