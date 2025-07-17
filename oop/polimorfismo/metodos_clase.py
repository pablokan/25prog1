# atributos y métodos de clases
class Persona:
    especie = 'Homo Sapiens'

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Especie: {self.especie}. Nombre: {self.nombre}. Edad: {self.edad}'

    @classmethod
    def desde_datos(cls, persona_datos): # constructor alternativo
        nombre, edad = persona_datos.split('-')
        return cls(nombre, edad)


alguien = Persona('Ana', 22)
print(alguien)
dato1 = 'Juan-35'
otra_persona = Persona(*dato1.split('-'))
print(otra_persona)
dato2 = 'Luis-61'
otra_persona_mas = Persona.desde_datos(dato2)
print(otra_persona_mas)
