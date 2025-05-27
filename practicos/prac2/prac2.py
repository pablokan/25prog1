personas = [
    "Josefa Taponales,France(Europe),30-10-2007",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Priya Singh,India(Asia),17-01-2007",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-01-2000"
]

a = 2000
for persona in personas:
    if int(persona[-4:]) < a:
        apellido_inicio = persona.find(' ') + 1
        apellido_final = persona.find(',')
        print(persona[apellido_inicio: apellido_final])

c = 0
pais = 'Norway'
for persona in personas:
    if pais in persona:
        c += 1
print(c)

for persona in personas:
    if 'Europe' not in persona:
        nombre_final = persona.find(' ')
        print(persona[:nombre_final], end=' ')
