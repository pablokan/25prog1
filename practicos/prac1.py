# 17:54
# 18:02 
# 18:05
# 18:13

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
    'Desarrollo'
]

fechas_nacimiento = [
    '15/05/1943',
    '07/04/1984',
    '10/02/1971',
    '21/12/1967',
    '30/01/1982',
    '30/08/1995',
    '18/07/1959'
]

# 1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
print()
print('1) Nombres de las personas:')
for nombre_completo in nombres_completos:
    pos_coma = nombre_completo.find(', ')
    nombre_pila = nombre_completo[pos_coma+2:]
    apellido = nombre_completo[:pos_coma]
    print(f'{nombre_pila[0]}. {apellido}')

print()
print('2) Nombre de pila más largo:')
nombre_mas_largo = ''
for nombre_completo in nombres_completos:
    pos_coma = nombre_completo.find(', ')
    nombre_pila = nombre_completo[pos_coma+2:]
    if len(nombre_pila) > len(nombre_mas_largo):
        nombre_mas_largo = nombre_pila
print(nombre_mas_largo)

print()
total = 0
cantidad_personas_logistica = 0
promedio_edad_logistica = 0
for i in range(len(departamentos)):
    if departamentos[i] == 'Logística':
        cantidad_personas_logistica += 1
        dn, mn, an = [int(n) for n in fechas_nacimiento[i].split('/')]
        dh, mh, ah = 1, 5, 2025
        edad = ah - an
        if (mn > mh) or (mn == mh and dn > dh):
            edad -= 1
        total += edad
        promedio_edad_logistica = total // cantidad_personas_logistica


print(f'3) El promedio de edad de las personas del Departamento de Logística es de  {promedio_edad_logistica} años')