class Producto:
    def __init__(self, id: int, tipo: str, precio: float)-> None:
        self.id = id
        self.tipo = tipo
        self.precio = precio

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id: int)-> None:
        if not isinstance(id, int):
            raise TypeError('La opción ingresada debe ser dato de tipo numérico.')
        else:
            self._id = id

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo: str)-> None:
        if not isinstance(tipo, str):
            raise TypeError('El comestible ingresado debe ser dato de tipo string.')
        else:
            self._tipo = tipo
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio: float)-> None:
        if not isinstance(precio, (int, float)):
            raise TypeError('El precio ingresado debe ser dato tipo numérico y no puede ser cero o negativo.')
        if precio < 0:
            raise ValueError('El precio no puede ser menor a cero.')
        self._precio = float(precio)
    
    def obtener_precio(self):
        return self.precio

    
class Bebida(Producto):
    def __init__(self, id, tipo, marca: str, precio: float)-> None:
        super().__init__(id, tipo, precio)
        self.marca = marca
        self.volumen = '500ml'
    
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca: str)-> None:
        if not isinstance(marca, str):
            raise TypeError('La marca ingresada debe ser dato de tipo string.')
        else:
            self._marca = marca
    
    def __str__(self):
        return f'Opción: {self.id} \n Tipo: {self.tipo} \n Marca: {self.marca} \n Volumen: {self.volumen} \n Precio: ${self.precio} '

class Comestible(Producto):
    def __init__(self, id, tipo, precio: float):
        super().__init__(id, tipo, precio)
    
    def __str__(self):
        return f'Opción: {self.id} \n Tipo: {self.tipo} \n Precio: ${self.precio}'
        