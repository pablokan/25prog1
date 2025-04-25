# Buscar una palabra y reemplazarla por otra todas las veces que 
# aparezca. 
# Ej.: ‘peras’ en lugar de ‘manzanas’ quedaría 
# 'Quiero comer peras, solamente peras.' Sin usar replace.

texto = "Quiero comer manzanas, solamente manzanas, muchas manzanas."
palabra_vieja = 'manzanas'
palabra_nueva = 'peras'
encontrado = True

while encontrado:
    print(texto)
    pos_palabra_vieja = texto.find(palabra_vieja)
    if pos_palabra_vieja == -1:
        encontrado = False
    else:
        principio = texto[:pos_palabra_vieja]
        final = texto[pos_palabra_vieja+len(palabra_vieja):]
        texto = principio + palabra_nueva + final

print(texto)