
class Persona:
    def __init__(self, dni, nombre, apellido):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        
    def get_dni(self):
        return self.__dni

    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    def __str__(self):
        return f"Persona: {self.get_nombre_completo()} (DNI: {self.__dni})"

    def mostrar_datos(self):
        return f"Datos Personales: {self.get_nombre_completo()}, DNI: {self.get_dni()}"