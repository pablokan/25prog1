for i in range(-3, 1): # -3, -2, -1, 0. Funciona porque el valor inicial es menor que el valor final
    print(i)

for x in range(-3): # esto no hace nada porque el rango sería (0, -3) y entonces, el valor inicial NO es menor que el valor final, cuestión que es OBLIGATORIA
    print('hola')

for x in range(3): # esto muestra 3 veces hola, es decir, funciona como 'cantidad de iteraciones', porque la x toma 0, 1, 2, que son 3 valores, o sea, da 3 vueltas
    print('hola')