# Buscar una palabra completa en un texto 
# y contar cuántas veces está.

texto = "Quiero comer manzanas, solamente manzanas."
palabra = 'manzanas'

# Solución 1: cambiando desde donde busco
""" 
comienzo = 0
encontrado = True
contador = 0
while encontrado: # encontrado == True
    pos_palabra = texto.find(palabra, comienzo) # cambio desde donde busco
    if pos_palabra == -1: # no lo encontró
        encontrado = False
    else:
        contador += 1 # contador = contador + 1
        comienzo = pos_palabra + 1
print(f'La palabra {palabra} fue encontrada {contador} veces.')

"""

# Solución 2: Recortando la cadena hasta la aparición
encontrado = True
contador = 0
while encontrado: # encontrado == True
    pos_palabra = texto.find(palabra)
    if pos_palabra == -1: # no lo encontró
        encontrado = False
    else:
        contador += 1 # contador = contador + 1
        texto = texto[pos_palabra+1:]
print(f'La palabra {palabra} fue encontrada {contador} veces.')