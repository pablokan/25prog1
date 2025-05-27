rank = [i for i in range(1,6)]
nac_varones_18 = [
    ["Liam",19837],
    ["Noah",18267],
    ["Michael",14516],
    ["James",13525],
    ["Oliver",13389]
    ]
nac_mujeres_18 = [
    ["Emma",18688],
    ["Olivia",17921],
    ["Ava",14924],
    ["Isabella",14464],
    ["Sophia",13928]]

nac_2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
nac_varones_08 = []
nac_mujeres_08 = []

nac_2008 = nac_2008.split(',')

for i in range(len(nac_2008)):
    if nac_2008[i] == 'f':
        nac_mujeres_08.append([nac_2008[i-2],int(nac_2008[i-1])])
    elif nac_2008[i] == 'm':
        nac_varones_08.append([nac_2008[i-2],int(nac_2008[i-1])])
        
nac_varones_08.sort(key=lambda x: x[1], reverse=True)
nac_mujeres_08.sort(key=lambda x: x[1], reverse=True)
        
# Diferencia en cantidad de nacimientos
print('DIFERENCIA EN RANKING DE NOMBRES')
posicion = int(input('Indica posicion: '))
sexo = input('Seleccione sexo (f/m): ').lower()
indice = posicion - 1
diferencia = 0
if sexo == 'm':
    if nac_varones_18[indice][1] > nac_varones_08[indice][1]:
        diferencia = nac_varones_18[indice][1] - nac_varones_08[indice][1]
        nom18 = nac_varones_18[indice][0]
        nom08 = nac_varones_08[indice][0]
        mensaje = f'Varones en posición #{posicion}: en 2018 hubo {diferencia} mas inscriptos ({nom18}) que el {posicion} de 2008 ({nom08})'
        print(mensaje)
    elif nac_varones_18[indice][1] == nac_varones_08[indice][1]:
        nom18 = nac_varones_18[indice][0]
        nom08 = nac_varones_08[indice][0]
        mensaje = f'Varones en posición #{posicion}: en 2018 hubo la misma cantidad de inscriptos ({nom18}) que en la misma posicion {posicion} del 2008 ({nom08})'
        print(mensaje)
    else:
        nom18 = nac_varones_18[indice][0]
        nom08 = nac_varones_08[indice][0]
        diferencia = nac_varones_08[indice][1] - nac_varones_18[indice][1]
        mensaje = f'Varones en posición #{posicion}: en 2018 hubo {diferencia} menos inscriptos ({nom18}) que el {posicion} de 2008 ({nom08})'
        print(mensaje)

if sexo == 'f':
    if nac_mujeres_18[indice][1] > nac_mujeres_08[indice][1]:
        diferencia = nac_mujeres_18[indice][1] - nac_mujeres_08[indice][1]
        nom18 = nac_mujeres_18[indice][0]
        nom08 = nac_mujeres_08[indice][0]
        mensaje = f'Mujeres en posición #{posicion}: en 2018 hubo {diferencia} mas inscriptos ({nom18}) que el {posicion} de 2008 ({nom08})'
        print(mensaje)
    elif nac_mujeres_18[indice][1] == nac_mujeres_08[indice][1]:
        nom18 = nac_mujeres_18[indice][0]
        nom08 = nac_mujeres_08[indice][0]
        mensaje = f'Mujeres en posición #{posicion}: en 2018 hubo la misma cantidad de inscriptos ({nom18}) que en la misma posicion {posicion} del 2008 ({nom08})'
        print(mensaje)
    else:
        nom18 = nac_mujeres_18[indice][0]
        nom08 = nac_mujeres_08[indice][0]
        diferencia = nac_mujeres_08[indice][1] - nac_mujeres_18[indice][1]
        mensaje = f'Mujeres en posición #{posicion}: en 2018 hubo {diferencia} menos inscriptos ({nom18}) que el {posicion} de 2008 ({nom08})'
        print(mensaje)
print('\n')

# nombres que cominezan con letra elegida
print('NOMBRES CON LA MISMA LETRA INICIAL')
letra_inicial = input('Ingrese letra: ').upper()
nombres = []
for m , a in nac_varones_18:
    if m[0] == letra_inicial:
        if m not in nombres:
            nombres.append(m)
for m , a in nac_varones_08:
    if m[0] == letra_inicial:
        if m not in nombres:
            nombres.append(m)
for f , a in nac_mujeres_18:
    if f[0] == letra_inicial:
        if f not in nombres:
            nombres.append(f)
for f , a in nac_mujeres_08:
    if f[0] == letra_inicial:
        if f not in nombres:
            nombres.append(f)
nombres.sort()
if nombres == []:
    mensaje = f"No se encontraron nombres con la letra {letra_inicial}"
    print(mensaje)
else:
    mensaje = f'Los nombres que empiezan con {letra_inicial} son:'
    print(mensaje)
    for nombre in nombres:
        print(nombre, end=' ')
        
print('\n')

# Nombres que se repiten en cada año
print('NOMBRES REPETIDOS')
print("Los nombres repetidos en ambos años son:")
nombres_repetidos = []
nombres_2018 = []
for m , a in nac_varones_18:
    nombres_2018.append(m)
for f , a in nac_mujeres_18:
    nombres_2018.append(f)
    
for n , a in nac_varones_08:
    if n in nombres_2018:
        nombres_repetidos.append(n)
        
for n , a in nac_mujeres_08:
    if n in nombres_2018:
        nombres_repetidos.append(n)

nombres_repetidos.sort()        
for nom in nombres_repetidos:
    print(nom, end=' ')