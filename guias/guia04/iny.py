print('Saber si un valor está en una lista y también en que posición está')
numeros = [20, 10, 30]

if 10 in numeros:
    print(f'está el 10 en la posición {numeros.index(10)}')
else:
    print('no encontré el número 10')
