nombre_completo = ["Torres, Ana",
"Hudson, Kate",
"Quesada, Benicio",
"Campoamores, Susana", 
"Santamaría, Carlos", 
"Skarsgard, Azul", 
"Catalejos, Walter"]

departamentos = ["Logistica", "Desarrollo", "Desarrollo", "Logistica", "Administracion", "Logistica", "Desarrollo"]

fecha_de_nacimiento = ["15/05/1943",
"07/04/1984",
"10/02/1971",
"21/12/1967",
"30/01/1982",
"30/08/1995",
"18/07/1959"]

#inicial de nombre con el apellido

for nombre in nombre_completo:
    nombre_dividido = nombre.split(",")
    apellido = nombre_dividido[0].strip()
    nombre_entero = nombre_dividido[1].strip()
    inicial = nombre_entero[0]
    print(f'{inicial}. {apellido}')

print('=' * 30)
#nombre pila mas largo 

nombre_mas_largo = []

for nombre in nombre_completo:
    nombre_dividido = nombre.split(",")
    nombre_entero = nombre_dividido[1]
    nombre_mas_largo.append(nombre_entero)

contador = 0
nombre_pila_largo = ""

for nombre_completo in nombre_mas_largo:
    tamaño_nombre = len(nombre_completo)
    if contador < tamaño_nombre:
        contador = tamaño_nombre
        nombre_pila_largo = nombre_completo

print(f'El nombre pila mas largo es {nombre_pila_largo}')

print('=' * 30)
#mostrar edad promedio del departamento de logistica

edades = []

for i in range(len(fecha_de_nacimiento)):
    if departamentos[i] == "Logistica":
        dia_mes_año = fecha_de_nacimiento[i].split("/")
        sin_signos = [s.strip("/") for s in dia_mes_año]
        dia = int(sin_signos[0])
        mes = int(sin_signos[1])
        año = int(sin_signos[2])

        if mes < 5 or (mes == 5 and dia <= 5):
            edad = 2025 - año
        else:
            edad = 2025 - año - 1

        edades.append(edad)

edad_total = 0

for edad in edades:
    edad_total += edad

print(f'El promedio de edad de las personas del Departamento de Logística es de {edad_total // len(edades)} años')