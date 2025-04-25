# Mostrar el valor doble del número de dos cifras (que es el único número) 
# encontrado en la cadena. Ej.: 'Juan tiene 25 años' mostraría el número 50.

cadena = 'Juan tiene 25 años'
cadena = 'Hace 98 años que Bohr inventó la cuántica'
cadena = '10 años atrás viajé a Bolivia'

i = 0
encontrado = False
while not encontrado: # encontrado == False
    if cadena[i] in '123456789':
        primer_digito = cadena[i]
        segundo_digito = cadena[i+1]
        encontrado = True
    else:
        i += 1 # i = i + 1

numero_2_digitos = primer_digito + segundo_digito
numero = int(numero_2_digitos)
print(numero * 2)