nacidosen2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
nacidosen2018 = "Liam,19837,m,Noah,18267,m,Michael,14516,m,James,13525,m,Oliver,13389,m,Emma,18688,f,Olivia,17921,f,Ava,14924,f,Isabella,14464,f,Sophia,13928,f"

nac2008 = nacidosen2008.split(',')
nac2018 = nacidosen2018.split(',')

#1)
masc2018 = []
fem2018 = []
posM2018 = 0
posF2018 = 0
masc2008 = []
fem2008 = []
posM2008 = 0
posF2008 = 0
nombresTotal = []

for dato2018 in range(0, len(nac2018), 3):
    nombre = nac2018[dato2018]
    nombresTotal.append(nombre)
    cantNaci = nac2018[dato2018 + 1]
    sexo = nac2018[dato2018 + 2]

    if sexo == 'm':
        posM2018 += 1
        masc2018.append((nombre, cantNaci, sexo, posM2018))
    elif sexo == 'f':
        posF2018 += 1
        fem2018.append((nombre, cantNaci, sexo, posF2018))

for dato in range(0, len(nac2008), 3):
    nombre = nac2008[dato]
    nombresTotal.append(nombre)
    cantNaci = nac2008[dato + 1]
    sexo = nac2008[dato + 2]

    if sexo == 'm':
        posM2008 += 1
        masc2008.append((nombre, cantNaci, sexo, posM2008))
    elif sexo == 'f':
        posF2008 += 1
        fem2008.append((nombre, cantNaci, sexo, posF2008))


pos = int(input('Ingrese una posicion (1-5): '))
gen = input('Ingrese un genero (m/f): ')

if gen == 'm':
    for nombre, cantidad, genero, posicion in masc2008:
        if posicion == pos:
            nombre2008 = nombre
            cant2008 = int(cantidad)
            
    for nombre, cantidad, genero, posicion in masc2018:
        if posicion == pos:
            nombre2018 = nombre
            cant2018 = int(cantidad)
            resultado = cant2008 - cant2018
    if cant2008 > cant2018:
        resultado = cant2008 - cant2018
        print(resultado,'1')
        print(f'Varones en posición #{pos}: {resultado} a favor de {nombre2008}(2008) sobre {nombre2018}(2018)')
    else:
        resultado = cant2018 - cant2008
        print(resultado,'2')                
        print(f'Varones en posición #{pos}: {resultado} a favor de {nombre2018}(2018) sobre {nombre2008}(2008)')
            
                   
else:
    for nombre, cantidad, genero, posicion in fem2008:
            if posicion == pos:
                nombre2008 = nombre
                cant2008 = int(cantidad)

    for nombre, cantidad, genero, posicion in fem2018:
        if posicion == pos:
            nombre2018 = nombre
            cant2018 = int(cantidad)
            resultado = cant2008 - cant2018
    if cant2008 > cant2018:
        resultado = cant2008 - cant2018
        print(f'Mujeres en posición #{pos}: {resultado} a favor de {nombre2008}(2008) sobre {nombre2018}(2018)')
    else:
        resultado = cant2018 - cant2008
        print(f'Mujeres en posición #{pos}: {resultado} a favor de {nombre2018}(2018) sobre {nombre2008}(2008)')

#2)
contador = {}
nombre_por_letra=[]
letra = input('Ingrese una letra: ')
letra = letra.upper()

for nombre in nombresTotal:
    if letra == nombre[0]:
        nombre_por_letra.append(nombre)       
if len(nombre_por_letra) < 1:
    print(f'No existen nombres con la letra {letra}')
else:    
    print(f'Nombres con {letra}: {' '.join(nombre_por_letra)}')
     

#3)
cont_nombres = {}
nomb_repet = []
for nombre in nombresTotal:
    if nombre in cont_nombres:
        cont_nombres[nombre] +=1
    else:
        cont_nombres[nombre] =1
for nombre, can_rep in cont_nombres.items():
    if can_rep > 1:
        nomb_repet.append(nombre)
print('Nombres que se repiten:',' '.join(nomb_repet))        

#Probando comprobe que print(' '.join(nomb_repet)) es igual a poner 
# nombRep = ' '.join(nomb_repet)
#print(nombRer)

    
