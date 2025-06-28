def contar_clientes_localidad(datos, localidad_buscada):
    c = 0
    for dato in datos:
        *_, localidad = dato.split('#')
        if localidad_buscada == localidad[:-1]:
            c += 1
    return c

def acumular_total_deuda_por_monto(datos, monto_buscado, mayor=True):
    ac_mayor = ac_menor = 0
    for dato in datos:
        monto = int(dato.split('#')[-2])
        if mayor and monto > monto_buscado:
            ac_mayor += monto
        elif not mayor and monto < monto_buscado:
            ac_menor += monto
    return ac_mayor if mayor else ac_menor

def archivar_clientes_por_documento(datos, dni_buscado):
    apellidos = []
    for dato in datos:
        dni, nombre_completo, *_ = dato.split('#')
        if dni > dni_buscado:
            apellidos.append(f'{nombre_completo.split()[1]}\n')
    with open('apellidos.txt', 'w') as ap_arch:
        ap_arch.write(f'Apellidos de los clientes con DNI mayor a {dni_buscado}\n')
        ap_arch.writelines(apellidos)

def main() -> None:
    with open('clientes.txt') as a:
        clientes = a.readlines()
    _ = clientes.pop(0)

    print(f'1) {contar_clientes_localidad(clientes, 'Sampacho')}')
    print('2) Deudas acumuladas:', end=' ')
    print(f'{acumular_total_deuda_por_monto(clientes, 90_000)}', end=' - ')
    print(f'{acumular_total_deuda_por_monto(clientes, 40_000, False)}')
    print('3) Grabación en archivo "apellidos.txt"')
    archivar_clientes_por_documento(clientes, '44000000')

if __name__ == "__main__":
    main()

