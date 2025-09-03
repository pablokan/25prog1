class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

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
    fundacion = LibroDigital("Fundación", "Isaac Asimov", 'ePub')
    print(fundacion)  # Output: Fundación by Isaac Asimov
    print(fundacion.prestar())
    print(fundacion)
    print(fundacion.prestar())  # Output: El libro ya está prestado
    print(fundacion.devolver())
    print(fundacion)
    print(f'{'-'*80}\n')

if __name__ == '__main__':
    main()
