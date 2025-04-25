# Eliminar todos los valores iguales de una lista. 
# Previamente, solicitar el valor que quiero eliminar y si no está, 
# mostrar un cartel diciendo que no lo ha encontrado.

numeros = [1, 4, 22, 4, 5, 4, 77]
print(numeros)
 
numero_a_eliminar = 4
numeros_sin_4 = []

for numero in numeros:
    if numero != numero_a_eliminar:
        numeros_sin_4.append(numero)
numeros = numeros_sin_4
print(numeros)

#numeros = [n for n in numeros if n != 4]
#print(numeros)