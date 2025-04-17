ventas = {"Enero": 5000, "Febrero": 6000, "Marzo": 4500}
total = 0
for valor in ventas.values():
    total += valor
print(total)