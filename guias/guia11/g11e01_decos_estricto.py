class Libro:
    def __init__(self, titulo: str, autor: str, disponible: bool = True):
        # Al asignar directamente en el constructor, se invocarán los setters
        # definidos con @<atributo>.setter, asegurando la validación inicial.
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    @property
    def titulo(self) -> str:
        """
        Getter para el título del libro.
        Permite acceder al título como si fuera un atributo normal (ej: mi_libro.titulo).
        """
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str):
        """
        Setter para el título del libro con validación.
        Se invoca cuando se asigna un valor a mi_libro.titulo = "Nuevo Título".
        """
        if not isinstance(titulo, str):
            raise ValueError("El título debe ser una cadena de texto.")
        if not titulo.strip(): # Valida que la cadena no esté vacía o solo con espacios
            raise ValueError("El título no puede estar vacío.")
        self._titulo = titulo # Almacena el valor en un atributo "privado"

    @property
    def autor(self) -> str:
        """
        Getter para el autor del libro.
        """
        return self._autor

    @autor.setter
    def autor(self, autor: str):
        """
        Setter para el autor del libro con validación.
        """
        if not isinstance(autor, str):
            raise ValueError("El autor debe ser una cadena de texto.")
        if not autor.strip():
            raise ValueError("El autor no puede estar vacío.")
        self._autor = autor

    @property
    def disponible(self) -> bool:
        """
        Getter para la disponibilidad del libro.
        """
        return self._disponible
    
    @disponible.setter
    def disponible(self, disponible: bool):
        """
        Setter para la disponibilidad del libro con validación.
        """
        if not isinstance(disponible, bool):
            raise ValueError("La disponibilidad debe ser un valor booleano.")
        self._disponible = disponible

    def prestar(self) -> str:
        """
        Intenta prestar el libro. Si está disponible, lo marca como no disponible.
        Accede a la propiedad 'disponible' directamente, lo que invoca al getter.
        """
        if self.disponible:  # Accede a la propiedad 'disponible' (llama al getter)
            self.disponible = False # Asigna a la propiedad 'disponible' (llama al setter)
            return f"Prestando el libro: \"{self.titulo}\""
        else:
            return f"El libro \"{self.titulo}\" ya está prestado."
    
    def devolver(self) -> str:
        """
        Devuelve el libro, marcándolo como disponible.
        """
        self.disponible = True # Asigna a la propiedad 'disponible' (llama al setter)
        return "Devolución exitosa."

    def __str__(self) -> str:
        """
        Método especial para la representación en cadena del objeto Libro.
        Se usa cuando haces print(mi_libro).
        """
        estado = "Disponible" if self.disponible else "No disponible"
        return f'"{self.titulo}" por {self.autor} ({estado})'

# --- Pruebas del código ---

print("--- Creación de objetos ---")
try:
    fundacion = Libro("Fundación", "Isaac Asimov")
    print(f"Libro creado: {fundacion}")

    el_hobbit = Libro("El Hobbit", "J.R.R. Tolkien", False)
    print(f"Libro creado: {el_hobbit}")

    # Intento de crear un libro con título inválido (lanzará error)
    print("\n--- Intento de crear libro con título inválido ---")
    # Este bloque try-except es crucial para capturar el ValueError lanzado por el setter
    libro_fallido = Libro(123, "Autor Desconocido")
    print(f"Libro creado (esto no debería verse): {libro_fallido}") 
except ValueError as e:
    print(f"Error al intentar crear un libro: {e}")

print("\n--- Operaciones con 'Fundación' ---")
# Accedemos a las propiedades directamente, sin necesidad de get_ o set_
print(fundacion)
print(fundacion.prestar())
print(fundacion)
print(fundacion.prestar()) # Intentar prestar de nuevo
print(fundacion.devolver())
print(fundacion)

print("\n--- Asignación de valores inválidos (lanzará error) ---")
try:
    fundacion.titulo = "" # Título vacío, esto llama al setter 'titulo' y lanza ValueError
    print(f"Título asignado: {fundacion.titulo}")
except ValueError as e:
    print(f"Error al asignar título: {e}")

try:
    fundacion.autor = None # Autor inválido, esto llama al setter 'autor' y lanza ValueError
    print(f"Autor asignado: {fundacion.autor}")
except ValueError as e:
    print(f"Error al asignar autor: {e}")

try:
    fundacion.disponible = "falso" # Disponibilidad inválida, esto llama al setter 'disponible' y lanza ValueError
    print(f"Disponibilidad asignada: {fundacion.disponible}")
except ValueError as e:
    print(f"Error al asignar disponibilidad: {e}")

print("\n--- Acceso y modificación directa ---")
print(f"El título actual de 'fundacion' es: {fundacion.titulo}")
fundacion.titulo = "Fundación e Imperio" # Esto llama al setter y valida
print(f"El nuevo título de 'fundacion' es: {fundacion.titulo}")
