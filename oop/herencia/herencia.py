class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def es_mayor_de_edad(self):
        msg = 'es mayor de edad' if self.edad >= 18 else 'es menor de edad'
        return msg


class Alumno(Persona):
    def __init__(self, nombre, edad, notas) -> None:
        super().__init__(nombre, edad)
        self.notas = notas

class Docente(Persona):
    def __init__(self, nombre, edad, cargo) -> None:
        super().__init__(nombre, edad)
        self.cargo = cargo

a = Alumno('Juan', 17, [4, 6, 7])
d = Docente('Ana', 44, 'Programación')

print(a.nombre, a.es_mayor_de_edad())
print(d.nombre)
