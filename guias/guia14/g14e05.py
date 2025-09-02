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

# --- Clase hija BolsaPremium ---
class BolsaPremium(BolsaProductos):
    """
    Clase hija que hereda de BolsaProductos, con un costo extra por producto.
    """
    _costo_extra_por_producto = 2.50

    def obtener_costo_total(self):
        """
        Calcula y retorna el costo extra total de la bolsa premium.
        
        Returns:
            float: El costo extra total.
        """
        return len(self) * self._costo_extra_por_producto

# --- Ejemplo de uso ---

# Crear una instancia de BolsaPremium
mi_bolsa_premium = BolsaPremium()

# Agregar productos a la bolsa premium
mi_bolsa_premium.agregar_producto("Queso")
mi_bolsa_premium.agregar_producto("Vino")
mi_bolsa_premium.agregar_producto("Chocolate")

# Imprimir la bolsa completa y su costo total
print("--- Uso de la clase BolsaPremium ---")
print(mi_bolsa_premium)

costo_total = mi_bolsa_premium.obtener_costo_total()
print(f"El costo extra total de la bolsa premium es: {costo_total:.2f} USD")