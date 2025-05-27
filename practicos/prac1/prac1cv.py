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

fechas_nacimientos = [
    '15/05/1943',
    '07/04/1984',
    '10/02/1971',
    '21/12/1967',
    '30/01/1982',
    '30/08/1995',
    '18/07/1959'
]

# Atención! No caer en la tentación de poner literales enteros (por ejemplo, ahhh, la coma está en la posición 6)

# pos_coma = nombre_completo.find(',')
# apellido = nombre_completo[:pos_coma]
# nombre = nombre_completo[pos_coma+2:]
# print(apellido, nombre)

for nombre_completo in nombres_completos:
    #nombre_completo = 'Torres, Ana' # A. Torres
    apellido, nombre = nombre_completo.split(', ')
    inicial = nombre[0]
    nombre_salida = f'{inicial}. {apellido}'
    print(nombre_salida)

nombre_mas_largo = ''
for nombre_completo in nombres_completos:
    _, nombre = nombre_completo.split(', ')
    if len(nombre) > len(nombre_mas_largo):
        nombre_mas_largo = nombre
print(nombre_mas_largo)

dh = 13
mh = 5
ah = 2025
total_edades_logistica = 0
contador_logistica = 0
for i in range(len(departamentos)):
    if departamentos[i] == 'Logística':
        contador_logistica += 1
        fecha = fechas_nacimientos[i]
        # dn = int(fecha[:2])
        # mn = int(fecha[3:5])
        # an = int(fecha[6:])
        dn, mn, an = [int(n) for n in fecha.split('/')]
        edad = ah - an
        if (mn > mh) or (mn == mh and dn > dh):
            edad -= 1
        total_edades_logistica += edad
print(total_edades_logistica // contador_logistica)