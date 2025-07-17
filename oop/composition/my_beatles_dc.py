from dataclasses import dataclass

@dataclass
class Musico:
    nombre: str
    instrumento: str

    def __str__(self) -> str:
        return f'{self.nombre} toca {self.instrumento}'

@dataclass
class Band:
    nombre: str
    miembros: list[Musico]

    @classmethod
    def desde_lista_tupla(cls, nombre: str, miembros_data: list[tuple[str, str]]):
        cls.miembros = [Musico(nombre, instrumento) for nombre, instrumento in miembros_data]
        return cls(nombre, cls.miembros)

    def __str__(self):
        salida = f"\n---------------------\nNombre de la banda: {self.nombre}\n" \
        f"{', '.join([str(m) for m in self.miembros])}"
        return salida

if __name__ == "__main__":
    integrantes_data = [
        ('John', 'la guitarra'),
        ('Paul', 'el bajo'),
        ('George', 'la guitarra'),
        ('Ringo', 'la batería')
    ]
    integrantes_data.append(('Quinto', 'la pandereta'))
    beatles = Band.desde_lista_tupla('Los Beatles', integrantes_data)
    beatles.miembros.append(Musico('Sexto', 'la pianola'))
    print(beatles)

    duo = [
        ('Simon', 'el oboe'),
        ('Garfunkel', 'la flauta')
    ]
    s_g = Band('Simon & Garfunkel', [Musico(*d) for d in duo])
    print(s_g)
