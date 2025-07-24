from pathlib import Path
from ...libs.basic import raya

class Auto:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_info(self):
        print(self.marca, self.modelo, self.anio)

def main():
    raya('inicio')
    fitito = Auto('Fiat', '600', 1970)
    r12 = Auto('Renault', 'R12', 1980)
    fitito.mostrar_info()
    r12.mostrar_info()
    raya('fin')
    
if __name__ == '__main__':
    main()

