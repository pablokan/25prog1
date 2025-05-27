nacidos2008="Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
# Separo la cadena por comas, agrupo de a 3 y ordeno por nro de nacimientos decrec.
nacidos2008separados = nacidos2008.split(',')
nacidos2008ordenados =[]
for i in range(10):
    nacidos2008ordenados.append(nacidos2008separados[i*3:i*3+3])
nacidos2008ordenados.sort(reverse=True, key=lambda nacimientos: nacimientos[1])
# Separo en dos listas segun sexo
nacidos2008m = []
nacidos2008f = []
for nacidos in nacidos2008ordenados:
    if nacidos[2] == 'm':
        nacidos2008m.append(nacidos)
    else:
        nacidos2008f.append(nacidos)
nacidos2018 = {
    1: {"m": {"nombre": "Liam", "cantidad": 19837},
        "f": {"nombre": "Emma", "cantidad": 18688}},
    2: {"m": {"nombre": "Noah", "cantidad": 18267},
        "f": {"nombre": "Olivia", "cantidad": 17921}},
    3: {"m": {"nombre": "Michael", "cantidad": 14516},
        "f": {"nombre": "Ava", "cantidad": "14924"}},
    4: {"m": {"nombre": "James", "cantidad": 13525},
        "f": {"nombre": "Isabella", "cantidad": 14464}},
    5: {"m": {"nombre": "Oliver", "cantidad": 13389},
        "f": {"nombre": "Sophia", "cantidad": 13928}}
}
# 1) Diferencia entre nombres en la misma posicion y sexo
posicion = input('\nIngrese la posición(1 al 5) del nombre que desea comparar: ')
posicion = int(posicion)
sexo = input('\nIngrese el sexo del nombre (m/f): ')
if sexo == 'm':
    m2008 = int(nacidos2008m[posicion-1][1])
    m2018 = nacidos2018[posicion][sexo]["cantidad"]
    if m2008 > m2018:
        diferencia = m2008 - m2018
        print(f'\nVarones en posición #{posicion}: El nombre {nacidos2008m[posicion-1][0]} (2008) tiene una diferencia de {diferencia} sobre el nombre {nacidos2018[posicion][sexo]["nombre"]} (2018)')
    else:
        diferencia = m2018 - m2008
        print(f'\nVarones en posición #{posicion}: El nombre {nacidos2018[posicion][sexo]["nombre"]} (2018) tiene una diferencia de {diferencia} sobre el nombre {nacidos2008m[posicion-1][0]} (2008)')
else:
    f2008 = int(nacidos2008f[posicion-1][1])
    f2018 = nacidos2018[posicion][sexo]["cantidad"]    
    if f2008 > f2018:
        diferencia = f2008 - f2018
        print(f'\nMujeres en posición #{posicion}: El nombre {nacidos2008f[posicion-1][0]} (2008) tiene una diferencia de {diferencia} sobre el nombre {nacidos2018[posicion][sexo]["nombre"]} (2018)')
    else:
        diferencia = f2018 - f2008
        print(f'\nMujeres en posición #{posicion}: El nombre {nacidos2018[posicion][sexo]["nombre"]} (2018) tiene una diferencia de {diferencia} sobre el nombre {nacidos2008f[posicion-1][0]} (2008)')
# 2) Nombres con la misma inicial
print('\nAhora verificamos los nombres que comiencen por la misma letra.')
inicial = input('\nIngrese una letra en mayuscula: ')
iniciales = []
for i in range(5):
    iniciales.append(nacidos2018[i+1]["m"]["nombre"][0])
    iniciales.append(nacidos2018[i+1]["f"]["nombre"][0])
    iniciales.append(nacidos2008m[i][0][0])
    iniciales.append(nacidos2008f[i][0][0])
if inicial in iniciales:
    nombres = []
    print(f'\nNombres que comienzan con {inicial}:', end = " ")
    for i in range(5):
        if inicial == nacidos2008m[i][0][0] and nacidos2008m[i][0] not in nombres:
            nombres.append(nacidos2008m[i][0])
        if inicial == nacidos2008f[i][0][0] and nacidos2008f[i][0] not in nombres:
            nombres.append(nacidos2008f[i][0])
        if inicial == nacidos2018[i+1]["m"]["nombre"][0] and nacidos2018[i+1]["m"]["nombre"] not in nombres:
            nombres.append(nacidos2018[i+1]["m"]["nombre"])
        if inicial == nacidos2018[i+1]["f"]["nombre"][0] and nacidos2018[i+1]["f"]["nombre"] not in nombres:
            nombres.append(nacidos2018[i+1]["f"]["nombre"])
    for nombre in nombres:
        print(nombre, end = " ")
    print("\n")
else:
    print('\nNo hay nombres guardados que comiencen con esa letra.\n')
# 3) Nombres que se repiten
print('Los nombres que se repiten son:', end = ' ')
for x in range(5):
    for y in range(5):
        if nacidos2008m[x][0] == nacidos2018[y+1]["m"]["nombre"]:
            print(nacidos2008m[x][0], end = ' ')
        if nacidos2008f[x][0] == nacidos2018[y+1]["f"]["nombre"]:
            print(nacidos2008f[x][0], end = ' ')
print('\n')
