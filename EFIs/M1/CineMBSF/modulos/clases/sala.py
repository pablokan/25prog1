from .asiento import Asiento
class Sala:
    def __init__(self, numero: int= 1, capacidad: int= 50)-> None: 
        self.numero = numero
        self.capacidad = capacidad
        self.asientos: list[Asiento] = [] 
        
    def crear_asientos(self)-> None: 
        filas = ["A","B","C","D","E"]
        for fila in filas: 
            for num in range(1,11): 
                self.asientos.append(Asiento(fila,num))

    def buscar_asiento(self, fila: str, numero: int):
        for asiento in self.asientos:
            if asiento.fila == fila.upper() and asiento.numero == numero:
                return asiento
        return None        

             
                



