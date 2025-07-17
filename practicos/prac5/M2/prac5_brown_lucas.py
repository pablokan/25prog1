def contar_clientes_por_localidad(ruta_archivo, localidad):
    """
    Cuenta la cantidad de clientes de una localidad dada.

    Args:
        ruta_archivo (str): Ruta al archivo de clientes.
        localidad (str): Localidad a buscar.

    Returns:
        int: Cantidad de clientes de la localidad.
    """
    cantidad = 0
    with open(ruta_archivo, encoding="utf-8") as f:
        _ = f.readline()  # Saltar encabezado
        for linea in f:
            partes = linea.strip().split("#")
            if len(partes) < 4:
                continue
            if partes[3].strip().lower() == localidad.strip().lower():
                cantidad += 1
    return cantidad

def total_deuda_filtrada(ruta_archivo, condicion="mas", monto=0):
    """
    Suma el total de deuda de los clientes según si deben más o menos que el monto dado.

    Args:
        ruta_archivo (str): Ruta al archivo de clientes.
        condicion (str): "mas" o "menos".
        monto (int or float): Monto límite.

    Returns:
        int: Total de deuda acumulada.
    """
    total = 0
    with open(ruta_archivo, encoding="utf-8") as f:
        _ = f.readline()  # Saltar encabezado
        for linea in f:
            partes = linea.strip().split("#")
            if len(partes) < 3:
                continue
            try:
                deuda = int(partes[2])
            except ValueError:
                continue
            if condicion == "mas" and deuda > monto:
                total += deuda
            elif condicion == "menos" and deuda < monto:
                total += deuda
    return total

def guardar_apellidos_dni_mayor_a(ruta_archivo, dni_limite, ruta_salida="apellidos.txt"):
    """
    Guarda los apellidos de clientes cuyo DNI sea mayor al valor dado, en un archivo.

    Args:
        ruta_archivo (str): Ruta al archivo de clientes.
        dni_limite (int): DNI límite.
        ruta_salida (str): Archivo de salida para los apellidos.
    """
    apellidos = []
    with open(ruta_archivo, encoding="utf-8") as f:
        _ = f.readline()
        for linea in f:
            partes = linea.strip().split("#")
            if len(partes) < 2:
                continue
            try:
                dni = int(partes[0])
            except ValueError:
                continue
            if dni > dni_limite:
                nombre_apellido = partes[1].strip()
                apellido = nombre_apellido.split()[-1]
                apellidos.append(apellido)
    with open(ruta_salida, "w", encoding="utf-8") as out:
        out.write(f"Apellidos de los clientes con DNI mayor a {dni_limite}\n")
        for apellido in apellidos:
            out.write(f"{apellido}\n")

# Ejemplo de uso 1: cantidad de clientes por localidad
localidad1 = "La Carlota"
cant1 = contar_clientes_por_localidad("clientes.txt", localidad1)
print(f"La cantidad de clientes de {localidad1} es {cant1}.")

localidad2 = "Sampacho"
cant2 = contar_clientes_por_localidad("clientes.txt", localidad2)
print(f"La cantidad de clientes de {localidad2} es {cant2}.")

# Ejemplo de uso 2: total de deuda filtrada
monto_mas = 90000
total_mas = total_deuda_filtrada("clientes.txt", condicion="mas", monto=monto_mas)
print(f"El total de deuda acumulada de los clientes que deben más de {monto_mas} pesos es ${total_mas}")

monto_menos = 40000
total_menos = total_deuda_filtrada("clientes.txt", condicion="menos", monto=monto_menos)
print(f"El total de deuda acumulada de los clientes que deben menos de {monto_menos} es ${total_menos}")

# Ejemplo de uso 3: guardar apellidos de clientes con DNI mayor a cierto valor
guardar_apellidos_dni_mayor_a("clientes.txt", 40000000, "apellidos.txt")
print("Archivo apellidos.txt generado.")    