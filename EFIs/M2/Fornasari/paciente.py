class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Paciente(Persona):
    def __init__(self, nombre, apellido, prioridad):
        super().__init__(nombre, apellido) 
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.prioridad})"

    @staticmethod
    def cargar_todos():
        pacientes = []
        try:
            with open("./pacientes.txt", "r") as file:
                for linea in file:
                    parts = linea.strip().split(",")
                    nombre = parts[0].strip()
                    apellido = parts[1].strip()
                    diagnostico = parts[2].strip()
                    paciente = Paciente(nombre, apellido, diagnostico)
                    pacientes.append(paciente)
        except Exception as e:
            print("Error al leer pacientes.txt:", e)
        return pacientes

    def clasificacion_emergencia(self):
        prioridad = self.prioridad.strip().lower()
        if prioridad == "rojo":
            return 1
        elif prioridad == "naranja":
            return 2
        elif prioridad == "amarillo":
            return 3
        elif prioridad == "verde":
            return 4
        elif prioridad == "azul":
            return 5
        else:
            return -1
