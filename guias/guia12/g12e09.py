class BolsaProductos:
    """
    Clase para representar una bolsa de productos.
    """
    def __init__(self):
        """Inicializa una nueva bolsa de productos."""
        self.nombres_productos = []

    def agregar_producto(self, nombre):
        """
        Agrega un producto a la bolsa.
        
        Args:
            nombre (str): El nombre del producto a agregar.
        """
        self.nombres_productos.append(nombre)

    def __len__(self):
        """
        Retorna la cantidad de productos en la bolsa.
        
        Permite usar la función len() en una instancia de la clase.
        """
        return len(self.nombres_productos)

    def __getitem__(self, indice):
        """
        Permite acceder a un producto por su índice.
        
        Args:
            indice (int): El índice del producto a obtener.
            
        Returns:
            str: El nombre del producto en el índice especificado.
        """
        return self.nombres_productos[indice]

    def __str__(self):
        """
        Retorna una representación en string de la bolsa de productos.
        
        Permite usar la función print() en una instancia de la clase.
        """
        return f"Bolsa con: {', '.join(self.nombres_productos)}"

# --- Ejemplo de uso ---

# Crear una instancia de BolsaProductos
mi_bolsa = BolsaProductos()

# Agregar algunos productos
mi_bolsa.agregar_producto("Leche")
mi_bolsa.agregar_producto("Pan")
mi_bolsa.agregar_producto("Huevos")
mi_bolsa.agregar_producto("Manzanas")

print("--- Uso de la clase BolsaProductos ---")

# Usar len() para obtener la cantidad de productos
print(f"Cantidad de productos en la bolsa: {len(mi_bolsa)}")

# Acceder a un producto por su índice
producto_en_indice_2 = mi_bolsa[2]
print(f"Producto en el índice 2: {producto_en_indice_2}")

# Imprimir la bolsa completa usando __str__
print(mi_bolsa)