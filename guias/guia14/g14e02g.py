class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, nuevo_autor):
        self._autor = nuevo_autor
        
    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, estado):
        if isinstance(estado, bool):
            self._disponible = estado
        else:
            print("Error: El estado de disponibilidad debe ser un booleano.")

    def prestar(self) -> str:
        print("Intentando prestar el libro...")
        if self.disponible:
            salida = f"Prestando el libro: {self.titulo}"
            self.disponible = False
        else:
            salida = f"El libro {self.titulo} ya está prestado"
        return salida
    
    def devolver(self):
        print("Devolviendo el libro...")
        self.disponible = True
        return "Devolución exitosa"

    def __str__(self):
        return f"{self.titulo} by {self.autor} ({'Disponible' if self.disponible else 'No disponible'})"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato_archivo, disponible=True):
        super().__init__(titulo, autor, disponible)
        self._formato_archivo = formato_archivo

    @property
    def formato_archivo(self):
        return self._formato_archivo

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, estado):
        if not estado:
            print("Error: Los libros digitales siempre están disponibles y no pueden ser prestados en el sentido tradicional.")
        else:
            self._disponible = estado
    
    def __str__(self):
        return f"{self.titulo} by {self.autor} ({self.formato_archivo} - {'Disponible' if self.disponible else 'No disponible'})"
    

def main():
    print(f'\n{'-'*80}')
    print("--- Demostración de Libro Físico ---")
    fundacion = Libro("Fundación", "Isaac Asimov")
    print(fundacion)
    print(fundacion.prestar())
    print(fundacion)
    print(fundacion.prestar())
    print(fundacion.devolver())
    print(fundacion)

    print(f'{'-'*80}')
    print("\n--- Demostración de Libro Digital ---")
    dune_digital = LibroDigital("Dune", "Frank Herbert", "ePub")
    print(dune_digital)
    print(dune_digital.prestar())
    print(dune_digital)
    dune_digital.disponible = False
    print(dune_digital)
    print(f'{'-'*80}\n')

if __name__ == '__main__':
    main()