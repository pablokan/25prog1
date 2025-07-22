# Reescritura del ejercicio 5 de la guía 10 
# para la clase Libro con setters y getters

class Libro:
    def __init__(self, titulo: str, autor: str, disponible: bool = True):
        print("\n-------------------------")
        print("Creando un nuevo libro... ", end='')
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_disponible(disponible)

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo: str):
        print("Asignando título... ", end='')
        if not isinstance(titulo, str):
            print("El título debe ser una cadena de texto")
        else:
            self._titulo = titulo

    def get_autor(self):
        return self._autor

    def set_autor(self, autor: str):
        print("Asignando autor... ", end='')
        if not isinstance(autor, str):
            print("El autor debe ser una cadena de texto")
        else:
            self._autor = autor

    def is_disponible(self):
        return self._disponible
    
    def set_disponible(self, disponible: bool):
        print("Asignando disponibilidad...")
        if not isinstance(disponible, bool):
            print("La disponibilidad debe ser un valor booleano")
        else:
            self._disponible = disponible

    def prestar(self) -> str:
        print("Intentando prestar el libro... ", end='')
        if self._disponible:
            salida = f"Prestando el libro: {self._titulo}"
            self._disponible = False
        else:
            salida = f"El libro {self._titulo} ya está prestado"
        return salida
    
    def devolver(self):
        print("Devolviendo el libro... ", end='')
        self._disponible = True
        return "Devolución exitosa"

    def __str__(self):
        return f"{self._titulo} por {self._autor} ({'Disponible' if self._disponible else 'No disponible'})"
    
fundacion = Libro("Fundación", "Isaac Asimov")
print(fundacion)  # Output: Fundación by Isaac Asimov
print(fundacion.prestar())
print(fundacion)
print(fundacion.prestar())  # Output: El libro ya está prestado
print(fundacion.devolver())
print(fundacion)
nineteen_eigthyfour = Libro("1984", "George Orwell", False)
print(nineteen_eigthyfour)  # Output: 1984 by George Orwell (No disponible)

