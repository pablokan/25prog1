def input_choice(lista, msg='Elegir entre'):
    validado = False
    while not validado:
        choice = input(f'{msg} {lista}: ')
        if choice in lista:
            validado = True
    return choice

def contar_mismo_origen(archivo,lugar):
    cantidad = 0
    with open(archivo) as file:
        lineas = file.readlines()
        for linea in lineas:
            if '#' in linea:
                _,_,_,localidad = linea.split('#')
                if lugar in localidad:
                    cantidad+=1
    return cantidad

def contar_deudores(archivo, deuda, mayor_que=True):
    total = 0
    with open(archivo) as file:
        lineas = file.readlines()
        for linea in lineas:
            if '#' in linea:
                _,_,monto,_ = linea.split('#')
                monto = int(monto)
                total = (total+monto if monto>deuda else total) if mayor_que else (total+monto if monto<deuda else total)
    msg = f'más de ${deuda} es de ${total}.' if mayor_que else f'menos de ${deuda} es de ${total}.'
    resultado = f'El total de deuda acumulada de los clientes que deben {msg}'
    return resultado

def extraer_por_dni(archivo_entrada, archivo_salida, referencia):
    with open(archivo_entrada) as origen, open(archivo_salida, 'a') as destino:
        lineas = origen.readlines()
        destino.write(f'Los apellidos de los clientes cuyo D.N.I. es mayor que {referencia} son:\n')
        for linea in lineas:
            if '#' in linea:
                dni,nombre_apellido,*_ = linea.split('#')
                if int(dni) > referencia:
                    _, apellido = nombre_apellido.split()
                    destino.write(f'{apellido}\n')

def main():
    opciones = []
    with open('clientes.txt') as file:
        lineas = file.readlines()
        for linea in lineas:
            if '#' in linea:
                _,_,_,localidad = linea.split('#')
                localidad = localidad.strip()
                if localidad not in opciones:
                    opciones.append(localidad)
    localidad = 'Sampacho'
    print(f'1) La cantidad de clientes de {localidad} es {contar_mismo_origen('clientes.txt',localidad)}.')
    localidad = input_choice(opciones, 'Elija otra localidad entre')
    print(f'   La cantidad de clientes de {localidad} es {contar_mismo_origen('clientes.txt',localidad)}.')
    print(f'2) {contar_deudores('clientes.txt', 90000)}')
    print(f'   {contar_deudores('clientes.txt', 40000, mayor_que=False)}')
    extraer_por_dni('clientes.txt', 'apellidos.txt', 40000000)

if __name__ == '__main__':
    main()