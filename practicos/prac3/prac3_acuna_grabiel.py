
nacidos2018 = [
    [1, "Liam", 19837, "Emma", 18688],
    [2, "Noah", 18267, "Olivia", 17921],
    [3, "Michael", 14516, "Ava", 14924],
    [4, "James", 13525, "Isabella", 14464],
    [5, "Oliver", 13389, "Sophia", 13928],
    ]

nacidos2008="Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"


# bucle para consegui lista de nacidos2008
contador = 0
inicio = 0
sublista = []
inicio_corte = 0
posición = 0
sublista = []
nacidos2008_list = []

while posición != -1:
    posición = nacidos2008.find(",", inicio)

    if posición != -1:
       posición_respaldo = posición

    if posición != -1:
        contador += 1
        inicio = posición + 1

        if contador == 3:
            contador = 0
            recorte = nacidos2008[inicio_corte:posición]
            inicio_corte = posición + 1
            sublista = recorte.split(",")
            nacidos2008_list.append(sublista)

    elif posición == -1:

        recorte = nacidos2008[inicio_corte:posición_respaldo+2]
        sublista = recorte.split(",")
        nacidos2008_list.append(sublista)


print(nacidos2008_list)
print(" ")

# ------------------------
# 1) _La diferencia en cantidad de bebés_ que existe entre los nombres de misma posición y mismo sexo.
# Se solicita posición y sexo. (Ver salidas de ejemplo).

# salida de ejemplo:
# Varones en posición #1: 2757 nacimientos de varones más del primero del ranking de 2008 Jacob sobre Liam del 2018
# Mujeres en posición #2: 695 es la diferencia entre Julia del 2008 sobre Olivia del 2018
# Varones en posición #4: 5680 a favor de Joshua(2008) sobre James(2018)


# liam = 19837 | jacob = 22594, m
# ------------------------

# bucle para saca el rank 1 de nombres masculinos más usados en 2018
nombre_max_masculino_2018 = nacidos2018[0]

for i in range(2):
    nombre_max_masculino_2018.pop()

nombre_max_masculino_2018.pop(0)

print(f"rank 1_2018: {nombre_max_masculino_2018}")


# bucle para ordena, por genero masculino y por nombre más usado 2008.
max_num_nombre = 0
nombre_max_masculino_2008 = []

for elemento in nacidos2008_list:
    if elemento[2] == "m":
        num_de_hombres = int(elemento[1])
        elemento.pop(1)
        elemento.insert(1, num_de_hombres)

        if max_num_nombre < num_de_hombres:
            max_num_nombre = num_de_hombres
            nombre_max_masculino_2008 = elemento

nombre_max_masculino_2008.pop()

print(f"rank 1_2008: {nombre_max_masculino_2008}")

# compracion entre rank 1 masculino, 2018 vs rank 1 masculino, 2008:

if nombre_max_masculino_2008[1] < nombre_max_masculino_2018[1]:

elif nombre_max_masculino_2008[1] > nombre_max_masculino_2018[1]:
    print("no")






