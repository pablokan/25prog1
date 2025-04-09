muebles = ["mesa", "silla", "banquito"]
#Se llevan bien con la instrucción de bucle for

print("Recorrido por posición en la lista (con rango)")

for indice in range(len(muebles)): 
    print(muebles[indice])
print("-----------------------------------------------")

print("Recorrido por elemento")
for mueble in muebles:
    print(mueble)
print("-----------------------------------------------")

print("Recorrido por elemento con enumeración")
# Equivalente a los dos anteriores juntos, 
# más la posibilidad de empezar a contar desde 1
# o cualquier otro valor entero
for indice, elemento in enumerate(muebles, start=1):
    print(indice, elemento)
print("-----------------------------------------------")

# Carga de elementos dentro de un for
lista_nombres = []
for i in range(5):
    nombre = input("Ingrese un nombre: ")
    lista_nombres.append(nombre)
print(lista_nombres)