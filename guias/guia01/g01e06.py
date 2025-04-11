# Pedir cuatro notas, calcular el promedio y mostrarlo.
# Salida ejemplo: El promedio de las notas 
# 5, 7, 8 y 9 es 7.25 

nota1 = input("Ingrese una nota 1: ")
nota1 = float(nota1)
nota2 = input("Ingrese una nota 2: ")
nota2 = float(nota2)
nota3 = input("Ingrese una nota 3: ")
nota3 = float(nota3)
nota4 = input("Ingrese una nota 4: ")
nota4 = float(nota4)

suma_notas = nota1 + nota2 + nota3 + nota4
promedio = suma_notas / 4
print('El promedio de las notas es', promedio)
print((nota1 + nota2 + nota3 + nota4)/4)