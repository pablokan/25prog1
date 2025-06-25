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

def cargar_datos(lista):
    l1 = []
    l2 = []
    l3 = []
    for i in lista:
        d1, d2, d3 = i.split(",")
        l1.append(d1)
        l2.append(d2)
        l3.append(d3)
    return l1, l2, l3

def contar_por_pais(datos, pais):
    contador = 0
    for i in datos:
        if i == pais:
            contador += 1
    return contador

def calculo_edad(fechas, fecha_actual):
    edades = []
    dia_h = int(fecha_actual[0:2])
    mes_h = int(fecha_actual[3:5])
    anio_h = int(fecha_actual[6:10])
    
    for f in fechas:
        dia = int(f[0:2])
        mes = int(f[3:5])
        anio = int(f[6:])
        edad = anio_h - anio
        
        if (mes > mes_h) or (mes == mes_h and dia > dia_h):
            edad -= 1
            edades.append(edad)
        else:
            edades.append(edad)
    return edades

lista_personas = cargar_datos(personas)
nombres_comp = lista_personas[0]
paises = lista_personas[1]
f_nac = lista_personas[2]
# 1 - Obtener cantidad de personas de Argentina
print('- CANTIDAD DE PERSONAS DE ARGENTINA EN LA LISTA')
pers_de_arg = contar_por_pais(paises, 'Argentina')
print(f'La cantidad de personas de Argentina son: {pers_de_arg}\n')

# 2 - Obtener cantidad de personas de un pais ingresado por el usuario
print('- CANTIDAD DE PERSONAS DE UN PAIS ELEGIDO POR EL USUARIO')
opciones = ['France', 'United States', 'Norway', 'Germany']
print(f'Opciones: {opciones}\n')
valido = False
while not valido:
    elegir_pais = input('Ingrese un pais de las opciones: ').title()
    if elegir_pais not in opciones:
        print(f'Pais invalido. Elige uno de las opciones {opciones}')
    else:
        valido = True
cantidad_personas = contar_por_pais(paises, elegir_pais)
print(f'La cantidad de personas de {elegir_pais} es {cantidad_personas}\n')

# 3 - Las nombres de pila y edades de las personas cuyo apellido comience con una letra solicitada al usuario
print('NOMBRE Y EDAD DE PERSONAS QUE SU APELLIDO COMIENZA CON LA LETRA ELEGIDA POR EL USUARIO')
fecha_hoy = input('Ingrese la fecha de hoy (formato: dd/mm/aaaa): ')
edades = calculo_edad(f_nac, fecha_hoy)

nombres = []
apellidos = []
for i in nombres_comp:
    nombre, apellido = i.split(' ')
    nombres.append(nombre)
    apellidos.append(apellido)
    
inicial_apellido = input('Ingrese inicial de apellido: ').upper()
print(f'Las nombres y edades de las personas cuyo apellido empieza con {inicial_apellido} son:')
for i in range(len(apellidos)):
    if apellidos[i][0] == inicial_apellido:
        print(f'- {nombres[i]} tiene {edades[i]} años')

 

