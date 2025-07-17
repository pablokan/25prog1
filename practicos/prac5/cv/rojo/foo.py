#Funciones del Practico 5
    
def cargar_clientes(nombre_archivo):
    clientes = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        encabezado = archivo.readline().strip().split(",")
        for linea in archivo:
            partes = linea.strip().split("#")
            if len(partes) == len(encabezado):
                cliente = {}
                for i in range(len(encabezado)):
                    cliente[encabezado[i]] = partes[i]
                clientes.append(cliente)
    return clientes

def contar_localidad(clientes, localidad):
    return sum(1 for cliente in clientes if cliente["localidad"].title() == localidad.title())

def sumar_deuda(clientes, limite, menores=False):
    total = 0
    for cliente in clientes:
        deuda = int(cliente["monto de deuda en pesos"])
        if (menores and deuda < limite) or (not menores and deuda > limite):
            total += deuda
    return total

def apellidos_por_DNI(clientes, minimo_DNI):
    apellidos = []
    for cliente in clientes:
        if int(cliente["DNI"]) >= minimo_DNI:
            apellido = cliente["nombre y apellido"].split(" ")[-1]
            apellidos.append(apellido)
    return apellidos