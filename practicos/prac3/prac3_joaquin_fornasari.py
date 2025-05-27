nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

datos_2008 = nacidos2008.split(",")
nombres_2008_m = []
cant_2008_m = []
nombres_2008_f = []
cant_2008_f = []

for i in range(0, len(datos_2008), 3):
    nombre = datos_2008[i]
    cantidad = int(datos_2008[i+1])
    sexo = datos_2008[i+2]
    if sexo == "m":
        nombres_2008_m.append(nombre)
        cant_2008_m.append(cantidad)
    else:
        nombres_2008_f.append(nombre)
        cant_2008_f.append(cantidad)

nombres_2018_m = ["Liam", "Noah", "Michael", "James", "Oliver"]
cant_2018_m = [19837, 18267, 14516, 13525, 13389]
nombres_2018_f = ["Emma", "Olivia", "Ava", "Isabella", "Sophia"]
cant_2018_f = [18688, 17921, 14924, 14464, 13928]

for i in range(5):
    dif_m = cant_2008_m[i] - cant_2018_m[i]
    dif_f = cant_2008_f[i] - cant_2018_f[i]
    print("Varones en posición #" + str(i+1) + ": " + str(abs(dif_m)) + " a favor de " + (nombres_2008_m[i] if dif_m > 0 else nombres_2018_m[i]))
    print("Mujeres en posición #" + str(i+1) + ": " + str(abs(dif_f)) + " a favor de " + (nombres_2008_f[i] if dif_f > 0 else nombres_2018_f[i]))

letra = input("Ingresá una letra para buscar nombres: ").upper()

todos_los_nombres = nombres_2008_m + nombres_2008_f + nombres_2018_m + nombres_2018_f
nombres_con_letra = []

for nombre in todos_los_nombres:
    if nombre.startswith(letra):
        if nombre not in nombres_con_letra:
            nombres_con_letra.append(nombre)

nombres_con_letra.sort()

texto = ""
for i in range(len(nombres_con_letra)):
    texto += nombres_con_letra[i]
    if i != len(nombres_con_letra) - 1:
        texto += " "

print("Nombres con " + letra + ":", texto)

repetidos = []
for nombre in nombres_2008_m + nombres_2008_f:
    if nombre in nombres_2018_m + nombres_2018_f:
        if nombre not in repetidos:
            repetidos.append(nombre)

repetidos.sort()

texto_repes = ""
for i in range(len(repetidos)):
    texto_repes += repetidos[i]
    if i != len(repetidos) - 1:
        texto_repes += " "

print("Nombres que se repiten:", texto_repes)
