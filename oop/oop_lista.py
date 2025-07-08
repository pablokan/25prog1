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

# sustituye la instanciación individual y construye una carga pidiendo al usuario que ingrese los datos, se instancie y se vaya cargando los objetos en una lista. Luego, hacé un recorrido mostrando los nombres completos y los mails
alumnos = []
num_alumnos = int(input("¿Cuántos alumnos desea ingresar? "))

for i in range(num_alumnos):
    print(f"\nIngrese los datos para el alumno {i+1}:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    nuevo_alumno = Alumno(nombre, apellido)
    alumnos.append(nuevo_alumno)

print("\n--- Lista de Alumnos ---")
for alumno in alumnos:
    print(f"Nombre Completo: {alumno.nombre_completo()}")
    print(f"Mail: {alumno.get_mail()}")
