#Tenés que armar a mano 3 listas paralelas, una lista por cada columna de la tabla.
nombres_completos = [
    "Torres, Ana",
    "Hudson, Kate",
    "Quesada, Benicio",
    "Campoamores, Susana",
    "Santamaría, Carlos",
    "Skarsgard, Azul",
    "Catalejos, Walter"
]

departamentos = [
    "Logística",
    "Desarrollo",
    "Desarrollo",
    "Logística",
    "Administración",
    "Logística",
    "Desarrollo"
]

fechas_nacimiento = [
    "15/05/1943",
    "07/04/1984",
    "10/02/1971",
    "21/12/1967",
    "30/01/1982",
    "30/08/1995",
    "18/07/1959"
]

#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
for nombre in nombres_completos:
     apellido, nombre_persona = nombre.split(", ")
     inicial = nombre_persona[0] + "."
     print(f"{inicial} {apellido}")

#2) Decir cuál es el nombre de pila más largo.
nombre_mas_largo = ""
longitud_maxima = 0
for nombre in nombres_completos:
     apellido, nombre_pila = nombre.split(", ")
     if len(nombre_pila) > longitud_maxima:
        longitud_maxima = len(nombre_pila)
        nombre_mas_largo = nombre_pila
print("El nombre de pila más largo es:", nombre_mas_largo)

#3) Mostrar el promedio de edad de las personas del Departamento de Logística

año_actual = 2025
mes_actual = 5
dia_actual = 8

edades_logistica = []

for i in range(len(nombres_completos)):
    if departamentos[i] == "Logística":
      dia, mes, año = fechas_nacimiento[i].split("/")
      dia = int(dia)
      mes = int(mes)
      año = int(año)
      edad = año_actual - año
      if (mes_actual, dia_actual) < (mes, dia):
        edad -= 1
        edades_logistica.append(edad)
if edades_logistica:
    promedio = sum(edades_logistica) / len(edades_logistica)
    promedio_entero = int(promedio)
    print(f"El promedio de edad de las personas del Departamento de Logística es: {promedio_entero } años")


