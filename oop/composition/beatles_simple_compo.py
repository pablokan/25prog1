class Musico:
    def __init__(self, nombre, instrumento) -> None:
        self.nombre = nombre
        self.instrumento = instrumento

    def __str__(self):
        return f'{self.nombre} toca {self.instrumento}'

class Banda:
    def __init__(self, nombre, members):
        self.nombre = nombre
        self.members = []
        for datos in members:
            nombre_musico, instrumento = datos
            musico = Musico(nombre_musico, instrumento) # Composición
            self.members.append(musico)

    def __str__(self):
        salida = f'Banda {self.nombre}\n-------------------\n'
        salida += '\n'.join([str(m) for m in self.members])
        return salida

if __name__ == "__main__":
    integrantes = [
        ('John', 'la guitarra'), 
        ('Paul', 'el bajo'), 
        ('George', 'la guitarra'), 
        ('Ringo', 'la batería')
    ]
    integrantes.append(('Quinto', 'la pandereta'))

    beatles = Banda('Los Beatles', integrantes)
    print(beatles)

        