
class ConfiguracionApp:
    _modo_depuracion = False
    _log_activo = True
    _version = "1.0.0"

    @classmethod
    def set_modo_depuracion(cls, valor):
        if isinstance(valor, bool):
            cls._modo_depuracion = valor

    @classmethod
    def get_modo_depuracion(cls):
        return cls._modo_depuracion
    
    # ... (getters y setters para log_activo y getter para version)

# Pruebas
print(f"Modo depuración: {ConfiguracionApp.get_modo_depuracion()}")
ConfiguracionApp.set_modo_depuracion(True)
print(f"Modo depuración: {ConfiguracionApp.get_modo_depuracion()}")