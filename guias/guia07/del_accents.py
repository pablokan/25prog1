def eliminar_acentos(cadena):
    letras_acentuadas = {
        'a': 'á',
        'e': 'é',
        'i': 'í',
        'o': 'ó',
        'u': 'ú'
    }
    cadena = list(cadena)
    for k, v in letras_acentuadas.items():
        if v in cadena:
            cadena[cadena.index(v)] = k
    return ''.join(cadena)

if __name__ == '__main__':
    print(eliminar_acentos('murciélago'))
    print(eliminar_acentos('árbol'))
    print(eliminar_acentos('mormón'))
    print(eliminar_acentos('tablero'))


