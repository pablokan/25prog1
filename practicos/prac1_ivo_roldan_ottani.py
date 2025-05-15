# Consigna 1: Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

nombres = ["Ana Torres", "Kate Hudson", "Benicio Quesada", "Susana Campoamores", "Carlos Santamaría", "Azul Skarsgard", "Walter Catalejos"]

for nom in nombres: 
    nombre = nom.split(',')
    apellido = nombre[-1]    
    inicial = ''
    for x in nom.split(): # ["Ana",  "Torres"]
        inicial += x[0] + '.'
    print(inicial.strip(), apellido) # Este no se como hacer para que aparezca solo el nombre

# Consigna 2: Decir cual es el nombre de la pila mas largo
nombre_mas_largo = ''
longitud = 0

for nom in nombres:
    if len(nom) > longitud:
        nombre_mas_largo = nom
        longitud = len(nom)
print(nombre_mas_largo, 'es el nombre mas largo de la lista.') # Por el mismo problema que en la 1 este da susana en vez de benicio

# Consigna 3: Mostrar el promedio de edad de las personas del Departamento de Logística

edad1 = 1943 - 2025
edad2 = 1967 - 2025
edad3 = 1995 - 2025
edades = (edad1, edad2, edad3)
suma = 0
for i in edades: suma += i
print('la edad prmedio es:', (int(suma / 3)), 'años')

# Esta ultima no entendi bien como hacerla por lo que hice un codigo un poco trivial jaja disculpe profe 

