class Color:
    def __init__(self, nombre):
        self.nombre = nombre

    def __add__(self, otro_color):
        if (self.nombre == "azul" and otro_color.nombre == "rojo"):
            return Color("violeta")
        else:
            return Color('desconocido')
        
    def __repr__(self) -> str:
        return f'Clase: {self.__class__.__name__}, Nombre: {self.nombre}'
    
    def __str__(self) -> str:
        return self.nombre
    
azul = Color("azul")
amarillo = Color("amarillo")
rojo = Color("rojo")

print(azul + amarillo)
print(rojo + amarillo)
print(azul + rojo)
otro = azul + rojo
print(otro)
print(repr(otro))