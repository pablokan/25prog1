from .alumno import *
class Actividad:

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.alumnos = []


    #getters y setters
    @property
    def nombre(self) -> str:
    
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
       
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre de la actividad debe ser un texto no vacío.")
        self._nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if not isinstance(valor, (int, float)):
            raise TypeError("El precio debe ser un valor numérico .")
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = float(valor)


    
    #métodos de gestión de alumnos
    
    def inscribir_alumno(self, alumno: Alumno):
        
        if not isinstance(alumno, Alumno):
            print(f"Error: el item '{alumno}' no es un objeto de tipo alumno.")
            return

       
        if alumno in self.alumnos:
            print(f"Error: {alumno.nombre} (DNI: {alumno.dni}) ya está inscripto en {self.nombre}.")
        else:
            self.alumnos.append(alumno)
            print(f"Éxito: {alumno.nombre} ha sido inscripto en {self.nombre}.")

    def quitar_alumno(self, alumno: Alumno):
        
        if not isinstance(alumno, Alumno):
            print(f"Error: el item '{alumno}' no es un objeto de tipo alumno.")
            return
       
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            print(f"Éxito: {alumno.nombre} ha sido quitado de {self.nombre}.")
        else:
            print(f"Error: {alumno.nombre} (DNI: {alumno.dni}) no está inscripto en {self.nombre}.")
