# import inputs # preserva el espacio de nombres
from datetime import date

hoy = date.today()
print(hoy)


from inputs import input_int, foo

def foo():
    print('yo soy el foo de app')

#edad = inputs.input_int('Ingrese su edad')
edad = input_int('Ingrese su edad')
print(f'Tenés {edad} años')

foo()


