# Ingresar nombres en una lista sin repetir (por teclado), 
# luego buscar un nombre (por recorrido) 
# y de encontrarlo decir en qué posición está.

nombres = []
hay_mas = 's'
while hay_mas == 's':
    nombre = input('Nombre: ')
    if nombre in nombres:
        print('nombre repetido, ingrese otro')
    else:
        nombres.append(nombre)
    hay_mas = input('Hay más? (s/n): ')
print(nombres)

nombre_a_buscar = input('Ingrese nombre a buscar: ')
encontrado = False
i = 0
while not encontrado: # encontrado == False
    if nombre_a_buscar == nombres[i]:
        encontrado = True
    else:
        i += 1 # i = i + 1
        if i == len(nombres):
            break # rompe el bucle

if encontrado: # encontrado == True
    print(f'Lo encontré en la posición {i}')
else:
    print('no ta') 
