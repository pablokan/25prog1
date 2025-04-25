fecha1 = '20250422' # fecha canónica
fecha2 = '22/4/25' # 1/1/25
fecha3 = '22-04-2025'


d1 = int(fecha1[6:])
m1 = int(fecha1[4:6])
a1 = int(fecha1[:4])
print(d1, m1, a1)

fecha2_lista = fecha2.split('/')
d2 = int(fecha2_lista[0])
m2 = int(fecha2_lista[1])
a2 = int(fecha2_lista[2])
print(d2, m2, a2)