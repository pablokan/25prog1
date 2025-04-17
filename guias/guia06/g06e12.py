personas = [
    {'nombre': 'Juan', 'edad': 45, 'ciudad': 'Córdoba', 'profesion y años de experiencia': ['Ingeniero', 13]},
    {'nombre': 'Ana', 'edad': 35, 'ciudad': 'Río Cuarto', 'profesion y años de experiencia': ['Contadora', 10]},
    {'nombre': 'Luis', 'edad': 24, 'ciudad': 'San Luis', 'profesion y años de experiencia': ['Médico', 1]}
]

suma = 0
print('Los profesionales viven en las siguientes ciudades:')
for persona in personas:
    print(persona['ciudad'])
    suma += persona['profesion y años de experiencia'][1]
print(f'Promedio de años de experiencia: {suma/3}')


