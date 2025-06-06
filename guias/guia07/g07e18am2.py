# Hacer una función que determine si una cadena de texto contiene todas las vocales.
def eliminar_acentos(cadena):
    letras_acentuadas = {
        'a': 'á',
        'e': 'é',
        'i': 'í',
        'o': 'ó',
        'u': 'ú'
    }
    for k, v in letras_acentuadas.items():
        if v in cadena:
            pos_letra_acentuada = cadena.index(v)
            cadena = cadena[:pos_letra_acentuada] + k + cadena[pos_letra_acentuada+1:]
    return ''.join(cadena)


def contiene_todas_las_vocales(cadena):
    cadena = eliminar_acentos(cadena)
    vocales = 'aeiou'
    for vocal in vocales:
        if vocal not in cadena:
            return False
    return True
    
if contiene_todas_las_vocales('murciélago'):
    print('si')
else:
    print('no')

palabra = input('Ingrese una palabra para verificar si contiene todas las vocales: ')
if contiene_todas_las_vocales(palabra):
    msg = 'SI'
else:
    msg = 'NO'
print(f'La palabra {palabra} {msg} contiene todas las vocales')
