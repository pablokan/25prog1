from .persona import Persona

class Paciente(Persona):
    def __init__(self, dni, nombre, apellido, telefono, id_bd=None):

        super().__init__(dni, nombre, apellido)
        self.__telefono = telefono 
        self.id_bd = id_bd 
        
    def get_telefono(self):
        return self.__telefono

    def mostrar_datos(self):
        datos_base = super().mostrar_datos()
        return f"{datos_base}, Teléfono: {self.get_telefono()}"