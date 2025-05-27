nacidos2008="Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

lista_nacidos2018= ['Liam,19837,m','Emma,18688,f','Noah,18267,m','Olivia,17921,f','Michael,14516,m','Ava,14924,f','James,13525,m','Isabella,14464,f','OLiver,13389,m','Sophia,13928,f']

#obtencion de sexos
lista_nacidos2008 = nacidos2008.split(',')

lista_sexos2008 = []
for sexos2008 in lista_nacidos2008:
    if sexos2008 == 'f' or sexos2008 == 'm':
        lista_sexos2008.append(sexos2008)

lista_sexos2018 = []
for x in lista_nacidos2018:
    partes = x.split()	
    for sexos2018 in partes:
        separador = sexos2018.split(',')
        lista_sexos2018.append(separador[2])



#obtencion de nombres
lista_nombres2008 = []
lista_nacidos2008 = nacidos2008.split(',')
nombres = lista_nacidos2008[::3]
for nombres2008 in nombres:
	lista_nombres2008.append(nombres2008)



lista_nombres2018 = []
for nombres in lista_nacidos2018:
	partes = nombres.split(',')
	lista_nombres2018.append(partes[0])


#obtencion de cantidad de naciminetos
lista_cantidad2008 = []
lista_cantidad = nacidos2008.split(',')
lista_cantidad2008 = lista_cantidad[1::3]


lista_cantidad2018 = []
for cantidad in lista_nacidos2018:
	partes = cantidad.split(',')
	lista_cantidad2018.append(partes[1])


#salida posicion 1 
lista_masculinos2008 = []
for nombres2008 in range(len(lista_nombres2008)):
	if lista_sexos2008[nombres2008] == 'm':
		lista_masculinos2008.append(lista_nombres2008[nombres2008])

lista_masculinos2018 = []
for nombres2018 in range(len(lista_nombres2018)):
	if lista_sexos2018[nombres2018] == 'm':
		lista_masculinos2018.append(lista_nombres2018[nombres2018])
lista_femeninas2008 = []
for nombres2008 in range(len(lista_nombres2008)):
	if lista_sexos2008[nombres2008] == 'f':
		lista_femeninas2008.append(lista_nombres2008[nombres2008])

lista_femeninas2018 = []
for nombres2008 in range(len(lista_nombres2018)):
	if lista_sexos2008[nombres2008] == 'f':
		lista_femeninas2018.append(lista_nombres2018[nombres2008])




 

valor_m1 = int(lista_cantidad2018[0])
valor_m2 = int(lista_cantidad2008[1])
print(f'Varones en posicion #1: {valor_m1 - valor_m2} nacimientos de varones mas del primero del ranking de 2018 {lista_masculinos2018[0]} sobre {lista_masculinos2008[0]} del 2008' )

valor_f1 = int(lista_cantidad2008[0])
valor_f2 = int(lista_cantidad2018[1])
print(f'Mujeres en posicion #1:{valor_f2 - valor_f1} es la diferencia entre {lista_femeninas2018[0]} del 2018 sobre {lista_femeninas2008[0]} del 2008')



lista_inicial_j = []
for inicial in lista_nombres2008:
	if inicial[0] == 'J':
		lista_inicial_j.append(inicial)

for inicial in lista_nombres2018:
	if inicial[0] == 'J':
		lista_inicial_j.append(inicial)
cadena_j = ', '.join(lista_inicial_j)
print(f'Nombres con J: {cadena_j}')

lista_inicial_e = []
for inicial in lista_nombres2008:
	if inicial[0] == 'E':
		lista_inicial_e.append(inicial)

for inicial in lista_nombres2018:
	if inicial[0] == 'E':
		lista_inicial_e.append(inicial)
cadena_m = ', '.join(lista_inicial_e)
print(f'Nombres con M: {cadena_m}')























