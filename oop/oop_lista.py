class Alumno:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = f'{nombre[0].lower()}.{apellido.lower()}@itecriocuarto.org.ar'

    def get_mail(self):
        return self.mail

    def nombre_completo(self):
        return f'{self.nombre} {self.apellido}'

    def promedio(self, *args):
        return sum(args) / len(args)

alumnos: list[Alumno] = []

for i in range(2):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    nuevo_alumno = Alumno(nombre, apellido)
    alumnos.append(nuevo_alumno)

print()
print("Lista de Alumnos")
for alumno in alumnos:
    print(f"Nombre Completo: {alumno.nombre_completo()}")
    print(f"Mail: {alumno.}")
