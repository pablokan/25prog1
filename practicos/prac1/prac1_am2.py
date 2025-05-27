nombres_completos = [
    'Torres, Ana',
    'Hudson, Kate',
    'Quesada, Benicio',
    'Campoamores, Susana', 
    'Santamaría, Carlos',
    'Skarsgard, Azul',
    'Catalejos, Walter'
]

departamentos = [
    'Logística',
    'Desarrollo',
    'Desarrollo',
    'Logística',
    'Administración',
    'Logística',
    'Desarrollo',
]

fechas_nacimiento = [
    '16/05/1943',
    '07/04/1984',
    '10/02/1971',
    '21/12/1967',
    '30/01/1982',
    '30/08/1995',
    '18/07/1959'
]
print('1) Iniciales y apellido de las personas: ')
for nombre_completo in nombres_completos:
    pos_coma = nombre_completo.find(',')
    apellido = nombre_completo[:pos_coma]
    inicial = nombre_completo[pos_coma+2]
    nombre_salida = f'{inicial}. {apellido}'
    print(nombre_salida)
print()

print('2) El nombre más largo es: ')
nombre_mas_largo = ''
for nombre_completo in nombres_completos:
    _, nombre = nombre_completo.split(', ')
    if len(nombre) > len(nombre_mas_largo):
        nombre_mas_largo = nombre
print(nombre_mas_largo)
print()

print('3) El promedio de edad de las personas del Departamento de Logística es de', end=' ')
total_edades_logistica = 0
contador_logistica = 0
for i in range(len(departamentos)):
    departamento = departamentos[i]
    fecha = fechas_nacimiento[i]

    if departamento == 'Logística':
        contador_logistica += 1
        dh = 15
        mh = 5
        ah = 2025
        dn = int(fecha[:2])
        mn = int(fecha[3:5])
        an = int(fecha[6:])

        edad = ah - an
        if (mn > mh) or (mn == mh and dn > dh):
            edad -= 1 # edad = edad - 1
        total_edades_logistica += edad
print(total_edades_logistica // contador_logistica)
