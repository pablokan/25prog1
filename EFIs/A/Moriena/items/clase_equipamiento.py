# Importaciones 




#Clase Madre de Equipamientos --------------------------------------------------------------
class Equipamiento: #Clase madre para todo tipo de equipamiento (Arma, Casco, Pechera).
    def __init__(self, nombre: str, tier: int, tipo: str, estadisticas: dict):
        self._nombre = nombre
        self._tier = tier
        self._tipo = tipo  # 'Casco', 'Pechera', 'Arma'
        self._estadisticas = estadisticas # {'vida': 100, 'daño': 5, ...}

    # Getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def tier(self):
        return self._tier

    @property
    def tipo(self):
        return self._tipo

    @property
    def estadisticas(self):
        return self._estadisticas

    # Métodos
    def obtener_stats(self) -> str: #Devuelve un string con las estadísticas que proporciona el equipo.
        stats_str = ", ".join([f"+{v} {k.capitalize()}" for k, v in self.estadisticas.items() if v > 0])
        return f"{self.nombre} (Tier {self.tier}) - Tipo: {self.tipo}. Stats: {stats_str}"

    def __str__(self):
        stats_str = ", ".join([f"{k.capitalize()}:+{v}" for k, v in self.estadisticas.items() if v > 0])
        return f"{self.nombre} [T'{self.tier}', {self.tipo}] ({stats_str})"

# Clases Hijas de Equipamiento

class Casco(Equipamiento): # Equipamiento de tipo Casco, que otorga Vida (y opcionalmente otros stats).
    def __init__(self, nombre: str, tier: int, bonus_vida: int):
        # tier: 1 (base), 2, 3 (mejor)
        estadisticas = {'vida': bonus_vida}
        super().__init__(nombre, tier, "Casco", estadisticas)

class Pechera(Equipamiento): # Equipamiento de tipo Pechera, que otorga Vida (y opcionalmente otros stats).
    def __init__(self, nombre: str, tier: int, bonus_vida: int):
        # tier: 1 (base), 2, 3 (mejor)
        estadisticas = {'vida': bonus_vida}
        super().__init__(nombre, tier, "Pechera", estadisticas)

class Arma(Equipamiento): # Equipamiento de tipo Arma, que otorga Daño (y opcionalmente otros stats).
    def __init__(self, nombre: str, tier: int, bonus_daño: int):
        # tier: 1 (base), 2, 3 (mejor)
        estadisticas = {'daño': bonus_daño}
        super().__init__(nombre, tier, "Arma", estadisticas)
