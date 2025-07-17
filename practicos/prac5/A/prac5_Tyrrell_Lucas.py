def contar_clientes_por_localidad(archivo, localidad):
    print('-' * 80)
    print(f'Buscando clientes en la localidad: {localidad}')
    
    with open(archivo, encoding='utf-8') as f:
        lineas = f.readlines()

    total = 0
    lineas.pop(0)
    for linea in lineas:
        partes = linea.strip().split('#')
        loc = partes[3].strip().lower()
        if loc == localidad.lower():
            total += 1
    
    print(f'La cantidad de clientes de {localidad}: {total}')


def total_deuda_acumulada(archivo, limite, condicion='mayor'):
    print('-' * 80)
    print(f'Calculando deuda de clientes con condición: {condicion} a {limite}')
    
    with open(archivo, encoding='utf-8') as f:
        lineas = f.readlines()
    
    total = 0
    for linea in lineas:
        partes = linea.strip().split('#')
        deuda_str = partes[2]
        deuda = float(deuda_str)
        if condicion == 'mayor' and deuda > limite:
            total += deuda
        elif condicion == 'menor' and deuda < limite:
            total += deuda

    texto = 'más de' if condicion == 'mayor' else 'menos de'
    print(f'El total de deuda acumulada de clientes que deben {texto} {limite:,.0f} pesos: ${int(total):,}')


def guardar_apellidos_dni_mayor(archivo, dni_minimo):
    print('-' * 80)
    print(f'Guardando apellidos de clientes con DNI mayor a {dni_minimo} en "apellidos.txt"')
    
    with open(archivo, encoding='utf-8') as f:
        lineas = f.readlines()
    
    apellidos = []
    for linea in lineas:
        partes = linea.strip().split('#')
        dni = int(partes[0])
        if dni > dni_minimo:
            nombre_apellido = partes[1].strip()
            apellido = nombre_apellido.split()[-1]
            apellidos.append(apellido)
    
    with open('apellidos.txt', 'w', encoding='utf-8') as salida:
        salida.write(f'Apellidos de los clientes con DNI mayor a {dni_minimo}\n')
        for a in apellidos:
            salida.write(f'{a}\n')
    
    print(f'{len(apellidos)} apellidos guardados.')

contar_clientes_por_localidad('clientes.txt', 'La Carlota')

otra_localidad = input('Ingrese otra localidad: ')
contar_clientes_por_localidad('clientes.txt', otra_localidad)

total_deuda_acumulada('clientes.txt', 90000, condicion='mayor')
total_deuda_acumulada('clientes.txt', 40000, condicion='menor')

guardar_apellidos_dni_mayor('clientes.txt', 40000000)


