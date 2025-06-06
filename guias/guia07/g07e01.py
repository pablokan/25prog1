# Cuántas veces se repite una letra cualquiera. 
# Parámetros: letra, cadena.

def contar(letra, cadena):
    cadena = cadena.lower()
    contador = 0
    for caracter in cadena:
        if letra == caracter:
            contador += 1
    return contador

# Programa Principal
texto = 'Quiero comer manzanas, solamente manzanas.'
letra_a_buscar = 'q'
print(contar(letra_a_buscar, texto))
#cantidad_arrobas = contar('@', 'pablokan@gmail.com')
#c = input('Caracter a buscar: ')
#t = input('Texto donde buscar: ')
#print(contar(c, t))