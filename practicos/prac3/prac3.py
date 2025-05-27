nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

nombres_08f = []
nombres_08m = []
cantidades_08f = []
cantidades_08m = []

lista_nacidos2008 = nacidos2008.split(',')

for i in range(len(lista_nacidos2008)):
    if lista_nacidos2008[i] == 'f':
        nombres_08f.append(lista_nacidos2008[i-2])
        cantidades_08f.append(int(lista_nacidos2008[i-1]))
    elif lista_nacidos2008[i] == 'm':
        nombres_08m.append(lista_nacidos2008[i-2])
        cantidades_08m.append(int(lista_nacidos2008[i-1]))

datos_08f = list(zip(cantidades_08f, nombres_08f))
datos_08m = list(zip(cantidades_08m, nombres_08m))
datos_08f.sort(reverse=True)
datos_08m.sort(reverse=True)
print(datos_08f)
print(datos_08m)

#[(18813, 'Emma'), (18616, 'Julia'), (17434, 'Emily'), (17081, 'Olivia'), (17039, 'Eva')]
#[(22594, 'Jacob'), (20626, 'Michael'), (20216, 'Ethan'), (19205, 'Joshua'), (19005, 'Daniel')]
# ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia']
datos_18f = [(18688, 'Emma'), (17921, 'Olivia'), (14924, 'Ava'), (14464, 'Isabella'), (13928, 'Sophia')]
datos_18m = [(19837, 'Liam'), (18267, 'Noah'), (14516, 'Michael'), (13525, 'James'), (13389, 'Oliver')]

gender = 'f'
pos = 1

if gender == 'm':
    print(f'Varones en posición {pos+1}: ')
    dife = datos_18m[pos][0] - datos_08m[pos][0]
    primer_nombre = datos_18m[pos][1]
    segundo_nombre = datos_08m[pos][1]
    primer_anio = 2018
    segundo_anio = 2008
    if dife < 0:
        dife *= -1
        primer_nombre, segundo_nombre = segundo_nombre, primer_nombre
        primer_anio, segundo_anio = segundo_anio, primer_anio
elif gender == 'f':
    print(f'Mujeres en posición {pos+1}: ')
    dife = datos_18f[pos][0] - datos_08f[pos][0]
    primer_nombre = datos_18f[pos][1]
    segundo_nombre = datos_08f[pos][1]
    primer_anio = 2018
    segundo_anio = 2008
    if dife < 0:
        dife *= -1
        primer_nombre, segundo_nombre = segundo_nombre, primer_nombre
        primer_anio, segundo_anio = segundo_anio, primer_anio

print(f'{primer_nombre} de {primer_anio} tiene {dife} nacimientos más que {segundo_nombre} de {segundo_anio}') 

print('2) Nombres que comienzan con J')
inicial = 'J'

nombres_18f = [n[1] for n in datos_18f]
nombres_18m = [n[1] for n in datos_18m]
#print(nombres_18f)

todos_los_nombres = nombres_08f + nombres_08m + nombres_18f + nombres_18m
for nombre in todos_los_nombres:
    #print(nombre, end='.')
    if nombre[0] == inicial:
        print(nombre, end=' ')
print()

print('3) Nombres que se repiten en ambos años')
nombres2008 = nombres_08f + nombres_08m
nombres2018 = nombres_18f + nombres_18m
for nombre in  nombres2008:
    if nombre in nombres2018:
        print(nombre)
