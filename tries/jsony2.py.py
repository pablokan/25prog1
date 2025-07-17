import json

# Ejemplo de un diccionario
data = {
    "nombre": "Alice",
    "edad": 30,
    "altura": 1.75,
    "ciudad": "Nueva York",
    "es_estudiante": False,
    "cursos": ["Matemáticas", "Historia", "Programación"],
    "direccion": {
        "calle": "Calle Falsa 123",
        "codigo_postal": "10001",
        "piso": None
    }
}

print("Diccionario original:")
print(data)
print(f"Tipo de data: {type(data)}")

# Serializar el diccionario a una cadena JSON
# json.dumps() convierte un objeto Python (como un diccionario) en una cadena JSON.
# `indent` hace que la salida JSON sea más legible con sangría.
json_string = json.dumps(data, indent=4, ensure_ascii=False)

print("\nDiccionario serializado a JSON (cadena):")
print(json_string)
print(f"Tipo de json_string: {type(json_string)}")

lista = ['Juan', 'Ana', 'Joaquín', 'Luis']
json_string_lista = json.dumps(lista, indent=4, ensure_ascii=False)
print(json_string_lista)
print(type(json_string_lista))  
tupla = ('Juan', 'Ana', 'Joaquín', 'Luis')
json_string_tupla = json.dumps(tupla, indent=4, ensure_ascii=False)
print(json_string_tupla)
print(type(json_string_tupla))

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def accion(self):
        return f"{self.nombre} está hablando."

    def to_json(self):
        return json.dumps(self.__dict__, indent=4, ensure_ascii=False)

p: Persona = Persona('Carlos', 40)
print(f"\nObjeto Persona serializado a JSON:\n{p.to_json()}")
json_string_objeto = json.dumps(p.__dict__, indent=4, ensure_ascii=False)
print(json_string_objeto)



