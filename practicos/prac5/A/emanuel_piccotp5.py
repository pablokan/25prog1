import unicodedata

def count_clients_by_locality(filename, locality):
    count = 0
    with open(filename, "r", encoding="utf-8") as entrada:
        next(entrada)  # Salta la línea de encabezado
        for linea in entrada:
            partes = linea.strip().split("#")
            if len(partes) == 4 and partes[3].strip().lower() == locality.lower():
                count += 1
    return count

def total_debt_by_condition(filename, limit, greater=True):
    total = 0
    with open(filename, "r", encoding="utf-8") as entrada:
        next(entrada)  # Salta la línea de encabezado
        for linea in entrada:
            partes = linea.strip().split("#")
            if len(partes) == 4:
                try:
                    deuda = float(partes[2])
                    if (greater and deuda > limit) or (not greater and deuda < limit):
                        total += deuda
                except ValueError:
                    continue
    return total

def save_surnames_by_dni(filename, dni_limit, output_file="apellidos.txt"):
    with open(filename, "r", encoding="utf-8") as entrada, \
         open(output_file, "w", encoding="utf-8") as salida:
        next(entrada)  # Salta la línea de encabezado
        salida.write(f"Apellidos de los clientes con DNI mayor a {dni_limit}\n")
        for linea in entrada:
            partes = linea.strip().split("#")
            if len(partes) == 4:
                try:
                    dni = int(partes[0])
                    if dni > dni_limit:
                        apellido = partes[1].strip().split()[-1]
                        salida.write(apellido + "\n")
                except ValueError:
                    continue

# Ejemplo punto 1
localidad1 = "La Carlota"
cantidad1 = count_clients_by_locality("clientes.txt", localidad1)
print(f"La cantidad de clientes de {localidad1} es {cantidad1}.")

localidad2 = input("Ingrese otra localidad: ")
cantidad2 = count_clients_by_locality("clientes.txt", localidad2)
print(f"La cantidad de clientes de {localidad2} es {cantidad2}.")

# Ejemplo punto 2
limite1 = 90000
total1 = total_debt_by_condition("clientes.txt", limite1, greater=True)
print(f"El total de deuda acumulada de los clientes que deben más de {limite1} pesos es ${int(total1)}")

limite2 = 40000
total2 = total_debt_by_condition("clientes.txt", limite2, greater=False)
print(f"El total de deuda acumulada de los clientes que deben menos de {limite2} es ${int(total2)}")

# Punto 3
dni_limite = 40000000
save_surnames_by_dni("clientes.txt", dni_limite)
print(f"Los apellidos de los clientes con DNI mayor a {dni_limite} se han guardado en apellidos.txt.")