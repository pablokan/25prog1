nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
lista_nacidos2008 = nacidos2008.split(',')
datos_08f = []
datos_08m = []
for i in range(len(lista_nacidos2008)):
    if lista_nacidos2008[i] == 'f':
        cantidad = int(lista_nacidos2008[i-1])
        nombre = lista_nacidos2008[i-2]
        datos_08f.append([cantidad, nombre])
    elif lista_nacidos2008[i] == 'm':
        datos_08m.append([int(lista_nacidos2008[i-1]), lista_nacidos2008[i-2]])
datos_08f.sort(reverse=True)
datos_08m.sort(reverse=True)
print(datos_08f)
print(datos_08m)
datos_18f = [(18688, 'Emma'), (17921, 'Olivia'), (14924, 'Ava'), (14464, 'Isabella'), (13928, 'Sophia')]
datos_18m = [(19837, 'Liam'), (18267, 'Noah'), (14516, 'Michael'), (13525, 'James'), (13389, 'Oliver')]

ddatos08 = {'Mujeres': datos_08f, 'Varones': datos_08m}
ddatos18 = {'Mujeres': datos_18f, 'Varones': datos_18m}

gender = 'Varones'
pos = 0

print(f'{gender} en posición {pos+1}: ')
dife = ddatos18[gender][pos][0] - ddatos08[gender][pos][0]
primer_nombre = ddatos18[gender][pos][1]
segundo_nombre = ddatos08[gender][pos][1]
primer_anio = 2018
segundo_anio = 2008
if dife < 0:
    dife *= -1
    primer_nombre, segundo_nombre = segundo_nombre, primer_nombre
    primer_anio, segundo_anio = segundo_anio, primer_anio

print(f'{primer_nombre} de {primer_anio} tiene {dife} nacimientos más que {segundo_nombre} de {segundo_anio}') 
