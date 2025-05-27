print("1)- La diferencia en cantidad de bebés que existe entre los nombres de misma posición y mismo sexo. Se solicita posición y sexo.")
print()
nacidos2008 ="Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
niñas_2008 = []
niños_2008 = []
total_2008_solo_nombres = []
nombres_totales_2018 = []
nombres_con_la_misma_inicial = []
repetiones = []
nacidos_2008 = nacidos2008.split(",")
for a in range(len(nacidos_2008)):
    if nacidos_2008[a] == "f":
        cantidad = nacidos_2008[a-1]
        nombre = nacidos_2008[a-2]
        cantidad_nombre = str(cantidad)+ ", " + str(nombre)
        total_2008_solo_nombres.append(nombre)
        niñas_2008.append(cantidad_nombre)
    if nacidos_2008[a] == "m":
        cantidad = nacidos_2008[a-1]
        nombre = nacidos_2008[a-2]
        cantidad_nombre = str(cantidad)+ ", " + str(nombre)
        total_2008_solo_nombres.append(nombre)
        niños_2008.append(cantidad_nombre)
niñas_2008_ordenado = sorted(niñas_2008, reverse=True)
niños_2008_ordenado =sorted(niños_2008, reverse=True)
niñas_2018_ordenados = ["18688, Emma", "17921, Olivia", "14924, Ava", "14464, Isabella", "13928, Sophia"]
niños_2018_ordenados = ["19837, Liam", "18267, Noah", "14516, Michael", "13525, James", "13389, Oliver"]
hay_mas_comparaciones = "s"
while hay_mas_comparaciones == "s":
    ranking = int(input("Ingrese el ranking que se quieres comparar: "))
    sexo = input("Ingrese el sexo (f/m): ")
    posicion = niñas_2008[ranking-1].find(",")
    if sexo == "f":
        diferencia = int(niñas_2008_ordenado[ranking-1][:posicion]) - int(niñas_2018_ordenados[ranking-1][:posicion])
        if diferencia >= 0:
            print(f"Mujeres en la posision #{ranking}: {diferencia} es la diferencia entre {niñas_2008_ordenado[ranking-1][posicion+2:]} del 2008 sobre {niñas_2018_ordenados[ranking-1][posicion+2:]} del 2018")
        else:
            print(f"Mujeres en la posision #{ranking}: {abs(diferencia)} es la diferencia entre {niñas_2018_ordenados[ranking-1][posicion+2:]} del 2018 sobre {niñas_2008_ordenado[ranking-1][posicion+2:]} del 2008")
    else:
        diferencia = int(niños_2008_ordenado[ranking-1][:posicion]) - int(niños_2018_ordenados[ranking-1][:posicion])
        if diferencia >= 0:
            print(f"Varones en la posision #{ranking}: {diferencia} es la diferencia entre {niños_2008_ordenado[ranking-1][posicion+2:]} del 2008 sobre {niños_2018_ordenados[ranking-1][posicion+2:]} del 2018")
        else:
            print(f"Varones en la posision #{ranking}: {abs(diferencia)} es la diferencia entre {niños_2018_ordenados[ranking-1][posicion+2:]} del 2018 sobre {niños_2008_ordenado[ranking-1][posicion+2:]} del 2008")
    hay_mas_comparaciones = input("Hay mas compraciones (s/n): ")

print()
print("2)- Los nombres de todos los bebés que comienzan con la misma letra considerando ambos periodos. Se debe solicitar la letra inicial.")
print()
for n in range(len(niñas_2018_ordenados)):
    nombre_niñas = niñas_2018_ordenados[n][7:]
    nombres_totales_2018.append(nombre_niñas)
    nombre_niños = niños_2018_ordenados[n][7:]
    nombres_totales_2018.append(nombre_niños)
combinacion_2008_2018 = nombres_totales_2018 + total_2008_solo_nombres
inicial = input("Ingrese la letra con el que se buscara los nombres (en mayuscula): ")
print()
for nombre in combinacion_2008_2018:
    if inicial == nombre[0]:
        v = nombre
        nombres_con_la_misma_inicial.append(v)
print(f"Los nombres con la misma inicial ({inicial}) son : {", ".join(nombres_con_la_misma_inicial)}")
print()
print("3)- Los nombres que se repiten en ambos años.")
print()
for nombre in nombres_totales_2018:
    if nombre in total_2008_solo_nombres:
        repetiones.append(nombre)
print(f"Los nombres que se repiten son: {", ".join(repetiones)}")
print()

    
    



        



 






