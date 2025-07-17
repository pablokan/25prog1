class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

p = Persona('11')

print(p.get_nombre())
