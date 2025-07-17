from foo import contador_por_filtrado

'''Quiero obtener:
La cantidad de clientes de ... (localidad literal y variable)
El total de deuda acumulada de los clientes que deben ... (mas o menos que)
Los apellidos de los clientes cuyos DNI sean mayores a ... (esta salida DEBE grabarse en un archivo llamado apellidos.txt)'''

with open('clientes.txt', 'r', encoding='utf-8') as clientes:
    lineas_de_datos = clientes.read().split('\n')
    pedir_localidad_usuario = input('Ingresa localidad a buscar => ').title()
    print("=" * 30)
    pedir_total_deuda_mas = int(input('Ingresa deuda total mayor que => '))
    print("=" * 30)
    pedir_total_deuda_menos = int(input('Ingresar deuda total menor que => '))
    print("=" * 30)
    pedir_dni_referencia = int(input('Ingresa DNi de referencia => '))
    print("=" * 30)

    datos_registrados = contador_por_filtrado(lineas_de_datos, pedir_localidad_usuario, pedir_total_deuda_mas, pedir_dni_referencia, pedir_total_deuda_menos)
    
    print(f'1) El total de personas de {pedir_localidad_usuario} son: {datos_registrados[0]}')
    print(f'''2) El total de deuda acumulada de los clientes que deben mas de {pedir_total_deuda_mas} es de {datos_registrados[1]}.
El total de deuda acumulada de los clientes que deben menos de {pedir_total_deuda_menos} es de {datos_registrados[2]}''')
    
    #guardar en archivo
    with open('apellidos.txt', 'w') as apellidos:
        for l in datos_registrados[3]:
            apellidos.write(l + '\n')