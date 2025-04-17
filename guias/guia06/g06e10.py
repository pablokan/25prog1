dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
lluvias = {}
print('Lluvia caída en mm por cada día')
# for dia in dias:
#     msg = f'{dia}: '
#     lluvias[dia] = int(input(msg))

lluvias = {'lunes': 1, 'martes': 1, 'miércoles': 10, 'jueves': 1, 'viernes': 1, 'sábado': 1, 'domingo': 1}
print(lluvias)

mas_mm = 0
dia_mas_lluvioso = ''
total = 0
for k, v in lluvias.items():
    total += v
    if v > mas_mm:
        mas_mm = v
        dia_mas_lluvioso = k

print(total, dia_mas_lluvioso)