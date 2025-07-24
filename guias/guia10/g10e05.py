class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

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
    

def main():
    print(f'\n{'-'*80}')
    fundacion = Libro("Fundación", "Isaac Asimov")
    print(fundacion)  # Output: Fundación by Isaac Asimov
    print(fundacion.prestar())
    print(fundacion)
    print(fundacion.prestar())  # Output: El libro ya está prestado
    print(fundacion.devolver())
    print(fundacion)
    print(f'{'-'*80}\n')

if __name__ == '__main__':
    main()
