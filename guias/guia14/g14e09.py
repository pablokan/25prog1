""" 
# Paso 1: Creación de Clases
class Profesor:
    def __init__(self, nombre, dni, materia):
        self._nombre = nombre
        self._dni = dni
        self._materia = materia

    def __str__(self):
        return f"Profesor: {self._nombre}, DNI: {self._dni}, Materia: {self._materia}"

class Alumno:
    def __init__(self, nombre, dni, notas):
        self._nombre = nombre
        self._dni = dni
        self._notas = notas

    def obtener_promedio(self):
        if not self._notas:
            return 0
        return sum(self._notas) / len(self._notas)
"""
# Paso 2: Generalización
class Persona:
    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni

class Profesor(Persona):
    def __init__(self, nombre, dni, materia):
        super().__init__(nombre, dni)
        self._materia = materia

    def __str__(self):
        return f"Profesor: {self._nombre}, DNI: {self._dni}, Materia: {self._materia}"

class Alumno(Persona):
    def __init__(self, nombre, dni, notas):
        super().__init__(nombre, dni)
        self._notas = notas

    def obtener_promedio(self):
        if not self._notas:
            return 0
        return sum(self._notas) / len(self._notas)

# Pruebas
profesor_ejemplo = Profesor("Pablo", "12345678", "Programación")
print(profesor_ejemplo)
alumno_ejemplo = Alumno("Micaela", "87654321", [8, 9, 7])
print(f"Promedio del alumno: {alumno_ejemplo.obtener_promedio()}")