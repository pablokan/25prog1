class Color:
    # Una tabla (diccionario) con algunos nombres de colores comunes y sus valores hexadecimales RGB.
    # Nota: Esta es una lista limitada; existen miles de colores nombrados.
    NAMED_COLORS = {
        "negro": "000000",
        "blanco": "FFFFFF",
        "rojo": "FF0000",
        "verde": "00FF00",
        "azul": "0000FF",
        "amarillo": "FFFF00",  # Rojo + Verde = Amarillo (aditivo)
        "magenta": "FF00FF",  # Rojo + Azul = Magenta (aditivo)
        "cian": "00FFFF",     # Verde + Azul = Cian (aditivo)
        "gris": "808080",
        "naranja": "FFA500",
        "purpura": "800080",
        "oro": "FFD700",
        "plata": "C0C0C0"
    }

    # Creamos un mapeo inverso para buscar el nombre por el valor hexadecimal
    _HEX_TO_NAME = {v: k for k, v in NAMED_COLORS.items()}

    def __init__(self, hex_code):
        """
        Inicializa un color con su código hexadecimal RGB.
        El código debe ser una cadena de 6 caracteres (ej. "FF0000").
        """
        if not isinstance(hex_code, str) or len(hex_code) != 6:
            raise ValueError("El código hexadecimal debe ser una cadena de 6 caracteres.")
        
        self._hex_code = hex_code.upper() # Almacenamos en mayúsculas para consistencia
        self._rgb = self._hex_to_rgb(self._hex_code)

    @property
    def hex(self):
        """Retorna el código hexadecimal del color."""
        return self._hex_code

    @property
    def rgb(self):
        """Retorna la tupla RGB (r, g, b) del color."""
        return self._rgb

    @property
    def name(self):
        """
        Retorna el nombre del color si está en la tabla de colores conocidos,
        de lo contrario retorna None.
        """
        return self._HEX_TO_NAME.get(self._hex_code)

    def _hex_to_rgb(self, hex_str):
        """Convierte una cadena hexadecimal RGB a una tupla (r, g, b)."""
        r = int(hex_str[0:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:6], 16)
        return (r, g, b)

    def _rgb_to_hex(self, rgb_tuple):
        """Convierte una tupla (r, g, b) a una cadena hexadecimal RGB."""
        r, g, b = rgb_tuple
        # Formatea cada componente como dos dígitos hexadecimales en mayúsculas
        return f"{r:02X}{g:02X}{b:02X}"

    def __add__(self, other):
        """
        Define la operación de suma aditiva de colores RGB.
        Cada componente se suma y se "clipea" (limita) a 255 (FFh).
        """
        if not isinstance(other, Color):
            raise TypeError(f"No se puede sumar un Color con un objeto de tipo {type(other).__name__}")

        r1, g1, b1 = self._rgb
        r2, g2, b2 = other._rgb

        # Suma los componentes y asegúrate de que no excedan 255
        new_r = min(255, r1 + r2)
        new_g = min(255, g1 + g2)
        new_b = min(255, b1 + b2)

        new_hex_code = self._rgb_to_hex((new_r, new_g, new_b))
        return Color(new_hex_code)

    def __str__(self):
        """Representación amigable del objeto Color."""
        name_info = f" ({self.name})" if self.name else ""
        return f"Color(Hex: #{self.hex}, RGB: {self.rgb}{name_info})"

    def __repr__(self):
        """Representación para desarrolladores."""
        return f"Color('{self.hex}')"

# --- EJEMPLOS DE USO ---

print("--- Colores Primarios Aditivos ---")
red = Color("FF0000")
green = Color("00FF00")
blue = Color("0000FF")

print(f"Rojo: {red}")
print(f"Verde: {green}")
print(f"Azul: {blue}")

print("\n--- Suma de Colores (Aditiva) ---")
# Rojo + Verde = Amarillo
red_plus_green = red + green
print(f"{red} + {green} = {red_plus_green}") # Salida: Color(Hex: #FFFF00, RGB: (255, 255, 0) (amarillo))

# Rojo + Azul = Magenta
red_plus_blue = red + blue
print(f"{red} + {blue} = {red_plus_blue}")   # Salida: Color(Hex: #FF00FF, RGB: (255, 0, 255) (magenta))

# Verde + Azul = Cian
green_plus_blue = green + blue
print(f"{green} + {blue} = {green_plus_blue}") # Salida: Color(Hex: #00FFFF, RGB: (0, 255, 255) (cian))

# Rojo + Verde + Azul = Blanco
white = red + green + blue
print(f"{red} + {green} + {blue} = {white}") # Salida: Color(Hex: #FFFFFF, RGB: (255, 255, 255) (blanco))

print("\n--- Sumas con Intensidades Reducidas ---")
# Un rojo más oscuro (mitad de intensidad)
dark_red = Color("800000") # 128 en decimal
light_green = Color("00FF00")

sum_dark_red_light_green = dark_red + light_green
print(f"{dark_red} + {light_green} = {sum_dark_red_light_green}")
# Expected: (128+0, 0+255, 0+0) = (128, 255, 0) -> #80FF00

# Suma que excede 255 (se clipea a 255)
brighter_red = Color("C00000") # 192 en decimal
another_brighter_red = Color("C00000") # 192 en decimal
sum_brighter_red = brighter_red + another_brighter_red
print(f"{brighter_red} + {another_brighter_red} = {sum_brighter_red}")
# Expected: (192+192, 0+0, 0+0) = (384, 0, 0) -> Clipped to (255, 0, 0) -> #FF0000

print("\n--- Ejemplos de Búsqueda por Nombre ---")
my_yellow = Color.NAMED_COLORS["amarillo"] # Accedemos al hex desde la tabla
yellow_color_obj = Color(my_yellow)
print(f"El color 'amarillo' es: {yellow_color_obj}")
print(f"¿Es un color conocido? {yellow_color_obj.name}")

unknown_color = Color("123456")
print(f"Color desconocido: {unknown_color}")
print(f"¿Es un color conocido? {unknown_color.name}")

print("\n--- Manejo de Errores ---")
try:
    invalid_color = Color("ABC")
except ValueError as e:
    print(f"Error al crear color: {e}")

try:
    result = red + "not a color"
except TypeError as e:
    print(f"Error al sumar: {e}")

