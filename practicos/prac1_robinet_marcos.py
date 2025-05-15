nombres = ['Torres Ana', 'Hudson Kate', 'Quesada Benicio', 'Campoamores Susana', 'Santamaría Carlos', 'Skarsgard Azul', 'Catalejos Walter']
departamentos = ['Logística', 'Desarrollo', 'Desarrollo', 'Logística', 'Administración', 'Logística', 'Desarrollo']
fechas_de_nacimiento = ['15/5/1943', '7/4/1984', '10/2/1971', '21/12/1967', '30/1/1982', '30/8/1995', '18/7/1959']

#1Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

print ("Inicial y apellido de cada persona:")
    
for nombre_completo in nombres:
    nombre_completo = nombre_completo.split()
    inicial = nombre_completo[1][0]
    apellido = nombre_completo[0]
    print (f"{inicial}. {apellido}")

#2Decir cuál es el nombre de pila más largo.

nombre_mas_largo = ""

for nombre_completo in nombres:
    nombre_completo = nombre_completo.split()
    nombre = nombre_completo[1]
    if len(nombre)  > len(nombre_mas_largo):
       nombre_mas_largo = nombre
print(f"El nombre mas largo es {nombre_mas_largo}")

#Mostrar el promedio de edad de las personas del Departamento de Logística
fecha = [6, 5, 2025]
edades =[]
for i in range (len(nombres)):
    if departamentos[i] == "Logística":
       fecha_de_nacimiento = fechas_de_nacimiento[i]
       años = (fecha_de_nacimiento.split("/"))
       d = int(años[0]) 
       m= int(años[1])
       a= int(años[2])
       edad = fecha[2] - a
       edades.append(edad)
total = 0
for año in edades:
    total += año
promedio_edades = total / len(edades)
print (f"El promedio de edades en el departamento logística es {promedio_edades}")
