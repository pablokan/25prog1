personas = []
with open('clientes.txt', 'r', encoding='utf-8') as archivo:
    next(archivo)
    for linea in archivo:
        partes = linea.strip().split('#')
        if len(partes) == 4:
            dni = int(partes[0])
            nombre_apellido = partes[1]
            deuda = float(partes[2])
            localidad = partes[3]
            apellido = nombre_apellido.split()[-1]
            personas.append([dni, nombre_apellido, deuda, localidad, apellido])
def clientes_por_localidad(personas, localidad='La Carlota'):
    contador = 0
    for cliente in personas:
        if cliente[3].lower() == localidad.lower():
            contador += 1
    print(f'La cantidad de clientes de {localidad} es {contador}.')    
def cant_clientes_mayores_deuda(personas, limite, condicion):
    contador = 0
    total = 0
    for cliente in personas:
        if condicion == 'mas':
            if cliente[2] > limite:
                contador += 1
                total+= cliente[2]
        elif condicion == 'menos':
            if cliente[2] < limite:
                contador += 1
                total+= cliente[2]
    print(f'El total de deuda acumulada de los clientes que deben {condicion} de {int(limite)} pesos es ${int(total)}')
with open('apellidos.txt', 'w', encoding='utf-8') as salida:
    salida.write(f'Apellidos de los clientes con DNI mayor a 40000000 \n')
    for cliente in personas:
        if cliente[0] > 40000000:
            salida.write(cliente[4] + '\n')
def main ():
    clientes_por_localidad(personas)
    localidad = input('Ingrese una localidad: ')
    clientes_por_localidad(personas, localidad)
    limite = float(input('Ingrese un monto para comparar deudas: '))
    condicion = input('¿Desea ver clientes con deuda mas o menos? (mas/menos): ')
    cant_clientes_mayores_deuda(personas, limite, condicion)
    limite = float(input('Ingrese un monto para comparar deudas: '))
    condicion = input('¿Desea ver los clientes con deuda mas alta o menos alta? (mas/menos): ')
    cant_clientes_mayores_deuda(personas, limite, condicion)  
if __name__ == '__main__':
    main()