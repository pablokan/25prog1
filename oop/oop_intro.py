class Alumno:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = f'{nombre[0].lower()}.{apellido.lower()}@itecriocuarto.org.ar'

    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'

    def promedio(self, *args):
        return sum(args) / len(args)

a1 = Alumno('Juan', 'Torres')
a2 = Alumno('Ana', 'Mesa')

print(a1.nombre_completo())
print(a1.mail)
print(a1.promedio(4,6,7))
