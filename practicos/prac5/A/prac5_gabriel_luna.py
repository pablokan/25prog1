def cargar_clientes(nombre_archivo):
    clientes = []
    with open(nombre_archivo, encoding="utf-8") as archivo:
        primera_linea = True
        for linea in archivo:
            if primera_linea:
                primera_linea = False
                continue  
            partes = linea.strip().split("#")
            dni = int(partes[0])
            nombre_apellido = partes[1]
            deuda = int(partes[2])
            localidad = partes[3]
            apellido = nombre_apellido.split()[-1]
            cliente = {
                "dni": dni,
                "nombre": nombre_apellido,
                "apellido": apellido,
                "deuda": deuda,
                "localidad": localidad
            }
            clientes.append(cliente)
    return clientes
def contar_por_localidad(clientes, localidad):
    contador = 0
    for cliente in clientes:
        if cliente["localidad"] == localidad:
            contador += 1
    return contador

def deuda_mayor_a(clientes, monto):
    total = 0
    for cliente in clientes:
        if cliente["deuda"] > monto:
            total += cliente["deuda"]
    return total
def guardar_apellidos_dni_mayor(clientes, dni_limite, archivo_salida):
    with open(archivo_salida, "w", encoding="utf-8") as salida:
        salida.write("apellidos de los clientes con DNI mayor a " + str(dni_limite) + "\n")
        for cliente in clientes:
            if cliente["dni"] > dni_limite:
                salida.write(cliente["apellido"] + "\n")


clientes = cargar_clientes("clientes.txt")
#1) La cantidad de clientes de ...
localidad_usuario = input("ingrese una localidad: ")
cantidad = contar_por_localidad(clientes, localidad_usuario)
print("la cantidad de clientes de " + localidad_usuario + " es: " + str(cantidad))
print()
#2) El total de deuda acumulada de los clientes que deben ...
monto_usuario = int(input("ingrese un monto para calcular el total de deuda: "))
total_deuda = deuda_mayor_a(clientes, monto_usuario)
print("la deuda acumulada de clientes que deben más de " + str(monto_usuario) + " es: " + str(total_deuda))
print()
#3) Los apellidos de los clientes cuyos DNI sean mayores a ... (esta salida DEBE grabarse en un archivo llamado apellidos.txt) 

dni_usuario = int(input(" los pellidos de los clientes con DNI mayor a (ingresar un nro) : "))
guardar_apellidos_dni_mayor(clientes, dni_usuario, "apellidos.txt")
print("se creo un archivo llamado apellidos.txt con el resultado")