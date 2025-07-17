#Practico 5

from foo import cargar_clientes, contar_localidad, sumar_deuda, apellidos_por_DNI

# Cargar datos
clientes = cargar_clientes("clientes.txt")

# Actividad 1
print("1) Cantidad de clientes por localidad:\n")
print(f"La cantidad de clientes de La Carlota es: {contar_localidad(clientes, 'La Carlota')}")

localidad = input("Ingrese otra localidad: ").title()
print(f"La cantidad de clientes de {localidad} es: {contar_localidad(clientes, localidad)}\n")

# Actividad 2
print("2) Total de deuda acumulada:\n")
limite = int(input("Ingrese monto mínimo para sumar deudas: "))
print(f"Deuda total de clientes con más de {limite}: ${sumar_deuda(clientes, limite)}\n")

limite = int(input("Ingrese monto máximo para sumar deudas: "))
print(f"Deuda total de clientes con menos de {limite}: ${sumar_deuda(clientes, limite, menores=True)}\n")

# Actividad 3
print("3) Apellidos de clientes con DNI mayor o igual a cierto valor:\n")
limite_DNI = int(input("Ingrese DNI mínimo: "))
apellidos = apellidos_por_DNI(clientes, limite_DNI)
print("")
for apellido in apellidos:
    print(apellido)

with open("apellidos.txt", "w", encoding="utf-8") as file:
    for apellido in apellidos:
        file.write(f"{apellido}\n")

print("\nDatos guardados correctamente.\n")