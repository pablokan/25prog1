class Natural(int):
    def __new__(cls, value):
        if not isinstance(value, int):
            raise TypeError("El valor debe ser un número entero.")
        if value < 0:
            raise ValueError("El valor debe ser un número natural (no negativo).")
        
        # Llama al constructor de la clase base (int) para crear la instancia.
        # Aquí es donde se "construye" el objeto int con el valor validado.
        return super().__new__(cls, value)

    # __init__ es opcional aquí porque no hay estado adicional que inicializar
    # más allá del valor int ya establecido por __new__.
    # Si quisieras añadir atributos propios de Natural, los pondrías aquí.
    # def __init__(self, value):
    #     print(f"Instancia de Natural inicializada con valor: {self}")

# Ejemplos de uso:

n1 = Natural(5)
print(f"n1: {n1}, Tipo: {type(n1)}") # Salida: n1: 5, Tipo: <class '__main__.Natural'>

n2 = Natural(0)
print(f"n2: {n2}, Tipo: {type(n2)}") # Salida: n2: 0, Tipo: <class '__main__.Natural'>

# Intentar crear un número negativo (esto generará un error)
try:
    n3 = Natural(-3)
except ValueError as e:
    print(f"Error al crear n3: {e}") # Salida: Error al crear n3: El valor debe ser un número natural (no negativo).

# Intentar crear un flotante (esto generará un error)
try:
    n4 = Natural(3.14)
except TypeError as e:
    print(f"Error al crear n4: {e}") # Salida: Error al crear n4: El valor debe ser un número entero.

# Puedes usar operaciones matemáticas con ellos como si fueran int
n5 = Natural(10) + Natural(20)
print(f"n5 (suma): {n5}, Tipo: {type(n5)}") # Salida: n5 (suma): 30, Tipo: <class 'int'>
# Nota: El resultado de la operación vuelve a ser un 'int' estándar,
# a menos que sobrescribas los métodos mágicos de operación (ej. __add__).