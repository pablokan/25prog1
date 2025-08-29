class ListaNumeros:
  """
  Una clase que representa una lista de números y sobrecarga los métodos
  __len__, __getitem__ y __str__ para un comportamiento personalizado.
  """
  def __init__(self):
    """
    El constructor de la clase. Se ejecuta al crear un nuevo objeto.
    Inicializa el atributo 'numeros' como una lista vacía.
    """
    self.numeros = []

  def agregar_numero(self, numero):
    """
    Este es un método 'setter' tradicional para añadir un número a la lista.
    
    Args:
      numero (int or float): El número que se va a agregar a la lista interna.
    """
    # Usamos el método append() de las listas para agregar el nuevo número
    self.numeros.append(numero)

  def __len__(self):
    """
    Implementación del método mágico __len__.
    Permite que la función global len() funcione con objetos de esta clase.
    
    Returns:
      int: La cantidad de elementos en la lista 'numeros'.
    """
    return len(self.numeros)

  def __getitem__(self, indice):
    """
    Implementación del método mágico __getitem__.
    Permite acceder a los elementos usando la notación de corchetes (ej. objeto[0]).
    
    Args:
      indice (int): El índice del elemento al que se quiere acceder.
      
    Returns:
      El número que se encuentra en el índice especificado.
    """
    # Retorna el elemento de la lista interna en la posición dada por 'indice'
    return self.numeros[indice]

  def __str__(self):
    """
    Implementación del método mágico __str__.
    Define la representación del objeto como una cadena de texto legible.
    Se invoca al usar print() o str() sobre el objeto.
    
    Returns:
      str: Una cadena de texto que representa el contenido del objeto.
    """
    return f"Contiene {self.numeros}"

# --- Demostración de uso de la clase ---

# 1. Creamos un objeto (una instancia) de la clase ListaNumeros
mi_lista = ListaNumeros()

# 2. Agregamos varios números utilizando el método que creamos
mi_lista.agregar_numero(10)
mi_lista.agregar_numero(20)
mi_lista.agregar_numero(30)

# 3. Usamos la función len() para obtener su tamaño (esto invoca a __len__)
print(f"El tamaño de la lista es: {len(mi_lista)}")

# 4. Accedemos a un elemento por su índice (esto invoca a __getitem__)
print(f"El elemento en el índice 0 es: {mi_lista[0]}")
print(f"El elemento en el índice 2 es: {mi_lista[2]}")

# 5. Imprimimos el objeto completo (esto invoca a __str__)
print("Imprimiendo el objeto completo:")
print(mi_lista)
