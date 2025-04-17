#Recibir por teclado una cadena de números, dejarlo en formato string e insertar  un punto cada 3 dígitos como divisorio de miles. Ej.  “1234567890” debería devolver “1.234.567.890”
from icecream import ic
ic.configureOutput(includeContext=True)

numero = '123456789'
numero_con_puntos = ''
cuento_tres = 0
for i in range(len(numero)):
    digito = numero[len(numero)-1-i]
    numero_con_puntos = digito + numero_con_puntos
    print(f'{numero_con_puntos=}')
    ic(numero_con_puntos)
    cuento_tres = cuento_tres + 1
    if cuento_tres == 3:
        numero_con_puntos = '.' + numero_con_puntos
        print(numero_con_puntos)
        cuento_tres = 0
if numero_con_puntos[0] == '.':
    numero_con_puntos = numero_con_puntos[1:]
print(numero_con_puntos)
