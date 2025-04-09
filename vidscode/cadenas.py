""" palabra = 'mesa'
for i in range(len(palabra)):
    print(palabra[i])

lista = ['m', 'e', 's', 'a']
for i in range(len(lista)):
    print(lista[i])

for letra in palabra:
    print(letra)

# concatenación
nombre = 'Ana'
edad = 33
frase = nombre + ' tiene ' + str(edad)
print(frase)

frase = 'El árbol y el bosque'
posiArbol = frase.find('árbol') # devuelve la posición de la subcadena en la cadena
print(posiArbol)
print(frase.find('l', 2)) # con un argumento adicional de posición de inicio, busca desde alli
print(frase.find('l ár'))
print(frase.find('silla'))
print(frase.find('z'))    
print(frase.find(' '))

# slicing: obtiene una subcadena
principio = frase[:8] # obtengo la subcadena que va desde el inicio hasta la posición 7
print(principio)
final = frase[10:]
print(final)
print(frase[9:14])

cadena = 'dulce y queso'
posi = cadena.find('y')
palabra1 = cadena[:posi-1]
palabra2 = cadena[posi+2:]
print(palabra1)
print(palabra2)
"""
frase = 'El árbol y el bosque'
lista = frase.split('l')
print(lista)
lista = frase.split()
print(lista)
cadena = 'queso---dulce---sal'
print(cadena.split('---'))
dato = 'Juan,234400,Alvear 987'
print(dato.split(','))
lista = ['hola', 'como', 'te', 'va']
print(lista)
print(''.join(lista))
print(' '.join(lista))
print('$$'.join(lista))