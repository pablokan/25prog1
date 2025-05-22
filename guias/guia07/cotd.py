def operar(operacion, n1, n2): # 3 parámetros: string, número, número
    if operacion == 'suma':
        resultado = n1 + n2 # resultado es una variable local
    elif operacion == 'resta':
        resultado = n1 - n2 
    else:
        resultado = f'Operación desconocida "{operacion}"'
    return resultado

print(resultado) # error!!! esta variable solamente existe dentro de la función
print('Resultado de la suma de 4+5: ', end='')
print(operar("suma", 4, 5)) # mismo orden que los parámetros
a = 2
b = 3
print(f'{a=} y {b=}')
print('Resultado de la resta:', operar("resta", a, b))
salida = operar('mutiplicación', 10, 4) # asigno el retorno a una variable
print(salida)
print(f'a * 3 + 10 (a vale 2): {operar('suma', a*3, 10)}')
otra_salida = operar(7, 5, 'resta') # error!!! orden incorrecto
print(operar('suma', 1, 2, 3)) # error!!! cantidad incorrecta de argumentos