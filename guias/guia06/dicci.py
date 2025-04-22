persona = {'nombre': 'Ana', 'edad': 22, 'altura': 1.54}

# Recorrido por claves solas
for clave in persona: # persona.keys()
    print(f'{clave} es {persona[clave]}')

for k, v in persona.items(): # Recorrido por item es clave y valor
    print(k, "->", v)