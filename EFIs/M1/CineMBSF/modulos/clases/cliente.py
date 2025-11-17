class Cliente():
    def __init__(self, nombre: str, apellido: str, telefono: int)-> None:
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre)-> None:
        if not isinstance(nombre, str):
            raise TypeError('El nombre del cliente debe ser un valor de tipo string.')
        if not nombre.strip():
            raise ValueError('El nombre del cliente no puede estar vacío.')
        else:
            self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido)-> None:
        if not isinstance(apellido, str):
            raise TypeError('El apellido del cliente debe ser un valor de tipo string.')
        if not apellido.strip():
            raise TypeError('El apellido del cliente no puede estar vacío.')
        else:
            self._apellido = apellido
    
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, telefono)-> None:
        if not isinstance(telefono, int):
            raise TypeError('El teléfono del cliente debe ser un valor tipo entero.')
        if telefono <= 0:
            raise TypeError('El telélefono del cliente no puede ser negativo ni menor a cero.')
        else:
            self._telefono = telefono
    
    def __str__(self):
        return f'Cliente  \nNombre: {self.nombre} \nApellido: {self.apellido} \nTeléfono: {self.telefono}'
    