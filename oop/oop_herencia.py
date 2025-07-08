class Vehiculo:
    def __init__(self, plazas, velocidad):
        self.plazas = plazas
        self.velocidad = velocidad

    def mostrar_info(self):
        return f"Plazas: {self.plazas}, Velocidad: {self.velocidad}"

class VehiculoMotorizado(Vehiculo):
    def __init__(self, plazas, velocidad, motor):
        super().__init__(plazas, velocidad)
        self.motor = motor

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Motor: {self.motor}"

class Coche(VehiculoMotorizado):
    def __init__(self, plazas, velocidad, motor, marca):
        super().__init__(plazas, velocidad, motor)
        self.marca = marca

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Marca: {self.marca}"

class Bicicleta(Vehiculo):
    def __init__(self, plazas, velocidad, tipo):
        super().__init__(plazas, velocidad)
        self.tipo = tipo

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo: {self.tipo}"

# Crear instancias de las clases
mi_coche = Coche(5, 200, "Nafta", "Toyota")
mi_bici = Bicicleta(1, 30, "Playera")

# Mostrar información
print(mi_coche.mostrar_info())
print(mi_bici.mostrar_info())
