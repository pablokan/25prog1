
class TemperaturaAmbiente:
    _temperatura_actual_celsius = 20.0
    _unidad_medida_preferida = "Celsius"

    @classmethod
    def establecer_temperatura_actual(cls, celsius_grados):
        if isinstance(celsius_grados, (int, float)):
            cls._temperatura_actual_celsius = celsius_grados

    @classmethod
    def cambiar_unidad_preferida(cls, unidad):
        if unidad in ["Celsius", "Fahrenheit"]:
            cls._unidad_medida_preferida = unidad

    @classmethod
    def obtener_temperatura_formateada(cls):
        if cls._unidad_medida_preferida == "Celsius":
            return f"{cls._temperatura_actual_celsius}°C"
        else:
            f = cls._temperatura_actual_celsius * 9/5 + 32
            return f"{f}°F"

    @classmethod
    def __str__(cls):
        return cls.obtener_temperatura_formateada()

# Pruebas
TemperaturaAmbiente.establecer_temperatura_actual(8)
print(TemperaturaAmbiente)
TemperaturaAmbiente.cambiar_unidad_preferida("Fahrenheit")
print(TemperaturaAmbiente)
