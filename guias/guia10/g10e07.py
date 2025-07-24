class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def obtener_valor_total(self):
        return f'El valor total del stock de {self.nombre} es {self.precio * self.stock}'

inventario = []

for i in range(3):
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    stock = int(input('stock: '))
    p = Producto(nombre, precio, stock)
    inventario.append(p)

for p in inventario:
    print(p.nombre, p.obtener_valor_total())


