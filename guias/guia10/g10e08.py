class Contacto:
    def __init__(self, nombre, telefono) -> None:
        self.nombre = nombre
        self.telefono = telefono

    def mostrar_contacto(self, datos='nombre'):
        print(self.nombre)
        if datos == 'full':
            print(self.telefono)

agenda = []
for i in range(2):
    nombre = input('Nombre: ')
    telefono = input('Telefono: ')
    c = Contacto(nombre, telefono)
    agenda.append(c)

todo = input('Quiere ver todos los datos? ')
if todo == 's':
    r = 'full'
else:
    r = ''
for c in agenda:
    print(c.mostrar_contacto(r))

