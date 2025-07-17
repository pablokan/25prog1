import json

# Ejemplo de un diccionario
data = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Nueva York",
    "es_estudiante": False,
    "cursos": ["Matemáticas", "Historia", "Programación"],
    "direccion": {
        "calle": "Calle Falsa 123",
        "codigo_postal": "10001"
    }
}

print("Diccionario original:")
print(data)
print(f"Tipo de data: {type(data)}")

# Serializar el diccionario a una cadena JSON
# json.dumps() convierte un objeto Python (como un diccionario) en una cadena JSON.
# `indent` hace que la salida JSON sea más legible con sangría.
json_string = json.dumps(data, indent=4)

print("\nDiccionario serializado a JSON (cadena):")
print(json_string)
print(f"Tipo de json_string: {type(json_string)}")

# Deserializar la cadena JSON de vuelta a un objeto Python (diccionario)
# json.loads() convierte una cadena JSON en un objeto Python.
decoded_data = json.loads(json_string)

print("\nCadena JSON deserializada de vuelta a un diccionario:")
print(decoded_data)
print(f"Tipo de decoded_data: {type(decoded_data)}")

# Acceder a los datos del diccionario deserializado
print(f"\nAccediendo a datos deserializados:")
print(f"Nombre: {decoded_data['nombre']}")
print(f"Primer curso: {decoded_data['cursos'][0]}")
print(f"Calle: {decoded_data['direccion']['calle']}")

# Guardar el diccionario en un archivo JSON
file_name = "datos_ejemplo.json"
with open(file_name, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"\nDiccionario guardado en '{file_name}'")

# Cargar datos desde un archivo JSON
loaded_data = {}
try:
    with open(file_name, 'r') as json_file:
        loaded_data = json.load
        print(f"\nDatos cargados desde '{file_name}':")
        print(loaded_data)
        print(f"Tipo de loaded_data: {type(loaded_data)}")
        print(f"Nombre cargado: {loaded_data['nombre']}")
        print(f"Primer curso cargado: {loaded_data['cursos'][0]}")
        print(f"Calle cargada: {loaded_data['direccion']['calle']}")
except FileNotFoundError:
    print(f"El archivo '{file_name}' no fue encontrado.")
    loaded_data = {}
    print(f"Tipo de loaded_data: {type(loaded_data)}")
    print(f"Nombre cargado: {loaded_data.get('nombre', 'No encontrado')}")
    print(f"Primer curso cargado: {loaded_data.get('cursos', ['No encontrado'])[0]}")
    print(f"Calle cargada: {loaded_data.get('direccion', {}).get('calle', 'No encontrado')}")

    