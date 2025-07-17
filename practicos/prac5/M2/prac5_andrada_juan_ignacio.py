
pregunta = input('ingrese la localidad: ').lower()
def busqueda_de_localidad(localidad, archivo):
     while True:
        with open(archivo, 'r') as file:
            contador = 0
            partes = file.readlines()
            for parte in partes[1:]:
                partes_de_datos = parte.strip().split('#')
                if localidad == partes_de_datos[3].lower():
                    contador += 1
        salida = print(f'la cantidad de personas que viven en {localidad} es {contador}')           
        return salida
busqueda_de_localidad(pregunta, 'clientes.txt')

pregunta2 = int(input('ingrese la deuda aproximada: '))
def busqueda_de_deuda(deuda, archivo):
     while True:
        opcion = input('Elegir los que deben mas o menos cantidad de plata (mas/menos): ').lower()
        if opcion == 'mas':
            with open(archivo, 'r') as file:
                contador_deuda = 0
                partes = file.readlines()
                for parte in partes[1:]:
                    partes_de_datos = parte.strip().split('#')
                    if int(partes_de_datos[2]) > deuda:
                        contador_deuda += int(partes_de_datos[2])
            salida = print(f'El total de deuda acumulada de los clientes que deben mas de {deuda} es ${contador_deuda}')
            break                
        elif opcion == 'menos':
                with open(archivo, 'r') as file:
                    contador_deuda = 0
                    partes = file.readlines()
                    for parte in partes[1:]:
                        partes_de_datos = parte.strip().split('#')
                        if int(partes_de_datos[2]) < deuda:
                            contador_deuda += int(partes_de_datos[2])
                salida = print(f'El total de deuda acumulada de los clientes que deben mas de {deuda} es ${contador_deuda}')
                break
        else:
            print('Opcion invalida, escribir mas o menos')
        
busqueda_de_deuda(pregunta2, 'clientes.txt')

pregunta3 = int(input('Escriba el DNI del cliente cuyo DNI sea mayor al DNI que escriba: '))

def DNI_archivo_aparte(DNI, archivo):
    almacen_nombres= []
    with open(archivo, 'r') as file:
        partes = file.readlines()
        for parte in partes[1:]:
            partes_de_datos = parte.strip().split('#')
            if int(partes_de_datos[0]) > DNI:
                nombre_apellido = partes_de_datos[1].strip().split()
                if len(nombre_apellido) > 1:
                    apellido = nombre_apellido[-1]  
                else:
                    apellido = nombre_apellido
                with open('apellido.txt', 'a') as file2:
                    file2.write(apellido + '\n')
DNI_archivo_aparte(pregunta3, 'clientes.txt')

                    
                    



