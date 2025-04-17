numeros = [1, 4, 2, 4, 5, 6, 4]
print(numeros)
eliminar = 4

#lista_sin_4 = []
""" for n in numeros:
    if n != eliminar:
        lista_sin_4.append(n)
numeros = lista_sin_4
 """
lista_sin_4 = [n for n in numeros if n != eliminar]
print(lista_sin_4)