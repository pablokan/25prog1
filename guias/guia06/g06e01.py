persona = {}
persona['nombre'] = 'Juan'
persona['edad'] = 35
persona['ciudad'] = 'Córdoba'
print(persona)

# construyo el diccionario a partir de listas paralelas
claves = ['nombre', 'edad', 'ciudad']
valores = ['Ana', 22, 'Rosario']
otra_persona = {}

for i in range(len(claves)):
    otra_persona[claves[i]] = valores[i]
print(otra_persona)

otra_persona_mas = {}
for c, v in zip(claves, valores): # zip permite recorrer listas paralelas por elemento
    otra_persona_mas[c] = v
print(otra_persona_mas)
