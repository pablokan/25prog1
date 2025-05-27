nacidos2018 = "Liam,19837,m,Noah,18267,m,Michael,14516,m,James,13525,m,Oliver,13389,m,Emma,18688,f,Olivia,17921,f,Ava,14924,f,Isabella,14464,f,Sophia,13928,f" 

datos = nacidos2018.split(',')

varones2018 = []
mujeres2018 = []

i = 0
while i < len(datos):
    nombre18 = datos[i]
    cantidad = int(datos[i+1])
    sexo = datos[i+2]

    if sexo == 'm':
        varones2018.append([nombre18, cantidad])
    else:
        mujeres2018.append([nombre18, cantidad])

    i = i + 3

varones2018.sort(key=lambda x: x[1], reverse=True)
mujeres2018.sort(key=lambda x: x[1], reverse=True)

nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

datos = nacidos2008.split(',')

varones2008 = []
mujeres2008 = []

i = 0
while i < len(datos):
    nombre = datos[i]
    cantidad = int(datos[i+1])
    sexo = datos[i+2]
    
    if sexo == 'm':
        varones2008.append([nombre, cantidad])
    else:
        mujeres2008.append([nombre, cantidad])

    i = i + 3

varones2008.sort(key=lambda x: x[1], reverse=True)
mujeres2008.sort(key=lambda x: x[1], reverse=True)

#-- Ejercicio 1 -- 

print("DIFERENCIAS ENTRE 2008 Y 2018:")  

for i in range(5):
    nombre08 = varones2008[i][0]
    cantidad08 = varones2008[i][1]
    nombre18 = varones2018[i][0]
    cantidad18 = varones2018[i][1]

    if cantidad08 > cantidad18: 
        diferencia = cantidad08 - cantidad18
        print("Varones en posición #" + str(i+1) + ": " + str(diferencia) + " nacimientos de varones más del primero del ranking de 2008 " + nombre08 + " sobre " + nombre18 + " del 2018")
    else:
        diferencia = cantidad18 - cantidad08
        print("Varones en posición #" + str(i+1) + ": " + str(diferencia) + " nacimientos de varones más del primero del ranking de 2018 " + nombre18 + " sobre " + nombre08 + " del 2008")

for i in range(5):
    nombre08 = mujeres2008[i][0]
    cantidad08 = mujeres2008[i][1]
    nombre18 = mujeres2018[i][0]
    cantidad18 = mujeres2018[i][1]

    if cantidad08 > cantidad18:
        diferencia = cantidad08 - cantidad18
        print("Mujeres en posición #" + str(i+1) + ": " + str(diferencia) + " es la diferencia entre " + nombre08 + " del 2008 sobre " + nombre18 + " del 2018")
    else:
        diferencia = cantidad18 - cantidad08
        print("Mujeres en posición #" + str(i+1) + ": " + str(diferencia) + " es la diferencia entre " + nombre18 + " del 2018 sobre " + nombre08 + " del 2008")

#-- Ejercicio 2 --

letra = input("Escribe una letra para buscar nombres: ").upper()
nom_letra = []

for persona in varones2008 + mujeres2008 + varones2018 + mujeres2018:
    nombre = persona[0]
    if nombre.upper()[0] == letra and nombre not in nom_letra:
        nom_letra.append(nombre)

nom_letra.sort()
print("Nombres con " + letra + ": " + ' '.join(nom_letra))

#-- Ejercicio 3 --

nombres2008 = []
for persona in varones2008 + mujeres2008:
    if persona[0] not in nombres2008:
        nombres2008.append(persona[0])

repetidos = []
for persona in varones2018 + mujeres2018:
    nombre = persona[0]
    if nombre in nombres2008 and nombre not in repetidos:
        repetidos.append(nombre)

repetidos.sort()
print("Nombres que se repiten: " + ' '.join(repetidos))