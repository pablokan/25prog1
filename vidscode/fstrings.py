# f-strings (cadenas de caracteres formateadas)

string_comun = "Yo soy una string común y corriente"
string_formateada = f'Yo soy una string formateada'
print(string_comun)
print(string_formateada)

nombre_completo = 'Pablo Kaniefsky'
edad = 59
altura = 1.73

print(nombre_completo, 'tiene', edad, 'años y mide', altura, 'metros')

print(f'{nombre_completo} tiene {edad} años y mide {altura} metros')

num1 = 2
num2 = 5

print(f'La suma de {num1} y {num2} es {num1 + num2} y el producto es {num1 * num2}')
