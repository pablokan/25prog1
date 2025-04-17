# Recibir por teclado una cadena de números, dejarlo en formato string e insertar  un punto cada 3 dígitos como divisorio de miles. Ej.  “1234567890” debería devolver “1.234.567.890”

numero = '12345678903490483948394839483948903'
numero_con_puntos = ''
posicion_ultimo_digito = len(numero)-1
contador = 0
for i in range(len(numero)):
    digito = numero[posicion_ultimo_digito - i]
    #print(digito, end=' - ')
    numero_con_puntos = digito + numero_con_puntos
    print(numero_con_puntos)
    contador = contador + 1
    if contador == 3:
        numero_con_puntos = '.' + numero_con_puntos
        contador = 0
        print(numero_con_puntos)
if numero_con_puntos[0] == '.':
    numero_con_puntos = numero_con_puntos[1:]
print(numero_con_puntos)
