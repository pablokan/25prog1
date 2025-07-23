def contar_clientes_localidad(datos, localidad_buscada):
    c = 0
    for dato in datos:
        *_, localidad = dato.split('#')
        if localidad_buscada == localidad.strip():
            c += 1
    return f'La cantidad de personas de {localidad_buscada} es {c}'

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
    with open('practicos/prac5/apellidos.txt', 'w') as arch_apellidos:
        arch_apellidos.write(f'Apellidos de los clientes con DNI mayor a {dni_buscado}\n')
        arch_apellidos.writelines(apellidos)

def main() -> None:
    with open('practicos/prac5/clientes.txt') as arch_clientes:
        clientes = arch_clientes.readlines()
    clientes.pop(0)

    print(f'1) {contar_clientes_localidad(clientes, 'Sampacho')}')
    otro_pueblo = 'La Carlota'
    print(f'1) {contar_clientes_localidad(clientes, otro_pueblo)}')
    print('2) Deudas acumuladas:', end=' ')
    print(f'{acumular_total_deuda_por_monto(clientes, 90_000)}', end=' - ')
    print(f'{acumular_total_deuda_por_monto(clientes, 40_000, False)}')
    print('3) Grabación en archivo "apellidos.txt"')
    archivar_clientes_por_documento(clientes, '40000000')

if __name__ == "__main__":
    main()

