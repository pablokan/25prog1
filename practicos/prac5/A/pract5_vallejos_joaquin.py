'''
Tengo un archivo clientes.txt con los siguientes datos de clientes:
DNI, nombre y apellido, monto de deuda en pesos y localidad.

Quiero obtener:
1) La cantidad de clientes de ... (localidad literal y variable)
2) El total de deuda acumulada de los clientes que deben ... (mas o menos que)
3) Los apellidos de los clientes cuyos DNI sean mayores a ... (esta salida DEBE grabarse en un archivo llamado apellidos.txt) 
'''

with open('clientes.txt') as textoClientes:
    data = textoClientes.readlines()  

def cantidadClientes(localidadBuscar):
    contadorCliente = 0
    for dataClientes in data[1:]: 
        dni, nombreApellido, deuda, localidad = dataClientes.strip().split('#')
        dni = int(dni)
        if localidad == localidadBuscar:
            contadorCliente += 1
    print(f"1) La cantidad de clientes de {localidadBuscar} es {contadorCliente}")

cantidadClientes("Sampacho")
cantidadClientes("La Carlota")

def totalDeuda(montoMenosQue, montoMasQue):
    sumaDeudaMas = 0
    sumaDeudaMenos = 0
    for dataClientes in data[1:]: 
        dni, nombreApellido, deuda, localidad = dataClientes.strip().split('#')
        deuda = int(deuda)
        if montoMasQue > deuda:
            sumaDeudaMas += deuda
        if montoMenosQue < deuda:
            sumaDeudaMenos += deuda
    print(f'2) El total de deuda acumulada de los clientes que deben más de {montoMasQue} pesos es ${sumaDeudaMas}')
    print(f'2) El total de deuda acumulada de los clientes que deben menos de {montoMenosQue} pesos es ${sumaDeudaMenos}')

totalDeuda(40000, 90000)
totalDeuda(10000, 40000)

def apellidosAguardar(dniMinimo):
    apellidos = []
    for dataClientes in data[1:]: 
        dni, nombreApellido, deuda, localidad = dataClientes.strip().split('#')
        dni = int(dni)
        if dni > dniMinimo:
            apellido = nombreApellido.split()[1]
            apellidos.append(apellido)
    apellidosStr = ", ".join(apellidos)
    with open('apellidos.txt', 'w') as archApellidos:
        for apellido in apellidos:
            archApellidos.write(apellido + '\n' )
    print(f'3) Ejemplo de contenido del archivo apellidos.txt:')
    print(f'Apellidos de los clientes con DNI mayor a {dniMinimo}: {apellidosStr}')
apellidosAguardar(40000000)