# atributos y métodos de clases
class Persona:
    especie = 'Homo Sapiens' # atributo de clase (aplica a todos los objetos)

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre # atributos de instancia 
        self.edad = edad

    def __str__(self):
        return f'Especie: {self.especie}. Nombre: {self.nombre}. Edad: {self.edad}'
    
    @classmethod
    def desde_datos(cls, persona_datos): #constructor alternativo
        nombre, edad = persona_datos.split('-')
        edad = int(edad)
        return cls(nombre, edad)
    
    @classmethod
    def set_especie(cls, nombre) -> None:
        cls.especie = nombre

alguien = Persona('Ana', 22)
print(alguien)
otra_persona = Persona('Juan', 35)
print(otra_persona)
dato1 = 'Luis-61'
otra_persona_mas = Persona.desde_datos(dato1)
print(otra_persona_mas)
Persona.set_especie('Homo Neanderthalensis')
print(alguien)
print(otra_persona)