# persona = {}
# persona['nombre'] = 'juan'
# persona['edad'] = 22
# persona['ciudad'] = 'San Luis'
#print(persona)
#persona = {'nombre': 'juan', 'edad': 22, 'ciudad': 'San Luis'}

#Dado el diccionario persona creado en el ejercicio número 1, sumale 10 a la edad 
# y agrega una nueva clave "profesion y años de experiencia" 
# con los valores Ingeniero para profesión y 13 para los años de experiencia. 
# Muestra el diccionario actualizado.

# Sumo 10 a la edad
#persona['edad'] += 10
#print(persona)
#persona["profesion y años de experiencia"] = ['ingeniero', 5]
#print(persona)
# {'nombre': 'juan', 'edad': 32, 'ciudad': 'San Luis', 'profesion y años de experiencia': ['ingeniero', 5]}

personas = [
    {'nombre': 'juan', 'edad': 32, 'ciudad': 'San Luis', 'profesion y años de experiencia': ['ingeniero', 5]},
    {'nombre': 'ana', 'edad': 34, 'ciudad': 'Córdoba', 'profesion y años de experiencia': ['contadora', 2]},
    {'nombre': 'pedro', 'edad': 63, 'ciudad': 'Río Cuarto', 'profesion y años de experiencia': ['plomero', 29]},
]

total = 0
print('Las ciudades donde viven los profesionales son:')
for persona in personas:
    print(persona['ciudad'])
    prof, antig = persona['profesion y años de experiencia']
    total += antig
print()
print(f'El promedio de antiguedad es {total/len(personas)}')
