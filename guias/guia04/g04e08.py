numeros = [1, 2, 3, 4, 5, 6, 7, 8]
#numeros = [n+1 for n in range(8)]
ultima_posicion = len(numeros)-1

for x in range(len(numeros)//2):
    aux = numeros[x]
    numeros[x] = numeros[ultima_posicion-x]
    numeros[ultima_posicion-x] = aux

# swap directo
#for x in range(len(numeros)//2):
#    numeros[x], numeros[ultima_posicion-x] = numeros[ultima_posicion-x], numeros[x]
    
print(numeros)


