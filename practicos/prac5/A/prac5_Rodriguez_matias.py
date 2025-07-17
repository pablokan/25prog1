clientes = []

with open("clientes.txt", "r", encoding="utf-8") as archivo:
    next(archivo)  # Salta la primera línea de encabezado
    for linea in archivo:
        partes = linea.strip().split("#")
        if len(partes) == 4:
            dni = int(partes[0])
            nombre_apellido = partes[1]
            deuda = float(partes[2])
            localidad = partes[3]
            apellido = nombre_apellido.split()[-1]
            clientes.append([dni, nombre_apellido, deuda, localidad, apellido])

# 1. Contar clientes por localidad
localidad_buscada = input("Ingrese una localidad: ")
contador = 0
for cliente in clientes:
    if cliente[3].lower() == localidad_buscada.lower():
        contador += 1
print(f"La cantidad de clientes de {localidad_buscada} es {contador}.")

# 2. Calcular deuda según condición
limite = float(input("Ingrese un monto para comparar deudas: "))
condicion = input("¿Desea ver clientes con deuda mayor o menor? (mayor/menor): ")

total = 0
for cliente in clientes:
    if condicion == "mayor" and cliente[2] > limite:
        total += cliente[2]
    elif condicion == "menor" and cliente[2] < limite:
        total += cliente[2]

print(f"El total de deuda acumulada de los clientes que deben {condicion} a {int(limite)} pesos es ${int(total)}")

# 3. Guardar apellidos de clientes con DNI mayor a un límite
dni_limite = int(input("Ingrese un número de DNI: "))
with open("apellidos.txt", "w", encoding="utf-8") as salida:
    salida.write(f"Apellidos de los clientes con DNI mayor a {dni_limite}\n")
    for cliente in clientes:
        if cliente[0] > dni_limite:
            salida.write(cliente[4] + "\n")

print("Archivo 'apellidos.txt' generado correctamente.")

