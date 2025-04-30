# Buscar una palabra completa en un texto y contar cuántas veces está.
texto = 'Quiero comer manzanas, solamente manzanas, muchas manzanas.'
palabra_a_buscar = 'kiwis'

contador = 0
while palabra_a_buscar in texto:
    if 1 == 1:
        print(texto)
    contador += 1 # contador = contador + 1
    pos_palabra = texto.find(palabra_a_buscar)
    texto = texto[pos_palabra+1:]
print(contador)