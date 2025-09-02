class Auto:
    def __init__(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio

    def __str__(self):
        return f"Auto: {self._marca} {self._modelo}, del año {self._anio}"

class AutoElectrico(Auto):
    def __init__(self, marca, modelo, anio, tiempo_carga):
        super().__init__(marca, modelo, anio)
        self._tiempo_carga = tiempo_carga

    @property
    def tiempo_carga(self):
        return self._tiempo_carga

    @tiempo_carga.setter
    def tiempo_carga(self, tiempo_carga):
        self._tiempo_carga = tiempo_carga

    def __str__(self):
        return f"Auto eléctrico: {self._marca} {self._modelo}, del año {self._anio}, requiere {self._tiempo_carga} horas para carga completa."

# Demostración
mi_auto = AutoElectrico("Honda", "Modelo-X", 2023, 4)
print(mi_auto)