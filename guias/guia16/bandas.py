class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Musico(Persona):
    def __init__(self, nombre, instrumento) -> None:
        super().__init__(nombre)
        self.instrumento = instrumento

    def __str__(self):
        return f'{self.nombre} toca {self.instrumento}'

class Banda:
    def __init__(self, nombre, miembros) -> None:
        self.nombre = nombre
        self.miembros = [] # lista de objetos Musico
        for datos in miembros:
            nombre_musico, instrumento = datos
            #musico = Musico(nombre_musico, instrumento) # composición
            musico = Musico(*datos) # composición
            self.miembros.append(musico)

    def __str__(self) -> str:
        salida = f'\nBanda {self.nombre}\n'
        salida += ' - '.join([str(m) for m in self.miembros])
        return salida

integrantes = [
        ('John', 'la guitarra'), 
        ('Paul', 'el bajo'), 
        ('George', 'la guitarra'), 
        ('Ringo', 'la batería')
    ]
integrantes.append(('Quinto Beatle', 'pandereta'))

beatles = Banda('Los Beatles', integrantes)
print(beatles)

duo = [
    ('Simon', "arpa"),
    ('Garfunkel', 'bongó')
]
sg = Banda('Simon & Garfunkel', duo)
print(sg)