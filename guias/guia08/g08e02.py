def contarSubCadena(texto, subtexto, ignorarMayusculas=True):
    if ignorarMayusculas:
        texto = texto.lower()
    return texto.count(subtexto)


frase = 'Desde niña me encanta mirar la luna, por eso es que le puse de nombre Luna a mi hija'
print(contarSubCadena(frase, 'luna')) # 2
print(contarSubCadena(frase, 'luna', ignorarMayusculas=False)) # 1
