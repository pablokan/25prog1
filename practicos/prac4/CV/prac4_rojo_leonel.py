#Practico 4

from datetime import date

hoy = date.today()
hoy = hoy.strftime("%d-%m-%Y")

personas = [
    "Vikki Tewkesbury,France,30-01-2000",
    "Virgie Brach,France,04-06-1994",
    "Adeline LaPadula,France,18-06-2002",
    "Willy Branscombe,Argentina,21-11-1997",
    "Diane Piffe,France,07-08-1993",
    "Britta Causbey,France,24-04-1991",
    "Elisabeth Cleeve,France,04-03-1991",
    "Rafael Ivanchenkov,France,28-04-2002",
    "Zerk Milsom,Norway,03-12-1994",
    "Adorne Ovington,United States,17-08-1991",
    "Kathryn Backshell,United States,04-10-1992",
    "Blake Colbeck,United States,18-01-1999",
    "Arron Bresnahan,United States,30-06-2001",
    "Deloria Dominguez,France,31-07-1990",
    "Grenville Aldersea,Argentina,11-01-2001",
    "Jemimah Haughian,Argentina,30-11-1998",
    "Con Gethen,United States,06-06-1992",
    "Roxie Igoe,France,31-03-2002",
    "Hollyanne Mottley,United States,05-01-1996",
    "Ambrosio Cadore,Norway,09-12-2002"
]

def contar_por_pais (lista_personas, pais_buscar = None):
    pais = ""
    contador = 0
    opciones = ['Germany', 'United States', 'Norway', 'France']

    while pais_buscar == None:
        pais_buscar = input("Ingrese otro país además de Argentina, Opciones: ['Germany', 'United States', 'Norway', 'France']: ")
        if pais_buscar not in opciones:
            print("Opción inválida")
            pais_buscar = None

    for i in range (len(lista_personas)):
        datos_persona = lista_personas[i].split(",")
        pais = datos_persona[1]

        if pais == pais_buscar:
            contador += 1
    
    return f"La cantidad de personas pertenecientes a {pais_buscar} son {contador}"

def calcular_edad (fecha, hoy = hoy):
    fecha_nacimiento = fecha.split("-")
    fecha_de_hoy = hoy.split("-")

    edad = int(fecha_de_hoy[2]) - int(fecha_nacimiento[2])
    if int(fecha_de_hoy[1]) < int(fecha_nacimiento[1]) or int(fecha_de_hoy[1]) == int(fecha_nacimiento[1]) and int(fecha_de_hoy[0]) < int(fecha_nacimiento[0]):
        edad -= 1
    
    return edad

def edades_segun_letra (lista_personas, letra_buscar):

    for i in range (len(lista_personas)):
        lista_datos = lista_personas[i].split(",")
        nombre_apellido = lista_datos[0]
        fecha_nacimiento = lista_datos[2]
        nombre_apellido = nombre_apellido.split(" ")
        nombre = nombre_apellido[0]
        apellido = nombre_apellido[1].lower()

        if apellido[0] == letra_buscar:
            print(f"{nombre} tiene {calcular_edad(fecha_nacimiento)} años")


#La cantidad de personas de Argentina:
print(contar_por_pais(personas, "Argentina"))
print()

#La cantidad de personas de un país ingresado por el usuario:
print(contar_por_pais(personas))
print()

#Las nombres de pila y edades de las personas cuyo apellido comience con una letra solicitada al usuario:
edades_segun_letra(personas, letra_buscar = input("Ingrese inicial de apellido: ").lower())