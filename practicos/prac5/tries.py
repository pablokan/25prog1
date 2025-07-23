# try:
#     n = int('hola')
#     print('sigue sin ejecutarse esto')
# except:
#     print('viene acá')

from curses.ascii import isalpha


nombre = input('Ingrese su nombre: ')
if nombre.isalpha():
    print('parece un nombre')
else:
    print('no parece')
print(nombre)
