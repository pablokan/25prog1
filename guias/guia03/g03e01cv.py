# Mostrar por pantalla una lista de 10 números enteros consecutivos, 
# comenzando con un número ingresado por teclado.

# Prueba: 11 - Salida: 11 12 13 ... 20

valor_inicial = input('Ingrese un valor para mostrar los 10 consecutivos siguientes: ')
valor_inicial = int(valor_inicial)
#valor_final = valor_inicial + 10
for i in range(valor_inicial, valor_inicial + 10):
    print(i, end=' : ')
