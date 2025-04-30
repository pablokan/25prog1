texto = 'Quiero comer manzanas, solamente manzanas, muchas manzanas.'
palabra_vieja = 'manzanas'
palabra_nueva = 'peras'

while palabra_vieja in texto:
    pos_palabra_vieja = texto.find(palabra_vieja)
    principio = texto[:pos_palabra_vieja]
    final = texto[pos_palabra_vieja+len(palabra_vieja):]
    texto = principio + palabra_nueva + final

print(texto)

