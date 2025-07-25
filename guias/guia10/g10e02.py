from sys import path
path.append('/home/kan/development/25prog1/libs')
from basic import raya

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def obtener_valor_total(self):
        return f'El valor total del stock de {self.nombre} es {self.precio * self.stock}'
    
def main():
    raya('inicio')
    mesa = Producto('Mesa', 100, 12)
    print(mesa.obtener_valor_total())
    raya('fin')

if __name__ == '__main__':
    main()
