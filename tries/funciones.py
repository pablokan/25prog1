def saludar(nombre, edad):
    return f'Hola {nombre}, tenés {edad} años'


# Programa Principal (Comienzo del flujo de ejecución)
print('Comienza el programa principal')
nombre = input('Ingrese su nombre: ')
edad = 99
print(saludar(nombre, edad//2))
print(saludar('Ana', 30))
edad_luis = 66
print(saludar('Luis', edad_luis))


print('Fin del programa principal')

print(saludar('Ana', ))