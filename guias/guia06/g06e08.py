notas = {"Juan": 85, "Ana": 92, "Luis": 78, "María": 95}
estudiantes_mas_90 = []

for nombre, nota in notas.items():
    if nota > 90:
        estudiantes_mas_90.append(nombre)

print(estudiantes_mas_90)