personas = [["Juan", 32], ["Ana", 87], ["Luis", 12]]  # equivalente a paralelas
for persona in personas: # recorro por elemento
    print(persona[0], 'tiene', persona[1], 'años', end=' | ')
print()

lista_anidada = [
    ['cero-cero', 'cero-uno'],
    ['uno-cero', 'uno-uno'],
    ['dos-cero', 'dos-uno'],
    ['tres-cero', 'tres-uno']
    ]

# for anidados por índice
for x in range(len(lista_anidada)):
    for y in range(len(lista_anidada[x])):
        print(lista_anidada[x][y], end=' | ')