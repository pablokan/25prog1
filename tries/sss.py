class Persona:
    def __init__(self, edad):
        print('⦃constructor', end=' ')
        self.edad = edad
        print('constructor⦄', end=' ')

    @property # decorador 
    def edad(self): # getter (get == obtiene)
        print('⦃get', end=' ')
        return f'Edad: {self._edad}⦄' # este es el atributo VERDADERO

    @edad.setter 
    def edad(self, nueva_edad): # setter (set == asigna)
        print('⦃set', end=' ')
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = nueva_edad # este es el atributo VERDADERO
        print(f'{self._edad=}', end=' ')
        print('set⦄', end=' ')


persona = Persona(10)
print(persona.edad)

try:
    otra_persona = Persona(-30)
except ValueError as error:
    print(f'Mensaje de error devuelto por el raise: {error}')

#p1.edad(50) # No funciona así el setter
persona.edad = 50 # ahora si!
print()
print(f'⦃ {persona.edad=} ⦄') # este es el GETTER
print(f'⦃ {persona._edad=} ⦄') # este es el atributo VERDADERO
