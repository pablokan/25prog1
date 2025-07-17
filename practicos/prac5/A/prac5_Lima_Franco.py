# Clientes

#Actividad 1 
'''
1) La cantidad de clientes de (localidad literal y variable)

1) La cantidad de clientes de La Carlota es 4.
   Ingrese otra localidad: Sampacho
   La cantidad de clientes de Sampacho es 5.
'''

def cantidad_clientes():
    archivo = 'clientes.txt'
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    localidad1 = 'La Carlota'
    contador1 = 0
    localidad2 = ''
    contador2 = 0

    for i in range(1, len(lineas)):
        linea = lineas[i]
        if linea[-1] == '\n':
            linea = linea[:-1]
        localidad = linea.split('#')[3]

        if localidad == localidad1:
            contador1 += 1

    print(f'1) La cantidad de clientes de {localidad1} es {contador1}.')

    localidad2 = input('Ingrese otra localidad: ')

    for i in range(1, len(lineas)):
        linea = lineas[i]
        if linea[-1] == '\n':
            linea = linea[:-1]
        localidad = linea.split('#')[3]

        if localidad == localidad2:
            contador2 += 1

    print(f'   La cantidad de clientes de {localidad2} es {contador2}.')



   
# Actividad 2
'''
2) El total de deuda acumulada de los clientes que deben (mas o menos que)
2) El total de deuda acumulada de los clientes que deben mas de $90.000 pesos es $1841808
   El total de deuda acumulada de los clientes que deben menos de $40.000 es $150220
'''

def total_acumulado():
    archivo = 'clientes.txt'
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    total_mayor = 0
    total_menor = 0

    for i in range(1, len(lineas)):
        linea = lineas[i]
        if linea[-1] == '\n':
            linea = linea[:-1]
        deuda = int(linea.split('#')[2])

        if deuda > 90000:
            total_mayor += deuda
        elif deuda < 40000:
            total_menor += deuda

    print(f'2) El total de deuda acumulada de los clientes que deben más de $90.000 pesos es ${total_mayor}')
    print(f'   El total de deuda acumulada de los clientes que deben menos de $40.000 es ${total_menor}')



#Actividad 3
''' 
3) Los apellidos de los clientes cuyos DNI seas mayores a (esta salida DEBE grabarse en un archivo llamado apellidos.txt)
3) Ejemplo de contenido del archivo apellidos.txt:
   Apellidos de los clientes con DNI mayor a 40000000
   Raynard
   Dominetti
   Aronsohn
   Farrell
   Dumingo
   Mingauld
'''

def guardar_apellidos_por_dni(archivo_entrada, archivo_salida, dni_limite):

    with open(archivo_entrada, 'r') as entrada:
        lineas = entrada.readlines()
    with open(archivo_salida, 'w') as salida:
        salida.write(f'Apellidos de los clientes con DNI mayor a {dni_limite}\n')
        for i in range(1, len(lineas)):
            linea = lineas[i]
            if linea[-1] == '\n':
                linea = linea[:-1]
            datos = linea.split('#')
            dni = int(datos[0])
            if dni > dni_limite:
                apellido = datos[1].split()[1]
                salida.write(apellido + '\n')

def apellidos_clientes():

    archivo = 'clientes.txt'
    archivo_salida = 'apellidos.txt'
    dni_limite = 40000000

    guardar_apellidos_por_dni(archivo, archivo_salida, dni_limite)
    print(f'Se creó el archivo {archivo_salida} con los apellidos de clientes con DNI mayor a {dni_limite}.')


if __name__ == '__main__':
    cantidad_clientes()
    print()
    total_acumulado()
    print()
    apellidos_clientes()
