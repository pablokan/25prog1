# escribe una clase Persona que reciba una edad y que tenga getter y setter con decoradores
class Persona:
    def __init__(self, edad):
        self.edad = edad

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.__edad = nueva_edad

p = Persona(10)
print(p.edad)
p.edad = -20
print(p.edad)