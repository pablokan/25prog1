
def contador_por_filtrado(lineas_de_datos, pedir_localidad_usuario, pedir_total_deuda_mas, pedir_dni_referencia, pedir_total_deuda_menos):
    fila_encabezados = lineas_de_datos[0].split(',')
    indice_localidad = fila_encabezados.index('localidad')
    indice_deuda = fila_encabezados.index('monto de deuda en pesos')
    indice_dni = fila_encabezados.index('DNI')
    indice_nombre = fila_encabezados.index('nombre y apellido')

    apellidos_dni_mayores = []
    deuda_total_mas = 0
    deuda_total_menos = 0

    contador = 0
    for linea in lineas_de_datos[1:]:
        linea_dividida = linea.split('#')
        if pedir_localidad_usuario == linea_dividida[indice_localidad]:
            contador += 1

        if pedir_total_deuda_mas < int(linea_dividida[indice_deuda]):
            deuda_total_mas += int(linea_dividida[indice_deuda])
        
        if pedir_total_deuda_menos > int(linea_dividida[indice_deuda]):
            deuda_total_menos += int(linea_dividida[indice_deuda])

        if int(linea_dividida[indice_dni]) > pedir_dni_referencia:
            nombres_apellidos = linea_dividida[indice_nombre]
            apellidos = nombres_apellidos.split(' ')
            print(apellidos[1])
            apellidos_dni_mayores.append(apellidos[1])


    return contador, deuda_total_mas, deuda_total_menos, apellidos_dni_mayores
