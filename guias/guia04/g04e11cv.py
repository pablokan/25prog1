""" fecha1 = '19650603' # fecha canónica
fecha2 = '3/6/65'
fecha3 = '03-06-1965'

a1 = int(fecha1[:4])
m1 = int(fecha1[4:6])
d1 = int(fecha1[6:])
print(a1, m1 ,d1)

fecha_lista = fecha2.split('/')
d2 = int(fecha_lista[0])
m2 = int(fecha_lista[1])
a2 = int(fecha_lista[2])
print(a2, m2 ,d2)

fecha_lista = fecha3.split('-')
d3 = int(fecha_lista[0])
m3 = int(fecha_lista[1])
a3 = int(fecha_lista[2])
print(a3, m3 ,d3)
 """

fechas = [[3,6,1965],[13,12,2001]]

for fecha in fechas:
    d, m, a = fecha # asignación múltiple
    print(d, m, a)
