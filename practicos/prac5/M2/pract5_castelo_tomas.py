# Practico 5: Archivos

localidad_literal = "La Carlota"
cant_clientes_localidad = 0

with open("clientes.txt", "r", encoding="utf-8") as file:
    lineas = file.readlines()[1:]
    for linea in lineas:
        datos = linea.strip().split("#")

        localidad = datos[3]

        if localidad == localidad_literal:
            cant_clientes_localidad += 1

print(f"\n1) Cantidad de clientes en '{localidad_literal}': {cant_clientes_localidad}")

localidad_variable = input("Ingrese otra localidad: ")
deuda_limite = int(input("Ingrese el monto de deuda: "))
comparacion = input("¿Desea filtrar por deuda mayor o menor al limite? (mayor/menor): ")
dni_limite = int(input("Ingrese el número de DNI: "))

cant_clientes_localidad = 0
total_deuda_filtrada = 0
apellidos_guardar = []

with open("clientes.txt", "r", encoding="utf-8") as file:
    lineas = file.readlines()[1:]

    for linea in lineas:
        datos = linea.strip().split("#")

        if len(datos) == 4:
            dni = int(datos[0])
            nombre_apellido = datos[1]
            deuda = int(datos[2])
            localidad = datos[3]

        if localidad == localidad_variable:
            cant_clientes_localidad += 1

        if comparacion == "mayor" and deuda > deuda_limite:
            total_deuda_filtrada += deuda
        elif comparacion == "menor" and deuda < deuda_limite:
            total_deuda_filtrada += deuda

        if dni > dni_limite:
            apellido = nombre_apellido.split()[-1]
            apellidos_guardar.append(apellido)

print(f"\nCantidad de clientes en '{localidad_variable}': {cant_clientes_localidad}")
print(f"\n2) El total de deuda acumulada de los clientes que deben mas de {deuda_limite} pesos es: ${total_deuda_filtrada}")

with open("apellidos.txt", "w", encoding="utf-8") as file:
    for apellido in apellidos_guardar:
        file.write(apellido + "\n")

print(f"\n3) Apellidos de los clientes con dni mayor a {dni_limite}")
with open("apellidos.txt", "r", encoding="utf-8") as file:
    contenido = file.read()
    print(contenido)
