'''
Algunas salidas posibles son:
Varones en posición #1: 2757 nacimientos de varones más del primero del ranking de 2008 Jacob sobre Liam del 2018
Mujeres en posición #2: 695 es la diferencia entre Julia del 2008 sobre Olivia del 2018
Varones en posición #4: 5680 a favor de Joshua(2008) sobre James(2018)
Nombres con J: Jacob Joshua Julia James
Nombres que se repiten: Emma Michael Olivia
'''

#La verdad profe es que este trabajo no lo termine solo, tuve ayuda de un amigo ya que me costo darme cuenta como afrontar el problema y como utilizar el sort en la actividad 1.
#Aunque lo primero que dice el tp es que tratemos de hacerlos solo esa es la realidad

nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

masc18 = [["Liam", 19837], ["Noah", 18267], ["Michael", 14516], ["James", 13525], ["Oliver", 13389]]
fem18 = [["Emma", 18688], ["Olivia", 17921], ["Ava", 14924], ["Isabella", 14464], ["Sophia", 13928]]

nacidos08 = nacidos2008.split(",")

masc08 = []
fem08 = []
for i in range(0, len(nacidos08), 3):
    nombre = nacidos08[i]
    cantidad = int(nacidos08[i + 1])
    sexo = nacidos08[i + 2]
    if sexo == "m":
        masc08.append([nombre, cantidad])
    else:
        fem08.append([nombre, cantidad])

masc08.sort(key=lambda x: x[1], reverse=True)
fem08.sort(key=lambda x: x[1], reverse=True)

masc08nombre = masc08[0][0]
masc08cantidad = masc08[0][1]
masc18nombre = masc18[0][0]
masc18cantidad = masc18[0][1]
diferencia_masc1 = masc08cantidad - masc18cantidad
print(f'Varones en posicion #1: {diferencia_masc1} nacimientos de varon mas del primero del ranking de 2009 {masc08nombre} sobre {masc18nombre} del 2018')
print()

fem08nombre = fem08[1][0]
fem08cantidad = fem08[1][1]
fem18nombre = fem18[1][0]
fem18cantidad = fem18[1][1]
diferencia_fem2 = fem08cantidad - fem18cantidad
print(f'Mujeres en posicion #2: {diferencia_fem2} es la diferencia entre {fem08nombre} del 2008 sobre {fem18nombre} del 2018')
print()

masc08nombre = masc08[3][0]
masc08cantidad = masc08[3][1]
masc18nombre = masc18[3][0]
masc18cantidad = masc18[3][1]
diferencia_masc4 = masc08cantidad - masc18cantidad
print(f'Varones en posicion #4: {diferencia_masc4} a favor de {masc08nombre} (2008) sobre {masc18nombre} (2018)')
print()

letra = "J"
todos_los_nombres = []

for nombre, cantidad in masc08 + fem08:
    if len(nombre) > 0 and nombre[0] == letra:  
        if nombre not in todos_los_nombres:
            todos_los_nombres.append(nombre)

for nombre, cantidad in masc18 + fem18:
    if len(nombre) > 0 and nombre[0] == letra:  
        if nombre not in todos_los_nombres:
            todos_los_nombres.append(nombre)
todos_los_nombres.sort()

print("Nombres con J:", end=" ")
for i in range(len(todos_los_nombres)):
    if i > 0:
        print(" ", end="")
    print(todos_los_nombres[i], end="")
print("")  

nombres08 = [nombre for nombre, cantidad in masc08 + fem08]
nombres18 = [nombre for nombre, cantidad in masc18 + fem18]
nombres_repetidos = []
for nombre in nombres08:
    if nombre in nombres18 and nombre not in nombres_repetidos:
        nombres_repetidos.append(nombre)
nombres_repetidos.sort()
print()

print("Nombres que se repiten:", end=" ")
for i in range(len(nombres_repetidos)):
    if i > 0:
        print(" ", end="")
    print(nombres_repetidos[i], end="")
print("")  


