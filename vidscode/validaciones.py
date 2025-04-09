# validaciones

# ejercicio 5 de la guía 1
# Pedir dos números enteros, sumarlos y mostrar el resultado.

n1 = input('Ingrese primer número entero: ')
n2 = input('Ingrese segundo número entero: ')
try:
    n1 = int(n1)
    n2 = int(n2)
    print(f"La suma de {n1} y {n2} es {n1 + n2}")
    
except ValueError:
    print('Debe ingresar un número entero')

