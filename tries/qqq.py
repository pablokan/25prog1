# Encapsulamiento: getters and setters
class Persona:
    def __init__(self, edad) -> None:
        self.set_edad(edad)

    def get_edad(self): # getter (get == obtener)
        return f'Edad: {self.edad}'
    
    def set_edad(self, nueva_edad): # setter (set == asignar)
        if nueva_edad > 0:
            self.edad = nueva_edad
        else:
            print('No puede tener edad negativa')
            self.edad = None

persona = Persona(11)
print(persona.get_edad())
otra_persona = Persona(-35)
print(otra_persona.get_edad())
