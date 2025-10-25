# Importaciones 




#Clase Madre de Pociones --------------------------------------------------------------

class Pociones:
    """Clase madre para todas las pociones."""
    def __init__(self, nombre: str, tipo_efecto: str, cantidad: int):
        self._nombre = nombre
        self._tipo_efecto = tipo_efecto  # 'Vida', 'Stamina', 'Daño'
        self._cantidad = cantidad

    # Getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo_efecto(self):
        return self._tipo_efecto

    @property
    def cantidad(self):
        return self._cantidad

    #Metodos--------------------------------------
    def consumir_pocion(self, personaje: object) -> str: # Aplica el efecto de la poción al personaje.

        if self.tipo_efecto == "Vida":
            # se accede directamente al atributo 'vida' con un setter que verifica límites.
            personaje.vida += self.cantidad
            return f"{personaje.nombre} consume {self.nombre}. Recupera {self.cantidad} de Vida."
        
        elif self.tipo_efecto == "Stamina":
            personaje.stamina += self.cantidad
            return f"{personaje.nombre} consume {self.nombre}. Recupera {self.cantidad} de Stamina."
        
        elif self.tipo_efecto == "Daño":
            # Efecto temporal: Podría implementarse como un aumento de daño por un turno.
            return f"{personaje.nombre} consume {self.nombre}. Aumenta el Daño en {self.cantidad} por un tiempo."
            
        else:
            return f"Efecto de poción desconocido: {self.tipo_efecto}"


    def __str__(self):
        return f"{self.nombre} ({self.tipo_efecto}: +{self.cantidad})"

# Clases Hijas de Pociones --------------------------------------------------------------

class PocionVida(Pociones): # Poción que recupera Vida.
    def __init__(self, nivel: int):
        # Nivel 1: +30, Nivel 2: +60, Nivel 3: +100
        cantidad_vida = {1: 30, 2: 60, 3: 100}.get(nivel, 30)
        nombre_pocion = f"Poción de Vida (Nvl {nivel})"
        super().__init__(nombre_pocion, "Vida", cantidad_vida)

class PocionStamina(Pociones):
    """Poción que recupera Stamina."""
    def __init__(self, nivel: int):
        # Nivel 1: +20, Nivel 2: +40, Nivel 3: +70
        cantidad_stamina = {1: 20, 2: 40, 3: 70}.get(nivel, 20)
        nombre_pocion = f"Poción de Stamina (Nvl {nivel})"
        super().__init__(nombre_pocion, "Stamina", cantidad_stamina)

class PocionFuerza(Pociones):
    """Poción que aumenta el Daño (Fuerza) temporalmente."""
    def __init__(self, nivel: int):
        # Nivel 1: +5, Nivel 2: +10, Nivel 3: +15
        cantidad_daño = {1: 5, 2: 10, 3: 15}.get(nivel, 5)
        nombre_pocion = f"Poción de Fuerza (Nvl {nivel})"
        super().__init__(nombre_pocion, "Daño", cantidad_daño)
        