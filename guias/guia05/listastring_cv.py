#cadena = 'piso'
#s[1] = 'a'

lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete']
print(lista[3], lista[-1])

#print(lista[1:5:2])
print(lista[::-1])
print(list(reversed(lista)))
lista.reverse()
print(lista)
cadena = '123'
# cadena.reverse() no funciona por inmutabilidad
print(list(reversed(cadena)))
print(cadena[::-1])
print(cadena)


""" for letra in cadena:
    print(letra, end=' - ')

for i in range(len(cadena)):
    print(cadena[i], end=' - ')

print(len(cadena), len(lista)) """