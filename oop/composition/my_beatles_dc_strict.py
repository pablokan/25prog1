from dataclasses import dataclass, field
from typing import List, Tuple # Import List and Tuple from typing for older Python versions (<3.9)

@dataclass
class Musico:
    nombre: str
    instrumento: str

    def __str__(self) -> str:
        return f'{self.nombre} toca {self.instrumento}'

@dataclass
class Band:
    nombre: str
    members: List[Musico] = field(default_factory=list) # Explicitly use List from typing

    @classmethod
    def from_tuple_list(cls, nombre: str, members_data: List[Tuple[str, str]]): # Explicitly type members_data
        members = [Musico(name, instrument) for name, instrument in members_data]
        return cls(nombre=nombre, members=members)

    def __str__(self):
        if not self.members:
            return f"La banda {self.nombre} no tiene integrantes."
        return '\n'.join([str(m) for m in self.members])

if __name__ == "__main__":
    integrantes_data: List[Tuple[str, str]] = [ # Explicitly type the variable
        ('John', 'la guitarra'),
        ('Paul', 'el bajo'),
        ('George', 'la guitarra'),
        ('Ringo', 'la batería')
    ]
    integrantes_data.append(('Quinto', 'la pandereta'))

    beatles = Band.from_tuple_list('Los Beatles', integrantes_data)
    print(beatles)

    print("\n--- Agregando un nuevo miembro directamente ---")
    beatles.members.append(Musico('Yoko', 'la voz'))
    print(beatles)

    print("\n--- Banda vacía de ejemplo ---")
    no_band = Band("Sin banda")
    print(no_band)