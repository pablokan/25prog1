# Métodos y Operaciones sobre cadenas de caracteres

# Las strings se pueden usar como listas de caracteres
s = "Yo soy una string"
for c in s:
    print(c, end='-')

print()

for c in s:
    if c == ' ':
        print('<space>', end='')
    else:
        print(c, end='')
