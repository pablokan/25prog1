personas = [
    "Josefa Taponales,France(Europe),30-10-2007",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Norway,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Priya Singh,India(Asia),17-01-2007",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Europe,United States(America),04-01-2000"
]
print('1) Los apellidos de las personas nacidas antes de un año solicitado al usuario.')
anio_solicitado = 2000
for persona in personas:
    lista_persona = persona.split(',')
    nombre_completo = lista_persona[0]
    lista_nombre_apellido = nombre_completo.split()
    _, apellido = lista_nombre_apellido
    anio_nacimiento = int(persona[-4:])
    if anio_nacimiento < anio_solicitado:
        print(apellido)
print()

print('2) La cantidad de personas nacidas en un país ingresado por el usuario.')
pais_ingresado = 'Argentina'
contador = 0
# "Britta Causbey,Germany(Europe),24-01-2000"
for persona in personas:
    pos_parentesis = persona.find(',')
    inicio_pais = pos_parentesis + 1
    final_pais = persona.find('(')
    pais = persona[inicio_pais:final_pais]
    if pais == pais_ingresado:
        contador += 1
print(f'La cantidad de personas nacidas en {pais_ingresado} es {contador}')
print()

print('3) Los nombres de pila de las personas que no son europeas.')
for persona in personas:
    pos_parentesis = persona.find('(')
    inicio_continente = pos_parentesis + 1
    final_continente = persona.find(')')
    continente = persona[inicio_continente:final_continente]
    if continente != 'Europe':
        pos_espacio = persona.find(' ')
        print(persona[:pos_espacio], end=' ')
