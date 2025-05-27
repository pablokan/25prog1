nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
femeninas2008 = []
masculinos2008 = []
femeninas2018 = ['Emma,18688', 'Olivia,17921', 'Ava,14924', 'Isabella,14464', 'Sophia,13928']
masculinos2018 = ['Liam,19837', 'Noah,18267', 'Michael,14516', 'James,13525', 'Oliver,13389']

#Convierte la string en listas y separa en masculino y femenino
lista_nacidos2008 = nacidos2008.split(',')
for i in range(len(lista_nacidos2008)):
    if lista_nacidos2008[i] == 'f':
        femenina = lista_nacidos2008[i-2] + ',' + lista_nacidos2008[i-1]
        femeninas2008.append(femenina)
    if lista_nacidos2008[i] == 'm':
        masculino = lista_nacidos2008[i-2] + ',' + lista_nacidos2008[i-1]
        masculinos2008.append(masculino)

#Ordena la lista segun el numero... en esto me ayude de internet
femeninas2008.sort(key=lambda x: int(x.split(',')[1]), reverse=True)
masculinos2008.sort(key=lambda x: int(x.split(',')[1]), reverse=True)

#Pide de entrada una posicion y el sexo y devuelve la diferencia en cantidad entre dichos nombres
pos = int(input('Ingrese una posicion del 1 al 5: '))
sexo = input('Ingrese el sexo(f/m): ')
if sexo == 'f':
    f18 = femeninas2018[pos-1].split(',')
    f08 = femeninas2008[pos-1].split(',')
    dif = int(f08[1]) - int(f18[1])
    print(f'Mujeres en el top #{pos}: {dif} es la diferencia entre {f08[0]} del 2008 y {f18[0]} del 2018')
elif sexo == 'm':
    m18 = masculinos2018[pos-1].split(',')
    m08 = masculinos2008[pos-1].split(',')
    dif = int(m08[1]) - int(m18[1])
    print(f'Hombres en el top #{pos}: {dif} es la diferencia entre {m08[0]} del 2008 y {m18[0]} del 2018')

#Al ingresar una letra devuelve todos los nombres que comienzan con esa letra
letra = input('Ingrese una letra: ')
for nombre in femeninas2008:
    pos_coma = nombre.find(',')
    if nombre[0] == letra:
        print(nombre[:pos_coma])
for nombre in femeninas2018:
    pos_coma = nombre.find(',')
    if nombre[0] == letra:
        print(nombre[:pos_coma])
for nombre in masculinos2008:
    pos_coma = nombre.find(',')
    if nombre[0] == letra:
        print(nombre[:pos_coma])
for nombre in masculinos2018:
    pos_coma = nombre.find(',')
    if nombre[0] == letra:
        print(nombre[:pos_coma])

#Muestra los nombres que se repiten
contador = 0
repetidos = []
for i in femeninas2008 + femeninas2018 + masculinos2008 + masculinos2018:
    pos_coma = i.find(',')
    nombrei = i[:pos_coma]
    for x in femeninas2008 + femeninas2018 + masculinos2008 + masculinos2018:
        pos_coma = x.find(',')
        nombrex = x[:pos_coma]
        if nombrei == nombrex:
            contador = contador + 1
    if contador >= 2:
        repetidos.append(nombrei)
    contador = 0
print(f'Los nombres repetidos son: {repetidos}')