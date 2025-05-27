nacidos_2008="Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
nacidos_2010 = ["Liam,19837,m,Noah,18267,m,Michael,14516,m,James,13525,m,Oliver,13389,m",
                "Emma,18688,f,Olivia,17921,f,Ava,14924,f,Isabella,14464,f,Sophia,13928,f"
                ]
"""
datos_2008 = nacidos_2008.split(",")                            #nacidos 2008
personas_2008 = []
i = 0
while i < len(datos_2008):                                  
    nombre = datos_2008[i]
    contador = int(datos_2008[i + 1])
    sexo = datos_2008[i + 2]
    personas_2008.append((nombre, contador, sexo))
    i += 3
    
datos_2010 = ",".join(nacidos_2010).split(",")                  #nacidos 2010
personas_2010 = []
i = 0
while i < len(datos_2010):
    nombre = datos_2010[i]
    contador = int(datos_2010[i + 1])
    sexo = datos_2010[i+2]
    personas_2010.append((nombre, contador, sexo))
    i += 3
    
                                                               #comparaciones
comp = 1
name08, contador08, sexo08 = personas_2008[comp]
name10, contador10, sexo10 = personas_2010[comp]
if sexo08 == 'm':
    diferencia = contador08 - contador10
    print(f"Varones en posición #{comp}: {diferencia} nacimientos de varones más del primero del ranking de (2008) {name08} sobre {name10} del (2010)")


comp = 2
name08, contador08, sexo08 = personas_2008[comp]
name10, contador10, sexo10 = personas_2010[comp]
if sexo08 == 'f':
    diferencia = contador08 - contador10
    print(f"Mujeres en posición #{comp}: {diferencia} es la diferencia entre {name08} del (2008) sobre {name10} del (2010)")


comp = 3
name08, contador08, sexo08 = personas_2008[comp]
name10, contador10, sexo10 = personas_2010[comp]
if sexo08 == 'm':
    diferencia = contador08 - contador10
    print(f"Varones en posición #{comp}: {diferencia} a favor de {name08}(2008) sobre {name10}(2010)")
    
"""






"""
datos = nacidos_2008.split(",") + ",".join(nacidos_2010).split(",")
nombres = datos[0::3]
nombres_letras = [nombre for nombre in nombres if nombre.lower().startswith("o")]     #metodo startswith (nos dice si empeieza o termina con determina palabra/caracter) .lower nos evita las mayuculas de los nombre

print(f"los nombre que comienzan con o son: {nombres_letras} ")
"""

"""
datos = nacidos_2008.split(",") + ",".join(nacidos_2010).split(",")          
nombres = set(datos[::3])                                                              #no supe como utilizar (set)
.                                                         
print(f"los nombres que se repiten son: {nombres}")
"""

nombres_repetidos = []
datos = nacidos_2008.split(",") + ",".join(nacidos_2010).split(",")
nombres = []
for i in range(0, len(datos),3):
    nombres.append(datos[i])

for nombre in nombres:
    if nombres.count(nombre) > 1 and nombre not in nombres_repetidos:        #.(count) nos dice las veces que se repite un elemento en una lista(> 1)
        nombres_repetidos.append(nombre)
print(f"los nombres repetidos son: {nombres_repetidos}")







    