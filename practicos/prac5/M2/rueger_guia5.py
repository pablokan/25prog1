def lugar(localidad, deuda, DNI, mayor = True):
    # VARIABLES
    todas_las_deudas = []
    mayores = []
    menores = []
    apellidos = []

    with open('clientes.txt', 'r') as file:
        file.readline() # descarto el primer renglon
        
        # LOCALIDAD:
        for persona in file:
            if localidad.lower() in persona.lower():
                resultado = (persona.split('#'))
        print(len(resultado) + 1)
        
        file.seek(0) # devuelvo el puntero al principio
        file.readline() # vuelvo a saltar el primer renglon

        # DEUDA:
        for persona in file:
            lista = (persona.strip().split('#')) # strip() quita los vacios o los saltos de renglon
            todas_las_deudas.append(int(lista[2]))
        
        # mayor que...
        if mayor == True:
            for x in todas_las_deudas:
                if x > deuda:
                    mayores.append(x)
            print(sum(mayores))

        # menor que...
        if mayor == False:
            for x in todas_las_deudas:
                if x < deuda:
                    menores.append(x)
            print(sum(menores))

        file.seek(0) # devuelvo el puntero al principio
        file.readline() # vuelvo a saltar el primer renglon
        
        # APELLIDO:
        for persona in file:
            lista = (persona.strip().split('#'))
            dni = (int(lista[0]))
            if dni > DNI:
                apellidos.append(dni)

    # DNI
    with open('apellidos.txt', 'w') as file:
        for apellido in apellidos:
            file.write(str(apellido) + '\n')
        
print(lugar('Sampacho', 80000, 40000000, mayor = False))