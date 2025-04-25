texto = 'Quiero comer manzanas, solamente manzanas.'
palabra_a_buscar = 'manzanas'

# Solución desagradable
pos_inicio_busqueda = 0
contador = 0
while palabra_a_buscar in texto:
    pos_palabra = texto.find(palabra_a_buscar, pos_inicio_busqueda)
    if pos_palabra != -1: # significa que está
        contador += 1 # contador = contador + 1
        pos_inicio_busqueda = pos_palabra + 1
    else:
        break
print(contador) 

""" 
# Solución más adecuada (por ahora)
contador = 0
while palabra_a_buscar in texto:
    pos_palabra = texto.find(palabra_a_buscar)
    contador += 1
    texto = texto[pos_palabra+1:]
print(contador) 
"""