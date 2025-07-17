def cantidad_clientes(nombre_archivo, localidad_buscada):
    contador_localidad = 0
        
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    for cliente in lineas:
        partes = cliente.strip().split('#')    
        if len(partes) == 4:
            localidad = partes[3].strip().lower()
            if localidad == localidad_buscada.lower():
                contador_localidad += 1
    return(contador_localidad)

def deuda(nombre_archivo, monto_condicion):
    deuda_mayor = 0
    deuda_menor = 0
    
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    for cliente in lineas:
        partes = cliente.strip().split('#')        
        if len(partes) == 4:           
            monto = int(partes[2].strip())                     
            if monto >= monto_condicion:
                deuda_mayor += monto
            elif monto <= monto_condicion:
                deuda_menor += monto
    return(deuda_mayor, deuda_menor)
            
def apellidos_clientes (nombre_archivo , dni_buscado):
    apellidos = []
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    for cliente in lineas:
        partes = cliente.strip().split('#')
        
        if len(partes) == 4:
            dni = int(partes[0].strip())  
            apellido = partes[1].split()[-1] 
            if dni > dni_buscado:
                apellidos.append(apellido)
    
    with open("apellidos.txt", "w") as archivo_apellidos:
        for apellido in apellidos:
            archivo_apellidos.write(apellido + "\n")
    return(apellidos)


archivo = "clientes.txt"
#1)La cantidad de clientes de ... (localidad literal y variable)
#Literal
localidad_lit = "La Carlota"
clientes_localidad_lite = cantidad_clientes(archivo, localidad_lit)
print(f'La cantidad de clientes de {localidad_lit} es {clientes_localidad_lite}')

#Variable
localidad_var = input("Ingrese otra localidad: ")
clientes_localidad_var = cantidad_clientes(archivo,localidad_var)
print(f'La cantidad de clientes de {localidad_var} es {clientes_localidad_var}')
#2)El total de deuda acumulada de los clientes que deben ... (mas o menos que)
#Mayor a...
monto_may_ing = int(input("Ingrese un monto: "))
deuda_mayor_a,_ = deuda(archivo, monto_may_ing)
print(f"El total de deuda acumulada de los clientes que deben mas de ${monto_may_ing} es de ${deuda_mayor_a}")
#Menor a ...
monto_men_ing = int(input("Ingrese un monto: "))
_, deuda_menor_a = deuda(archivo, monto_men_ing)
print(f"El total de deuda acumulada de los clientes que deben mas de ${monto_men_ing} es de ${deuda_menor_a}")

#3)Los apellidos de los clientes cuyos DNI sean mayores a ...
dni_a_buscar = int(input("Ingrese un DNI: "))
apellidos_de_clientes = apellidos_clientes(archivo,dni_a_buscar)
print(apellidos_de_clientes)