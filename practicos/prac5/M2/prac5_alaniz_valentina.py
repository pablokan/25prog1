# prac5_alaniz_valentina.py

# contar la cantidad de clientes que viven en una localidad dada
def contar_clientes(localidad):
    cantidad = 0  # iniciar contador en cero
    # abrir el archivo clientes.txt en modo lectura con encoding utf-8
    with open("clientes.txt", "r", encoding="utf-8") as archivo:
        next(archivo)  # saltar la primera línea (encabezado)
        # recorrer línea por línea el archivo
        for linea in archivo:
            # eliminar espacios al principio y final, y separar por '#'
            partes = linea.strip().split("#")
            # verificar que la línea tenga al menos 4 elementos (dni, nombre, deuda, localidad)
            if len(partes) < 4:
                continue  # saltar esta línea si está incompleta
            # comparar la localidad leída con la localidad buscada (ignorar mayúsculas)
            if partes[3].strip().lower() == localidad.lower():
                cantidad += 1  # aumentar el contador en 1
    return cantidad  # devolver la cantidad total encontrada

# sumar la deuda total de clientes según si es mayor o menor a un monto dado
def sumar_deudas(monto, condicion):
    total = 0  # iniciar acumulador de deuda en cero
    # abrir el archivo clientes.txt en modo lectura con encoding utf-8
    with open("clientes.txt", "r", encoding="utf-8") as archivo:
        next(archivo)  # saltar la primera línea (encabezado)
        # recorrer línea por línea el archivo
        for linea in archivo:
            # eliminar espacios al principio y final, y separar por '#'
            partes = linea.strip().split("#")
            # verificar que la línea tenga al menos 3 elementos (dni, nombre, deuda)
            if len(partes) < 3:
                continue  # saltar línea si está incompleta
            try:
                # convertir la deuda de texto a número decimal
                deuda = float(partes[2])
            except ValueError:
                continue  # saltar línea si la deuda no es un número válido
            # sumar la deuda si es mayor que el monto dado y la condición es "mayor"
            if condicion == "mayor" and deuda > monto:
                total += deuda
            # sumar la deuda si es menor que el monto dado y la condición es "menor"
            elif condicion == "menor" and deuda < monto:
                total += deuda
    return total  # devolver el total acumulado

# guardar en un archivo llamado apellidos.txt los apellidos de clientes con DNI mayor a un límite dado
def guardar_apellidos(dni_limite):
    # abrir clientes.txt para leer y apellidos.txt para escribir, con encoding utf-8
    with open("clientes.txt", "r", encoding="utf-8") as archivo, \
         open("apellidos.txt", "w", encoding="utf-8") as salida:
        # escribir la línea de encabezado en el archivo de salida
        salida.write(f"Apellidos de los clientes con DNI mayor a {dni_limite}\n")
        next(archivo)  # saltar la primera línea (encabezado)
        # recorrer línea por línea el archivo de clientes
        for linea in archivo:
            # eliminar espacios y separar por '#'
            partes = linea.strip().split("#")
            # verificar que la línea tenga al menos 2 elementos (dni, nombre)
            if len(partes) < 2:
                continue  # saltar línea incompleta
            try:
                # convertir el DNI a número entero
                dni = int(partes[0])
            except ValueError:
                continue  # saltar línea si DNI no es válido
            # si el DNI es mayor al límite indicado
            if dni > dni_limite:
                # obtener el apellido como la última palabra del nombre completo
                apellido = partes[1].strip().split()[-1]
                # escribir el apellido en el archivo apellidos.txt con salto de línea
                salida.write(apellido + "\n")

# =========================
# EJEMPLOS DE USO DEL PROGRAMA
# =========================

# mostrar la cantidad de clientes que viven en La Carlota
print("La cantidad de clientes de La Carlota es", contar_clientes("La Carlota"))

# mostrar la cantidad de clientes que viven en Sampacho
print("La cantidad de clientes de Sampacho es", contar_clientes("Sampacho"))

# mostrar el total de deuda de clientes que deben más de 90.000 pesos
print("El total de deuda de los que deben más de 90000 es $", int(sumar_deudas(90000, "mayor")))

# mostrar el total de deuda de clientes que deben menos de 40.000 pesos
print("El total de deuda de los que deben menos de 40000 es $", int(sumar_deudas(40000, "menor")))

# generar el archivo apellidos.txt con los apellidos de clientes con DNI mayor a 40.000.000
guardar_apellidos(40000000)
print("Se guardaron los apellidos en el archivo apellidos.txt")
