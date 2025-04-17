# Cargar una lista con números. Invertir los elementos sin usar otra lista. Sin usar reverse

numeros = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete']
#numeros.reverse() esto no vale
""" 
aux = numeros[0]
numeros[0] = numeros[6]
numeros[6] = aux

aux = numeros[1]
numeros[1] = numeros[5]
numeros[5] = aux

aux = numeros[2]
numeros[2] = numeros[4]
numeros[4] = aux
"""

posicion_ultimo_elemento = len(numeros) - 1
for i in range(len(numeros)//2):
    aux = numeros[i]
    numeros[i] = numeros[posicion_ultimo_elemento-i]
    numeros[posicion_ultimo_elemento-i] = aux

print(numeros)