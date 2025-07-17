def cantidad_de_clientes(archivo_entrada,localidad_buscada = '',opciones = ['Villa María', 'Río Cuarto', 'Sampacho']):
    with open(archivo_entrada,'r',encoding='utf-8') as file:
        archivo = file.readlines()
        if localidad_buscada == '':
            validacion = False
            while not validacion: 
                print(f'Ingrese otra localidad distitnta a La Carlota, las opciones son: {opciones}')
                eleccion = input(f'Localidad: ')
                if eleccion in opciones:
                    validacion = True
                    localidad_a_contar = eleccion
                else:
                    print('Opcion Invalida')
        else:
            localidad_a_contar = localidad_buscada
        cant = 0
        for linea in archivo[1:]:
            datos = linea.strip().split('#')
            #print(datos)
            #print(datos[-1])
            localidad = datos[-1]
            if localidad == localidad_a_contar:
                cant += 1
    return cant

def total_deuda_clientes(archivo_entrada,monto_deuda = '',opciones=['deben mas','deben menos']):
    with open(archivo_entrada,'r',encoding='utf-8') as file:
        archivo = file.readlines()
        '''    
        for linea in archivo[1:]: 
            datos = linea.strip().split('#')
            deuda = datos[2]
            #print(deuda)
'''
        total_deuda = 0
        salida = ''
        validacion = False
        while not validacion: # validacion de opciones (mayorq o mennorq)
            print(f'Opciones para comparar deuda: {opciones}')
            eleccion = input('Eleccion: ')
            if eleccion in opciones:
                validacion = True
                if eleccion == 'deben mas':
                    validacion2 = False
                    while not validacion2: # validacion de monto
                        monto_deuda = input('Monto de deuda: ')
                        try:
                            monto_deuda = int(monto_deuda)
                            validacion2 = True
                        except:
                            print('Ingrese un numero entero')
                    for linea in archivo[1:]:
                        datos = linea.strip().split('#')
                        deuda = datos[2]
                        deuda = int(deuda)
                        if deuda > monto_deuda:
                            total_deuda += deuda
                    salida = f'El total de deuda acumulada mayor a {monto_deuda} es de: ${total_deuda} pesos'
                elif eleccion == 'deben menos':
                    validacion2 = False
                    while not validacion2: # validacion de monto
                        monto_deuda = input('Monto de deuda: ')
                        try:
                            monto_deuda = int(monto_deuda)
                            validacion2 = True
                        except:
                            print('Ingrese un numero entero')
                    for linea in archivo[1:]:
                        datos = linea.strip().split('#')
                        deuda = datos[2]
                        deuda = int(deuda)
                        if deuda < monto_deuda:
                            total_deuda += deuda
                    salida = f'El total de deuda acumulada menor a {monto_deuda} es de: ${total_deuda} pesos'
            else:
                print('Opcion Invalida')
    return salida

def escritura_apellido(archivo_entrada,archivo_salida,nro_documento = ''):
    validacion = False
    while not validacion: # validacion de nro_documento
        nro_documento = input('Apellido de los clientes cuyo DNI sea mayor a: ')
        try:
            nro_documento = int(nro_documento)
            validacion = True
        except:
            print('Ingrese numero valido')
    with open(archivo_entrada,'r',encoding='utf-8') as file:
        archivo = file.readlines()

    with open(archivo_salida,'w',encoding='utf-8') as file:
        file.write(f'Apellidos de los clientes con documento mayor a {nro_documento}\n')
        for i in range(1,len(archivo)):
            datos = archivo[i].strip().split('#')
            documento = datos[0]
            documento = int(documento)
            nombre_completo = datos[1].split(' ')
            apellido = nombre_completo[1]
            if documento > nro_documento:
                file.write(f'{apellido}\n')

if __name__ == '__main__':
    cantidad_de_localidad_literal = cantidad_de_clientes('clientes.txt', 'La Carlota')     
    print(f'La cantidad de clientes de La Carlota son: {cantidad_de_localidad_literal} clientes')
    cant_localidad_variable = cantidad_de_clientes('clientes.txt')
    print(f'La cantidad de clientes de la localidad ingresada es: {cant_localidad_variable} clientes')

    monto_total_de_deuda = total_deuda_clientes('clientes.txt')
    print(monto_total_de_deuda)

    escritura_apellido('clientes.txt','apellidos.txt')
