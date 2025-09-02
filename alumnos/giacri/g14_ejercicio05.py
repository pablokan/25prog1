'''
(Herencia por Especializacion)
BolsaPremium heredando de BolsaProductos

-Basado en el Ejercicio 9 de la Guia 12.
-Crea una clase BolsaProductos con el atributo privado _nombres_productos y los dunders __len__, __getitem__ y __str__.
-La clase hija BolsaPremium debe heredar de BolsaProductos.
-BolsaPremium debe tener un atributo de clase privado _costo_extra_por_producto (ej.2.50 USD).
-Agregar un metodo obtener_costo_total() en BolsaPremium que calcule y retorne el costo extra total basado en la cantidad de productos en la bolsa.
-Crea un objeto BolsaPremium, agrega varios productos y luego imprime su costo total.
'''

class BolsaProductos:
    def __init__(self, nombres_productos):
        self._nombres_productos = nombres_productos

    def __len__(self):
        return len(self._nombres_productos)

    def __getitem__(self, indice):
        return self._nombres_productos[indice]
        
    def __str__(self):
        return f'Bolsa con: {','.join(self._nombres_productos)}'
    

class BolsaPremium(BolsaProductos):
    def __init__(self, nombres_productos, costo_extra_por_producto):
        super().__init__(nombres_productos)
        self._costo_extra_por_producto = costo_extra_por_producto
    
    def obtener_costo_total(self):
        return self.__len__() * self._costo_extra_por_producto
    
productos = ['Manzanas', 'Leche', 'Pan', 'Huevos']

bolsa = BolsaPremium(productos, 2.50)

print(f'Productos en la bolsa: {len(bolsa)}')
for i in range(len(bolsa)):
    print(f' - {bolsa[i]}')

print(f'\nCosto total premium: ${bolsa.obtener_costo_total()}')