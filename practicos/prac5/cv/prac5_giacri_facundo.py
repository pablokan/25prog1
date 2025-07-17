def contar_localidad(base_de_datos, pos_local, filtro='La Carlota'):
    locs = []
    for c in base_de_datos:
        if len(c) == 4:
            loc = c[pos_local]
            locs.append(loc)
    contador = locs.count(filtro)
    return f'La cantidad de clientes de {filtro} es {contador}.'

def deuda_total(base_de_datos, pos_deuda, menor , mayor):
    sumar_menor = 0
    sumar_mayor = 0
    for c in base_de_datos:
        if len(c) == 4:
            if int(c[pos_deuda]) < menor:
                sumar_menor += int(c[pos_deuda])
            elif int(c[pos_deuda]) > mayor:
                sumar_mayor += int(c[pos_deuda])
    return f'El total de deuda acumulada de los clientes que deben más de {mayor} pesos es ${sumar_mayor}', f'El total de deuda acumulada de los clientes que deben menos de {menor} es ${sumar_menor}'
        
def filtrar_dni(base_de_datos, buscar, retornar):
    filtro = int(input('Filtrar DNI mayores a: '))
    lista_ap = []
    for c in base_de_datos:
        if len(c) == 4:
            if int(c[buscar]) > filtro:
                ap = c[retornar].split(' ')[1]
                lista_ap.append(ap)
    return lista_ap
              

with open('clientes.txt', 'r', encoding='utf-8') as archivo_etrada:
    datos_originales = archivo_etrada.read()
    lista_datos = datos_originales.split('\n')
    clientes = []    
    for d in lista_datos[1:]:
        cliente = d.split('#')
        clientes.append(cliente)
    encabezado = lista_datos[0].split(',')
    dni = encabezado.index('DNI')
    nombre_apellido = encabezado.index('nombre y apellido')
    deuda = encabezado.index('monto de deuda en pesos') 
    localidad = encabezado.index('localidad')

clientes_por_localidad = contar_localidad(clientes, localidad)
print(clientes_por_localidad)
pedir_localidad = input('Ingrese otra localidad: ').title()
contar_otra_localidad = contar_localidad(clientes,localidad,pedir_localidad)
print(contar_otra_localidad)

deuda_menor_que = int(input('Suma deudas menor a: '))
deuda_mayor_que = int(input('Suma deudas mayor a: '))
deuda_acumulada = deuda_total(clientes, deuda, deuda_menor_que, deuda_mayor_que)
print(deuda_acumulada[0])
print(deuda_acumulada[1])

ap_filtrados = filtrar_dni(clientes, dni, nombre_apellido)
with open('apellidos.txt', 'x', encoding='utf-8') as archivo_salida:
    escribir = archivo_salida
    for ap in ap_filtrados:
        escribir.write(f'{ap}\n')