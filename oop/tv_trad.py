class Producto:
    def __init__(self, nombre, cantidad_inicial):
        self.nombre = nombre
        self.cantidad = cantidad_inicial

    @property
    def cantidad(self):
        """Este es el 'getter'. Se ejecuta al leer 'objeto.cantidad'."""
        # El atributo real se guarda con un guion bajo por convención (_cantidad)
        return self._cantidad

    @cantidad.setter
    def cantidad(self, nuevo_valor):
        """Este es el 'setter'. Se ejecuta al asignar 'objeto.cantidad = valor'."""
        print(f"-> Intentando cambiar la cantidad a {nuevo_valor}...")
        if nuevo_valor < 0:
            # 1. VALIDACIÓN: El objeto se protege a sí mismo.
            raise ValueError("La cantidad no puede ser negativa.")
        
        # 2. LÓGICA ADICIONAL: Podemos hacer más cosas aquí.
        # Por ejemplo, podríamos registrar el cambio en un log.
        print("   ¡Cantidad actualizada correctamente!")
        
        self._cantidad = nuevo_valor

# --- Veamos cómo funciona ahora ---

# La creación sigue siendo limpia y ahora es segura
producto_tv = Producto("Televisor 4K", 10)
# >> -> Intentando cambiar la cantidad a 10...
# >>    ¡Cantidad actualizada correctamente!

# El acceso para lectura es idéntico
print(f"Hay {producto_tv.cantidad} televisores.")
# >> Hay 10 televisores.

# Intentemos asignar un valor inválido
try:
    producto_tv.cantidad = -5
except ValueError as e:
    print(f"ERROR: {e}")
# >> -> Intentando cambiar la cantidad a -5...
# >> ERROR: La cantidad no puede ser negativa.

# El estado del objeto se mantuvo íntegro
print(f"La cantidad sigue siendo {producto_tv.cantidad}.")
# >> La cantidad sigue siendo 10.