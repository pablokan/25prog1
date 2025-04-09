# Ana = 100, Juan = 20, Luisa = 40
respuesta = 'si'
salario_menor = 10**10000
mas_pobre = ''
while respuesta == 'si':
    nombre = input('ingrese su nombre: ')
    salario = int(input('ingrese su sueldo: '))
    if salario < salario_menor :
        salario_menor = salario
        mas_pobre = nombre
    respuesta = input('hay mas personal?(si/no) ')
print(f'el salario mas miserable es de {salario_menor} y el más pobre es {mas_pobre}')

