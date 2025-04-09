lista = [2, 4, 6, 4, 8, 4]
print(lista)
valor = int(input("Ingrese el valor que desea eliminar: "))
""" 
if valor in lista:
    lista = [x for x in lista if x != valor]
    print(f"La lista sin {valor}:", lista)
else:
    print("El valor no ta en la lista.")

"""

lista_nueva = []

for numero in lista:
    if numero != valor:
        lista_nueva.append(numero)

lista = lista_nueva

print(lista)
