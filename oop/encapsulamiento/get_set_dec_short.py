# Uso de setter y getter de manera pitónica (con decoradores)
class Persona:
    def __init__(self, edad):
        self.edad = edad

    @property # decorador 
    def edad(self): # getter (get == obtiene)
        return f'Edad: {self._edad}' # este es el atributo VERDADERO

    @edad.setter 
    def edad(self, nueva_edad): # setter (set == asigna)
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = nueva_edad # este es el atributo VERDADERO

p1 = Persona(10)
print(p1.edad)

try:
    p2 = Persona(-30)
except ValueError as error:
    print(f'Mensaje de error devuelto por el raise: {error}')

# p1.edad(50) # No funciona así el setter
p1.edad = 50 # ahora si!
print()
print(f'{p1.edad=}') # este es el GETTER
print(f'{p1._edad=}') # este es el atributo VERDADERO

