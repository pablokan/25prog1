# Dada una serie de nombres y de salarios respectivos, 
# determinar el salario mínimo y mostrar el nombre 
# de la persona que menos gana.
# Datos para probar: Ana=40, Luis=20, Quico=30
# Luis es la persona que menos gana y su salario es de $20

mas_pobre = '' # va cadena vacía porque se cargara cuando la comparación sea positiva
salario_minimo = 1_000_000_000 # es para garantizar que la primera comparación lo sustituya
hay_mas = "si" # es para garantizar que ingrese al while
while hay_mas == "si":
    nombre = input('Nombre: ')
    salario = input('Salario: ')
    salario = int(salario)
    if salario < salario_minimo:
        salario_minimo = salario
        mas_pobre = nombre
    hay_mas = input('Hay más datos para cargar? (si/no): ')

print(f'{mas_pobre} es la persona que menos gana y su salario es de ${salario_minimo}')

