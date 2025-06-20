def input_int(msg='Ingrese un entero'):
    msg = f'{msg}: '
    validado = False
    while not validado:
        n = input(msg)
        try:
            n = int(n)
            validado = True
        except:
            print('Debe ingresar un número entero!')
    return n

def foo():
    print('yo soy el foo de inputs')

if __name__ == "__main__":
    entero = input_int()
    print(f'Ingresó el entero {entero}')


