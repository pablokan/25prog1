# Setter and Getter clásicos
class Persona:
    def __init__(self, edad):
        self.edad = edad

    def get_edad(self): # getter (get == obtiene)
        return f'Edad: {self.edad}'

    def set_edad(self, nueva_edad): # setter (set == asigna)
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.edad = nueva_edad

p1 = Persona(10)
print(p1.edad)
p2 = Persona(-30)
print(p2.edad)
try:
    p2.set_edad(-30)
except ValueError as error:
    print(f'Mensaje de error devuelto por el raise: {error}')



