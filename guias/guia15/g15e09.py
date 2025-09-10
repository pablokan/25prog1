from abc import ABC, abstractmethod

class DispositivoElectronico(ABC):
    def __init__(self, nombre):
        self._encendido = False
        self._nombre = nombre
        print(f'Dispositivo {self._nombre} creado')

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    def estado_actual(self):
        estado = "encendido" if self._encendido else "apagado"
        return f"{self._nombre} está {estado}."

class Laptop(DispositivoElectronico):
    def encender(self):
        if not self._encendido:
            self._encendido = True
            print("Laptop encendida. ¡Bienvenido!")
        else:
            print("La Laptop ya está encendida.")

    def apagar(self):
        if self._encendido:
            self._encendido = False
            print("Laptop apagada. ¡Hasta pronto!")
        else:
            print("La Laptop ya está apagada.")

class Smartphone(DispositivoElectronico):
    def encender(self):
        if not self._encendido:
            self._encendido = True
            print("Smartphone encendido. Desliza para desbloquear.")
        else:
            print("El Smartphone ya está encendido.")

    def apagar(self):
        if self._encendido:
            self._encendido = False
            print("Smartphone apagado. Nos vemos.")
        else:
            print("El Smartphone ya estaba apagado.")

def main():
    disps: list[DispositivoElectronico] = [
        Laptop('MacBook Pro i9'), 
        Smartphone('Samsung S25')
        ]
    for disp in disps:
        print('-----------------------')
        print(disp.estado_actual())
        disp.encender()
        print(disp.estado_actual())
        disp.apagar()
        print(disp.estado_actual())
        

if __name__ == '__main__':
    main()
