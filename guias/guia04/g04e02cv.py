# Cargar letras en una lista hasta que el usuario ingrese un asterisco. 
# Luego hacer otra iteración para contar las vocales. 
# Al final mostrar el total.

# q, w, e, r, a, z, o
letra = ''
letras = []
print('Ingrese letras, cuando quiera finalizar, ingrese un asterisco')
while letra != '*':
    letra = input('Letra: ')
    letras.append(letra)
print(letras)

cantidad_letras = len(letras)
contador_vocales = 0
for i in range(cantidad_letras):
    if letras[i] == 'a' or letras[i] == 'e' or letras[i] == 'i' or letras[i] == 'o' or letras[i] == 'u':
        contador_vocales += 1

print(f'La cantidad de vocales ingresadas es {contador_vocales}')
