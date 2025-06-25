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

list_personas = []

for persona in personas: # este bucle es para ordena la lista
    parte = persona.split(",")
    list_personas.append(parte)

def buscar_pais(pregunta):
    contador = 0
    opciones = ['Germany', 'United States', 'Norway', 'France']

    if pregunta == False:
        print("Opciones: ['Germany', 'United States', 'Norway', 'France']")
        pais = input("ingrese otro país además de Argentina: ")
    

    if pregunta == True:
        for persona in list_personas:
            if persona[1] == "Argentina":
                contador += 1
        print(f"La cantidad de personas de Argentina es {contador}")

    elif pais in opciones and pregunta == False:
        for persona in list_personas:
            if persona[1] == pais:
                contador += 1
        print(f"La cantidad de personas de {pais} es {contador}")

    else:
        print("opción inválida")


# ---------------------------------

def buscar_apellido(inicial):

    for nom_apelli in list_personas:
        cadena = nom_apelli[0]
        cadena = cadena.split()

        fecha = nom_apelli[2]
        fecha = fecha.split("-")
        año = int(fecha[2])
        edad = 2025 - año
        
        if inicial in cadena[1]:
            print(f"{cadena[0]} tiene {str(edad)} años")







# 1) La cantidad de personas de Argentina
# salida: La cantidad de personas de Argentina es 3
buscar_pais(True)
print(" ")

# 2) La cantidad de personas de un país ingresado por el usuario 
# salida: 
buscar_pais(False)
print(" ")

# 3) Las nombres de pila y edades
# de las personas cuyo apellido comience con una letra solicitada al usuario
# Virgie tiene 31 años  | ['Virgie Brach', 'France', '04-06-1994']
# Willy tiene 27 años   | ['Willy Branscombe', 'Argentina', '21-11-1997']
# Kathryn tiene 32 años | ['Kathryn Backshell', 'United States', '04-10-1992']
# Arron tiene 23 años   | ['Arron Bresnahan', 'United States', '30-06-2001']
inicial = input("Ingrese una inicial en mayusculas: ")
buscar_apellido(inicial)
