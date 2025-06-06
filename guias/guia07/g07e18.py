# Hacer una función que determine si una cadena de texto contiene todas las vocales.
from del_accents import eliminar_acentos

def contiene_todas_las_vocales(cadena):
    cadena = eliminar_acentos(cadena)
    vocales = "aeiou"
    c = 0
    for vocal in vocales:
        if vocal in cadena:
            c += 1
    return True if c == 5 else False
        
if contiene_todas_las_vocales('murciélago'):
    print('sep')
print(contiene_todas_las_vocales('ahora'))
print(contiene_todas_las_vocales('uuuuuuuuuuuh'))
print(contiene_todas_las_vocales('euforia'))
palabra = input('Ingrese palabra: ')
if contiene_todas_las_vocales(palabra):
    msg = 'contiene'
else:
    msg = 'no contiene'
print(f'{palabra} {msg}')    
