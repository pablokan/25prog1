
nacidos2018 = {"rank": [1,2,3,4,5],
               "nombres masculinos": ["Liam", "Noah", "Michael","James","Oliver"],
               "cantidad por nombres masculinos": [19837,18267,14516,13525,13389],
               "nombres femeninos": ["Emma", "Olivia", "Ava", "Isabella", "Sophia"],
               "cantidad por nombres femeninos": [18688,17921,14924,14464,13928]}

nacidos2008 = ["Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"]

nacidos2008_organizado = {"nombre masculinos": [],
                          "cantidad por nombres masculinos": [],
                          "nombres femeninos": [],
                          "cantidad por nombres femenino": []}

#ornizar nombres de masculinos y femeninos de mayor cantidad a menor
datos_separados_2008 = nacidos2008[0].split(",")

cantidades_2008 = []
masculinos_totales_2008 = []
femeninos_totales_2008 = []

for i in range(0, len(datos_separados_2008), 3):
    cantidad = int(datos_separados_2008[i + 1])
    nombre = datos_separados_2008[i]
    sexo = datos_separados_2008[i + 2]

    if sexo == "m":
        masculinos_totales_2008.append([nombre, cantidad])
    else:
        femeninos_totales_2008.append([nombre, cantidad])

for i in range(len(masculinos_totales_2008)):
    for pos in range(len(masculinos_totales_2008) - 1 -i):
        if masculinos_totales_2008[pos][1] < masculinos_totales_2008[pos + 1][1]:
            masculinos_totales_2008[pos], masculinos_totales_2008[pos + 1] = masculinos_totales_2008[pos + 1], masculinos_totales_2008[pos]

for nombre, cantidad in masculinos_totales_2008:
    nacidos2008_organizado["nombre masculinos"].append(nombre)
    nacidos2008_organizado["cantidad por nombres masculinos"].append(cantidad)

for i in range(len(femeninos_totales_2008)):
    for pos in range(len(femeninos_totales_2008) -1 -i):
        if femeninos_totales_2008[pos][1] < femeninos_totales_2008[pos + 1][1]:
            femeninos_totales_2008[pos], femeninos_totales_2008[pos + 1] = femeninos_totales_2008[pos + 1], femeninos_totales_2008[pos]

for nombre, cantidad in femeninos_totales_2008:
    nacidos2008_organizado["nombres femeninos"].append(nombre)
    nacidos2008_organizado["cantidad por nombres femenino"].append(cantidad)

contador_vueltas = 0

while True:
    #saber si el usuario desea continuar
    contador_vueltas += 1

    if contador_vueltas > 1:
        print('= =' * 30)
        continuar = input('Desea continuar? (si/no) => ').lower()
        if continuar == 'no':
            print('=' * 30)
            print('Muchas gracias')
            break

    #mostrar diferencias entre posiciones de distintos años
    print("=" * 30)
    ranking_deseado_usuario = int(input("Ingrese el ranking que desea (del 1 al 5) => "))
    sexo_deseado_usuario = input('Ingrese el sexo deseado (f/m) => ').lower()

    if ranking_deseado_usuario > 5:
        print('El ranking deseado que inserto, no es valido')

    if sexo_deseado_usuario == 'm':
        if nacidos2018["cantidad por nombres masculinos"][ranking_deseado_usuario -1] > nacidos2008_organizado["cantidad por nombres masculinos"][ranking_deseado_usuario -1]:
            diferencia = nacidos2018["cantidad por nombres masculinos"][ranking_deseado_usuario -1] - nacidos2008_organizado["cantidad por nombres masculinos"][ranking_deseado_usuario-1]
            print(f'En el ranking {ranking_deseado_usuario} de masculinos, la diferencia es de: {diferencia} de {nacidos2018["nombres masculinos"][ranking_deseado_usuario-1]} (2008) sobre {nacidos2008_organizado["nombre masculinos"][ranking_deseado_usuario-1]} (2018)')
        elif nacidos2018["cantidad por nombres masculinos"][ranking_deseado_usuario-1] < nacidos2008_organizado["cantidad por nombres masculinos"][ranking_deseado_usuario-1]:
            diferencia = nacidos2008_organizado["cantidad por nombres masculinos"][ranking_deseado_usuario-1] - nacidos2018["cantidad por nombres masculinos"][ranking_deseado_usuario-1]
            print(f'En el ranking {ranking_deseado_usuario} de masculinos, la diferencia es de: {diferencia} de {nacidos2008_organizado["nombre masculinos"][ranking_deseado_usuario-1]} (2008) sobre {nacidos2018["nombres masculinos"][ranking_deseado_usuario-1]} (2018)')
    else:
        if nacidos2018["cantidad por nombres femeninos"][ranking_deseado_usuario - 1] > nacidos2008_organizado["cantidad por nombres femenino"][ranking_deseado_usuario - 1]:
            diferencia = nacidos2018["cantidad por nombres femeninos"][ranking_deseado_usuario - 1] - nacidos2008_organizado["cantidad por nombres femenino"][ranking_deseado_usuario -1]
            print(f'En el ranking {ranking_deseado_usuario} de femeninos, la diferencia es de: {diferencia} de {nacidos2018["cantidad por nombres femeninos"][ranking_deseado_usuario-1]} (2008) sobre {nacidos2008_organizado["nombres femeninos"][ranking_deseado_usuario-1]} (2018)')
        elif nacidos2018["cantidad por nombres femeninos"][ranking_deseado_usuario -1 ] < nacidos2008_organizado["cantidad por nombres femenino"][ranking_deseado_usuario -1 ]:
            diferencia = nacidos2008_organizado["cantidad por nombres femenino"][ranking_deseado_usuario-1] - nacidos2018["cantidad por nombres femeninos"][ranking_deseado_usuario-1]
            print(f'En el ranking {ranking_deseado_usuario} de femeninos, la diferencia es de: {diferencia} de {nacidos2008_organizado["nombres femeninos"][ranking_deseado_usuario-1]} (2008) sobre {nacidos2018["nombres femeninos"][ranking_deseado_usuario-1]} (2018)')
            
    #solicitar letra al usuario y poner nombres que comiencen con esa letra
    print('=' * 30)

    inicial_usuario = input('Ingrese la inicial para filtrar nombres => ').upper()
    nombres_con_iniciales = []
    todos_los_nombres = []

    for nombre_masculino_2018 in nacidos2018["nombres masculinos"]:
        nombre_dividido = nombre_masculino_2018.split()
        todos_los_nombres.append(nombre_dividido)
        inicial_nombre = ''
        for inicial in nombre_dividido:
            inicial_nombre += inicial[0]
            if inicial_usuario == inicial_nombre:
                nombres_con_iniciales.append(nombre_masculino_2018)
    
    for nombre_femenino_2018 in nacidos2018["nombres femeninos"]:
        nombre_dividido = nombre_femenino_2018.split()
        todos_los_nombres.append(nombre_dividido)
        inicial_nombre = ''
        for inicial in nombre_dividido:
            inicial_nombre += inicial[0]
            if inicial_usuario == inicial_nombre:
                nombres_con_iniciales.append(nombre_femenino_2018)
    
    for nombre_masculino_2008 in nacidos2008_organizado["nombre masculinos"]:
        nombre_dividido = nombre_masculino_2008.split()
        todos_los_nombres.append(nombre_dividido)
        inicial_nombre = ''
        for inicial in nombre_dividido:
            inicial_nombre += inicial[0]
            if inicial_usuario == inicial_nombre:
                nombres_con_iniciales.append(nombre_masculino_2008)

    for nombre_femenino_2008 in nacidos2008_organizado["nombres femeninos"]:
        nombre_dividido = nombre_femenino_2008.split()
        todos_los_nombres.append(nombre_dividido)
        inicial_nombre = ''        
        for inicial in nombre_dividido:
            inicial_nombre += inicial[0]
            if inicial_usuario == inicial_nombre:
                nombres_con_iniciales.append(nombre_femenino_2008)
    

    if len(nombres_con_iniciales) == 0:
        print(f'No hay nombres con la inicial {inicial_usuario}')
    else:
        print(f'Los nombres que comienzan con {inicial_usuario} son:')
        for nombre in nombres_con_iniciales:
            print(nombre)

    #nombres que se repiten en los periodos
    print('=' * 30)
    nombres = []

    for sublista in todos_los_nombres: #hago la lista de listas, en una sola lista de strings
        nombre = sublista[0]
        nombres.append(nombre)

    repetidos = []

    for nombre in nombres:
        contador = 0
        for n in nombres:
            if n == nombre:
                contador += 1
        if contador > 1 and nombre not in repetidos:
            repetidos.append(nombre)

    print(f'Los nombres que se repiten son: {repetidos}')
    
