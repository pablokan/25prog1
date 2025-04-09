# tuplas

lista_nombres = ["Juan", "Pedro", "Ana", "José"]
tupla_nombres = ("Juan", "Pedro", "Ana", "José")
print(lista_nombres)
print(tupla_nombres)
print(lista_nombres[1])
print(tupla_nombres[1])
lista_nombres[1] = "María" # se puede modificar

#tupla_nombres[1] = "María" # da error porque no se puede modificar

t1 = (1,) # la coma es importante
print(t1)
print(t1[0])

t2 = 1, 2, 3
print(t2)

# desempaquetado
a, b, c, d = tupla_nombres
print(a, b, c, d)

