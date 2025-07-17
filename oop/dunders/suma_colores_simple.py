class Color:
    def __init__(self, name):
        self.name = name.lower() # Guardamos el nombre en minúsculas para consistencia

    def __add__(self, other):
        if not isinstance(other, Color):
            raise TypeError(f"No se puede sumar un Color con un objeto de tipo {type(other).__name__}")

        # Definimos las reglas de mezcla sustractiva (pigmentos)
        # Primarios: Rojo, Amarillo, Azul
        # Secundarios: Naranja, Verde, Morado/Violeta

        # Azul + Amarillo = Verde
        if (self.name == "azul" and other.name == "amarillo") or \
           (self.name == "amarillo" and other.name == "azul"):
            return Color("verde")
        
        # Rojo + Amarillo = Naranja
        elif (self.name == "rojo" and other.name == "amarillo") or \
             (self.name == "amarillo" and other.name == "rojo"):
            return Color("naranja")

        # Azul + Rojo = Morado/Violeta
        elif (self.name == "azul" and other.name == "rojo") or \
             (self.name == "rojo" and other.name == "azul"):
            return Color("morado") # O "violeta", según preferencia

        # Mezcla de un color consigo mismo (no cambia)
        elif self.name == other.name:
            return Color(self.name)

        # Si se mezcla con un color ya secundario o una combinación no definida
        # Podríamos devolver un color más oscuro o "marrón" o "negro"
        # Para este ejemplo, si no hay una regla específica, lo consideraremos "indefinido"
        else:
            return Color("color indefinido")

    def __repr__(self):
        return f"Color('{self.name}')"
    
    def __str__(self) -> str:
        return self.name


# Creamos algunas instancias de Color
azul = Color("azul")
amarillo = Color("amarillo")
rojo = Color("rojo")
verde = Color("verde")
naranja = Color("naranja")
morado = Color("morado")

print(f"Azul + Amarillo = {azul + amarillo}") # Output: Color('verde')
print(f"Rojo + Amarillo = {rojo + amarillo}") # Output: Color('naranja')
print(f"Azul + Rojo = {azul + rojo}")       # Output: Color('morado')
print(f"Verde + Azul = {verde + azul}")     # Output: Color('color indefinido') - No hay una regla simple para esto aquí
print(f"Rojo + Rojo = {rojo + rojo}")       # Output: Color('rojo')

try:
    print(f"Azul + 5 = {azul + 5}")
except TypeError as e:
    print(e) # Output: No se puede sumar un Color con un objeto de tipo int