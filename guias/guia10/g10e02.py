class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def obtener_valor_total(self):
        return f'El valor total del stock de {self.nombre} es {self.precio * self.stock}'
    
def main():
    print(f'\n{'-'*80}')
    mesa = Producto('Mesa', 100, 12)
    print(mesa.obtener_valor_total())
    print(f'{'-'*80}\n')

if __name__ == '__main__':
    main()
