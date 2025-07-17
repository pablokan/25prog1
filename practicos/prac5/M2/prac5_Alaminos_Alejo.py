def cantidad_clientes_por_localidad(nombre_archivo, localidad_buscada):
    contador = 0
    with open(nombre_archivo, encoding='utf-8') as archivo:
        next(archivo)  
        for linea in archivo:
            partes = linea.strip().split('#')
            if len(partes) == 4 and partes[3] == localidad_buscada:
                contador += 1
    return contador

def deuda_total_por_condicion(nombre_archivo, monto, mayor=True):
    total = 0
    with open(nombre_archivo, encoding='utf-8') as archivo:
        next(archivo)  
        for linea in archivo:
            partes = linea.strip().split('#')
            if len(partes) == 4:
                deuda = int(partes[2])
                if (mayor and deuda > monto) or (not mayor and deuda < monto):
                    total += deuda
    return total

def guardar_apellidos_por_dni(nombre_archivo, dni_minimo, archivo_salida='apellidos.txt'):
    with open(nombre_archivo, encoding='utf-8') as archivo, open(archivo_salida, 'w', encoding='utf-8') as salida:
        salida.write(f"Apellidos de los clientes con DNI mayor a {dni_minimo}\n\n")
        next(archivo)
        for linea in archivo:
            partes = linea.strip().split('#')
            if len(partes) == 4:
                dni = int(partes[0])
                if dni > dni_minimo:
                    apellido = partes[1].split()[-1]
                    salida.write(f"{apellido}\n")

#(Punto 1 y 2 ejemplo de consigna)
archivo_clientes = 'clientes.txt'


localidad_1 = 'La Carlota'
print(f"La cantidad de clientes de {localidad_1} es {cantidad_clientes_por_localidad(archivo_clientes, localidad_1)}.")
localidad_2 = 'Sampacho'
print(f"La cantidad de clientes de {localidad_2} es {cantidad_clientes_por_localidad(archivo_clientes, localidad_2)}.")


print(f"El total de deuda acumulada de los clientes que deben más de 90000 pesos es ${deuda_total_por_condicion(archivo_clientes, 90000, mayor=True)}")
print(f"El total de deuda acumulada de los clientes que deben menos de 40000 es ${deuda_total_por_condicion(archivo_clientes, 40000, mayor=False)}")

# Punto 3: generar archivo con apellidos
guardar_apellidos_por_dni(archivo_clientes, 40000000)