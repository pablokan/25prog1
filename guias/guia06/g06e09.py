hay_mas = 's'
personas = {}
mujeres = []
while hay_mas == 's':
    nombre = input('Nombre: ')
    sexo = input('Sexo: ')
    personas[nombre] = sexo
    hay_mas = input('Más? ')

for nombre, sexo in personas.items():
    if sexo == 'f':
        mujeres.append(nombre)

print(mujeres)