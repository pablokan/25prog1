#Consigna
#Tengo unas estadísticas de nombres de los recién nacidos en USA que se encuentran en el sitio de la Administración de la Seguridad Social (https://www.ssa.gov/OACT/babynames/)
#Utilizaremos el top-5 de dos años diferentes.
#Dados los siguientes datos:
#Data 2018
#Rank
#Male name
#Number of
#males
#Female name
#Number of
#females
#1
#Liam
#19837
#Emma
#18688
#2
#Noah
#18267
#Olivia
#17921
#3
#Michael
#14516
#Ava
#14924
#4
#James
#13525
#Isabella
#14464
#5
#Oliver
#13389
#Sophia
#13928
#Y considerando que diez años antes, en el 2008, la situación era la siguiente:

#Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f

#Se quiere saber:
#La diferencia en cantidad de bebés que existe entre los nombres de misma posición y mismo sexo. Se solicita posición y sexo. (Ver salidas de ejemplo).
#Los nombres de todos los bebés que comienzan con la misma letra considerando ambos periodos. Se debe solicitar la letra inicial.
#Los nombres que se repiten en ambos años.
#Requisitos de codificación:
#Los datos del 2008 deben ser almacenados inicialmente en una sola variable de tipo string del siguiente modo:
#nacidos2008="Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
#Los datos del 2018 se pueden almacenar a criterio del desarrollador.

#Nota: Se recomienda usar el método sort para ordenar las listas.(investigar!)
#Algunas salidas posibles son:

#Varones en posición #1: 2757 nacimientos de varones más del primero del ranking de 2008 Jacob sobre Liam del 2018
#Mujeres en posición #2: 695 es la diferencia entre Julia del 2008 sobre Olivia del 2018
#Varones en posición #4: 5680 a favor de Joshua(2008) sobre James(2018)

#Nombres con J: Jacob Joshua Julia James
#Nombres que se repiten: Emma Michael Olivia


# Datos 2008 como string
nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18016,f,Jacob,22594,m,Joshua,19225,m,Michael,20626,m,Olivia,17881,f"

# Datos 2018 directamente como listas
datos_2018 = {
    "male": [("Liam", 19837), ("Noah", 18267), ("Michael", 13525), ("James", 13525), ("Oliver", 13389)],
    "female": [("Emma", 18688), ("Olivia", 17921), ("Ava", 14924), ("Isabella", 14464), ("Sophia", 13928)]
}

# datos 2008
lista_2008 = nacidos2008.split(",")
datos_2008 = {"male": [], "female": []}

for i in range(0, len(lista_2008), 3):
    nombre = lista_2008[i]
    cantidad = int(lista_2008[i+1])
    sexo = lista_2008[i+2]
    if sexo == "m":
        datos_2008["male"].append((nombre, cantidad))
    else:
        datos_2008["female"].append((nombre, cantidad))

# 1) Diferencia de cantidad  iguales
print("Diferencias por posición y sexo:")
for sexo in ["male", "female"]:
    print(f"\nSexo: {sexo}")
    for i in range(min(len(datos_2008[sexo]), len(datos_2018[sexo]))):
        nom_2008, cant_2008 = datos_2008[sexo][i]
        nom_2018, cant_2018 = datos_2018[sexo][i]
        diferencia = abs(cant_2018 - cant_2008)
        print(f"Puesto {i+1}: {nom_2008} (2008) vs {nom_2018} (2018) -> Diferencia: {diferencia}")

# 2) Nombres que empiezan con la misma letra (entre ambos años)
def nombres_misma_letra(letra):
    letra = letra.upper()
    nombres = []

    for sexo in ["male", "female"]:
        nombres += [n for n, _ in datos_2008[sexo] if n.upper().startswith(letra)]
        nombres += [n for n, _ in datos_2018[sexo] if n.upper().startswith(letra)]

    return sorted(nombres)

letra = input("\nIngresá una letra para buscar nombres que comienzan con ella: ").upper()
coinciden = nombres_misma_letra(letra)
print(f"\nNombres de ambos años que comienzan con '{letra}':")
for n in coinciden:
    print("-", n)

# 3) Nombres que se repiten en ambos años
def nombres_repetidos():
    nombres_2008 = set([n for s in datos_2008 for n, _ in datos_2008[s]])
    nombres_2018 = set([n for s in datos_2018 for n, _ in datos_2018[s]])
    comunes = sorted(nombres_2008 & nombres_2018)
    return comunes

repetidos = nombres_repetidos()
print("\nNombres que se repiten en 2008 y 2018:")
for n in repetidos:
    print("-", n)
