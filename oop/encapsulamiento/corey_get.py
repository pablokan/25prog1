class Persona:
    def __init__(self, nombre, edad, altura) -> None:
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, asignar_nombre):
        self.__nombre = asignar_nombre

p = Persona('John', 33, 1.88)
print(p.edad)
