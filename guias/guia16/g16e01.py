# Librería y Libro: Crea una clase Libro con atributos titulo y autor. Luego, crea una clase Libreria que contiene una lista de objetos Libro. Libreria debe tener métodos para agregar_libro y listar_libros.


class Libro:
    def __init__(self, titulo, autor) -> None:
        self._titulo = titulo
        self._autor = autor

    def __str__(self):
        return f'{self._titulo} de {self._autor}'

class Libreria:
    def __init__(self) -> None:
        self._libros: list[Libro] = []

    def agregar_libro(self, libro):
        self._libros.append(libro)

    def listar_libros(self):
        for l in self._libros:
            print(l)

def main():
    lema = Libreria()
    lema.agregar_libro(Libro('Fundación', 'Asimov'))
    lema.agregar_libro(Libro('2001', 'Arthur Clarke'))
    lema.listar_libros()


if __name__ == '__main__':
    main()