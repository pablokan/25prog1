from datetime import datetime 

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

#-1 

cantidad_argentinos = 0

for persona in personas:
    partes = persona.split(",")
    pais = partes[1]
    if pais == "Argentina":
        cantidad_argentinos += 1
    
print("La cantidad de personas de argentina son", cantidad_argentinos)

#-2 

paises_validos = ['Germany', 'United States', 'Norway', 'France']

pais_ingresado = ""

while pais_ingresado not in paises_validos:
    print("opciones:", paises_validos)
    pais_ingresado = input("Ingrese otro pais ademas de Argentina: ")
    if pais_ingresado not in paises_validos:
        print("Opcion invalida")

cantidad_usuario = 0

for persona in personas:
    partes = persona.split(",")
    pais = partes[1]
    if pais == pais_ingresado:
        cantidad_usuario += 1

print('la cantidad de personas de', pais_ingresado, 'es', cantidad_usuario)

#-3

inicial = input("Ingrese inicial del apellido:")

print("Las nombres y edades de las personas cuyo apellido empieza con", inicial, "son:")

for persona in personas:
    partes = persona.split(",")
    nombre_completo = partes[0]
    fecha_nac = partes[2]

    nombre, apellido = nombre_completo.split(" ", 1)

    if apellido.startswith(inicial):
        fecha_nac_dt = datetime.strptime(fecha_nac, "%d-%m-%Y")
        hoy = datetime.today()
        edad = hoy.year - fecha_nac_dt.year
        if (hoy.month, hoy.day) < (fecha_nac_dt.month, fecha_nac_dt.day):
            edad -= 1

        print(nombre, "tiene", edad, "años")