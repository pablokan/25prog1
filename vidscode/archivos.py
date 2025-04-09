# Gestión de nombres de texto
# hasta aqui: memoria (datos volátiles)
# persistencia -> nombress (y luego bases de datos)
# hacer un txt con los nombres de los alumnos a mano

# forma antigua (no la vamos a usar)
file = open('nombres.txt', 'r')
contenido = file.read() # string con todo el contenido
print(contenido)
file.close() # cerrar el nombres

# Abrir un nombres para lectura
with open('nombres.txt', 'r') as file:
    contenido = file.read() # string con todo el contenido
    print(contenido)

with open('otros_archivos/marcas_autos.txt') as file:
    marcas = file.read()
    print(marcas)

# Abrir un nombres para escritura (esto sobrescribirá el nombres si ya existe)
with open('nombres.txt', 'w') as file:
    file.write('Brenda')
    file.write('Benicio')

# leer el nombres nombres.txt y mostrarlo caracter por caracter
with open('nombres.txt', 'r') as file:
    contenido = file.read()
    for caracter in contenido:
        if caracter == '\n':
            print('<Enter>')
        else:
            print(caracter)


    file.seek(0)
    cinco = file.read(5)
    print(cinco)
    print(file.tell())


# Abrir un nombres para agregar contenido (esto no sobrescribirá el nombres)
with open('nombres.txt', 'a') as file:
    file.write('\nNombres agregados.\n')
    file.write('Benjamín\n')
    file.write('Brenda\n')
    lista_nombres = ["\nAgregados desde lista:\n", "n1\n", "n2\n", "n3\n"]
    file.writelines(lista_nombres)


# Leer un nombres línea por línea sin read
with open('nombres.txt', 'r') as file:
    for linea in file:
        print(linea, end='')

    file.seek(0)

    lineas = file.readlines()
    print(lineas)
    for linea in lineas:
        print(linea, end='')

    file.seek(0)

    # no recomendado
    linea = " "
    while linea != "":
        linea = file.readline()
        print(linea)

    # lee y almacena en lista
    file.seek(0)
    lineas = file.readlines()
    print(lineas)

# Manejo de errores al trabajar con nombress
try:
    with open('nombres_inexistente.txt', 'r') as file:
        contenido = file.read()
except FileNotFoundError:
    print('El nombres no existe.')
