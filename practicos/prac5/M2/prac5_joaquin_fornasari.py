def cargar_clientes(nombre_archivo):
    clientes = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        next(archivo)
        for linea in archivo:
            partes = linea.strip().split('#')
            if len(partes) == 4:
                dni = int(partes[0])
                nombre_apellido = partes[1]
                deuda = float(partes[2])
                localidad = partes[3]
                clientes.append((dni, nombre_apellido, deuda, localidad))
    return clientes

def cantidad_clientes_localidad(clientes, localidad):
    return sum(1 for c in clientes if c[3].lower() == localidad.lower())

def deuda_total(clientes, monto, condicion='mayor'):
    if condicion == 'mayor':
        return sum(c[2] for c in clientes if c[2] > monto)
    else:
        return sum(c[2] for c in clientes if c[2] < monto)

def guardar_apellidos_dni_mayor(clientes, dni_limite, nombre_salida='apellidos.txt'):
    with open(nombre_salida, 'w', encoding='utf-8') as archivo:
        archivo.write(f"Apellidos de los clientes con DNI mayor a {dni_limite}\n")
        for c in clientes:
            if c[0] > dni_limite:
                apellido = c[1].split()[-1]
                archivo.write(f"{apellido}\n")

def main():
    clientes = cargar_clientes("clientes.txt")
    print(f"La cantidad de clientes de La Carlota es {cantidad_clientes_localidad(clientes, 'La Carlota')}")
    print(f"La cantidad de clientes de Sampacho es {cantidad_clientes_localidad(clientes, 'Sampacho')}")
    print(f"El total de deuda acumulada de los clientes que deben más de 90000 pesos es ${deuda_total(clientes, 90000, 'mayor'):.0f}")
    print(f"El total de deuda acumulada de los clientes que deben menos de 40000 pesos es ${deuda_total(clientes, 40000, 'menor'):.0f}")
    guardar_apellidos_dni_mayor(clientes, 40000000)
    print("Se creó el archivo apellidos.txt con los apellidos de clientes cuyo DNI es mayor a 40000000.")

    print("\n Modo interactivo")
    localidad_input = input("Ingrese una localidad: ")
    print(f"La cantidad de clientes de {localidad_input} es {cantidad_clientes_localidad(clientes, localidad_input)}")

    monto = float(input("Ingrese un monto de deuda: "))
    tipo = input("¿Quiere ver los que deben más o menos que ese monto? (mas/menos): ").lower()
    condicion = 'mayor' if tipo == 'mas' else 'menor'
    print(f"El total de deuda acumulada de los clientes que deben {tipo} de {monto:.0f} pesos es ${deuda_total(clientes, monto, condicion):.0f}")

    dni_limite = int(input("Ingrese un DNI para filtrar: "))
    guardar_apellidos_dni_mayor(clientes, dni_limite)
    print(f"Se generó 'apellidos.txt' con los apellidos de clientes cuyo DNI es mayor a {dni_limite}.")

if __name__ == "__main__":
    main()
