class Musico:
    def __init__(self, nombre: str, instrumento: str) -> None:
        self.nombre = nombre
        self.instrumento = instrumento

    def __str__(self) -> str:
        return f'{self.nombre} toca {self.instrumento}'

class Banda:
    def __init__(self, nombre: str, members: list[tuple[str, str]]):
        self.nombre = nombre
        self.members: list[Musico] = [Musico(*datos) for datos in members]

    def __str__(self):
        return '\n'.join([str(m) for m in self.members])

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

        