valor_inicial = 5
valor_final = 9

print('El for comienza con la variable_de_recorrido tomando el valor_inicial')

for variable_de_recorrido in range(valor_inicial, valor_final):
    # muestra 5 cuando ingresa y luego 6, 7 y 8
    print(variable_de_recorrido) 

print('cuando llega al valor final menos uno sale')

vi = 10 # valor inicial
vf = 20 # valor final

print('rango con expresiones:')

for i in range(vi-15, vf*2//3):
    print(i, end=' | ')