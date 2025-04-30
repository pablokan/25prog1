dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
lluvias = {}
print('Ingrese la lluvia caída por cada día:')
for dia in dias:
    msg = f'{dia}: '
    mm = input(msg)
    mm = int(mm)
    lluvias[dia] = mm

total_lluvia = 0
for valores in lluvias.values():
    total_lluvia += valores

print(total_lluvia)

