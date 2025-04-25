# Ingresar nombres en una lista sin repetir (por teclado), 
# luego buscar un nombre (por recorrido) 
# y de encontrarlo decir en qué posición está.

""" 
nombres = []
hay_mas = 's'
while hay_mas == 's':
    nombre = input('Nombre: ')
    nombres.append(nombre)
    print(nombres)
    hay_mas = input('Hay más nombres para cargar? (s/n): ')
"""

nombres = ['Juan', 'Ana', 'Pedro']
nombre_a_buscar = 'Jorge'
encontrado = False
for i in range(len(nombres)):
    #print(f'{i=}')
    #print(f'{nombres[i]=}')
    if nombres[i] == nombre_a_buscar:
        encontrado = True
        print('Está en la posición', i)

if not encontrado: # encontrado == False
    print('no ta')
