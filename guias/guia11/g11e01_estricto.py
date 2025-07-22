# robustez en la validación y separación de responsabilidades

class Libro:
    def __init__(self, titulo: str, autor: str, disponible: bool = True):
        # Al inicializar, es crucial que los atributos sean válidos.
        # Si la asignación falla, el constructor lanzará un ValueError.
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_disponible(disponible)

    def get_titulo(self) -> str:
        return self._titulo

    def set_titulo(self, titulo: str):
        # Validamos el tipo y lanzamos una excepción si no es válido.
        # Esto asegura que el título siempre sea una cadena de texto.
        if not isinstance(titulo, str):
            raise ValueError("El título debe ser una cadena de texto.")
        if not titulo.strip(): # También validamos que no esté vacío o solo espacios
            raise ValueError("El título no puede estar vacío.")
        self._titulo = titulo
        # Eliminamos el 'print' interno para no mezclar lógica con salida.

    def get_autor(self) -> str:
        return self._autor

    def set_autor(self, autor: str):
        # Similar para el autor.
        if not isinstance(autor, str):
            raise ValueError("El autor debe ser una cadena de texto.")
        if not autor.strip():
            raise ValueError("El autor no puede estar vacío.")
        self._autor = autor
        # Eliminamos el 'print' interno.

    def is_disponible(self) -> bool:
        return self._disponible
    
    def set_disponible(self, disponible: bool):
        # Validamos el tipo.
        if not isinstance(disponible, bool):
            raise ValueError("La disponibilidad debe ser un valor booleano.")
        self._disponible = disponible
        # Eliminamos el 'print' interno.

    def prestar(self) -> str:
        # El método decide si puede prestar y devuelve un mensaje claro.
        if self._disponible:
            self._disponible = False
            return f"Prestando el libro: {self._titulo}"
        else:
            return f"El libro {self._titulo} ya está prestado."
    
    def devolver(self) -> str:
        # El método simplemente cambia el estado.
        self._disponible = True
        return "Devolución exitosa."

    def __str__(self) -> str:
        # Este método es para representación del objeto, no para mensajes de acción.
        estado = "Disponible" if self._disponible else "No disponible"
        return f'"{self._titulo}" por {self._autor} ({estado})'

# --- Pruebas del código mejorado ---

print("--- Creación de objetos ---")
try:
    fundacion = Libro("Fundación", "Isaac Asimov")
    print(f"Libro creado: {fundacion}")

    libro_vacio = Libro("El Hobbit", "J.R.R. Tolkien", False)
    print(f"Libro creado: {libro_vacio}")

    # Intento de crear un libro con título inválido (lanzará error)
    print("\n--- Intento de crear libro con título inválido ---")
    libro_fallido = Libro(123, "Autor Desconocido")
    print(f"Libro creado (esto no debería verse): {libro_fallido}") # Esto no se ejecutará
except ValueError as e:
    print(f"Error al intentar crear un libro: {e}")

print("\n--- Operaciones con 'Fundación' ---")
print(fundacion)
print(fundacion.prestar())
print(fundacion)
print(fundacion.prestar()) # Intentar prestar de nuevo
print(fundacion.devolver())
print(fundacion)

print("\n--- Asignación de valores inválidos (lanzará error) ---")
try:
    fundacion.set_titulo("") # Título vacío
    print(f"Título asignado: {fundacion.get_titulo()}")
except ValueError as e:
    print(f"Error al asignar título: {e}")

try:
    fundacion.set_autor(None) # Autor inválido
    print(f"Autor asignado: {fundacion.get_autor()}")
except ValueError as e:
    print(f"Error al asignar autor: {e}")

try:
    fundacion.set_disponible("falso") # Disponibilidad inválida
    print(f"Disponibilidad asignada: {fundacion.is_disponible()}")
except ValueError as e:
    print(f"Error al asignar disponibilidad: {e}")