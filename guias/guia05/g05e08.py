#  Determinar cuál es la vocal que aparece con mayor frecuencia.
texto = 'Quiero comer emaenzanas, esolaeeeeeeeeeeemente manzanas.'

vocales = ['a', 'e', 'i', 'o', 'u']
cantidades = [0, 0, 0, 0, 0]

for letra in texto:
    if letra == 'a':
        cantidades[0] += 1
    elif letra == 'e':
        cantidades[1] += 1
    elif letra == 'i':
        cantidades[2] += 1
    elif letra == 'o':
        cantidades[3] += 1
    elif letra == 'u':
        cantidades[4] += 1
print(cantidades)

mas_vocales = 0
mas_frecuente = ''

for i in range(len(vocales)):
    if cantidades[i] > mas_vocales:
        mas_vocales = cantidades[i]
        mas_frecuente = vocales[i]

print(mas_frecuente)