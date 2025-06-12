def input_int(msg):
    correcto = False
    while not correcto:
        n = input(msg)
        try:
            n = int(n)
            correcto = True
        except ValueError:
            print('Debe ingresar un entero!')
    return n

numero = input_int('Ingrese un entero: ')
print(f'El número ingresado es {numero}')

edad = input_int('Ingrese su edad: ')
print(f'Tenés {edad} años')