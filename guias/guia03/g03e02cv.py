# Pedir el ingreso de 5 números. Contar los mayores de 23. Mostrar el resultado.

# La iteración sirve para evitar estas repeticiones:
# n1 = input('Número 1: ')
# n2 = input('Número 2: ')
# n3 = input('Número 3: ')
# n4 = input('Número 4: ')
# n5 = input('Número 5: ')

# Prueba: 5, 40, 1, 30, 2
contador = 0
for i in range(5): # range(5) es igual que range(0, 5)
    n = input(f'Ingrese número {i+1}: ')
    n = int(n)
    if n > 23:
        contador = contador + 1 # contador += 1 es equivalente
print(f'Los números ingresados que eran mayores a 23 eran {contador}')

