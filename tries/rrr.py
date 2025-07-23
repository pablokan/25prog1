class Persona:
    def __init__(self, edad) -> None:
        self.edad = edad

    @property # decorador
    def edad(self): # getter
        return f'La edad es {self._edad}'
    
    @edad.setter
    def edad(self, nueva_edad): # setter
        if nueva_edad < 0:
            print('No puede tener edad negativa!')
            self._edad = None
        else:
            self._edad = nueva_edad

persona = Persona(10)
print(persona.edad)
otra_persona = Persona(-9)
print(otra_persona.edad)