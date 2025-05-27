nacidos2018 = {
    'rank1':{
        'male_name': 'Liam',
        'number_of_males': '19837',
        'female_name': 'Emma',
        'number_of_females': '18688',
    },
    'rank2':{
        'male_name': 'Noha',
        'number_of_males': '18267',
        'female_name': 'Olivia',
        'number_of_females': '17921',
    },
    'rank3':{
        'male_name': 'Michael',
        'number_of_males': '14516',
        'female_name': 'Ava',
        'number_of_females': '14924',
    },
    'rank4':{
        'male_name': 'James',
        'number_of_males': '13525',
        'female_name': 'Isabella',
        'number_of_females': '14464',
    },
    'rank5':{
        'male_name': 'Oliver',
        'number_of_males': '13389',
        'female_name': 'Sophia',
        'number_of_females': '13928',
    }
}

hombres_2018 = {}
mujeres_2018 = {}
# separar el diccionario en dos.
for rank, data in nacidos2018.items():
    hombres_2018[rank] = {'name': data['male_name'], 'number': data['number_of_males']}
    mujeres_2018[rank] = {'name': data['female_name'], 'number': data['number_of_females']}
#print(hombres, '\n','\n', mujeres)

sexo = input('Que genero desea consultar (Hombre/Mujer): ')
posicion = int(input('Ingrese el ranking que desea ver (1/5): '))
letra = input('Ingrese la inicial del nombre que desea (A-Z): ')


nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"
data_2008 = nacidos2008.split(',')
#print(data_2008)

hombres_2008 = []
mujeres_2008 = []

# reorganizar el listado.
for i in range(0, len(data_2008), 3):
    nombre = data_2008[i]
    nacimiento = data_2008[i+1]
    genero = data_2008[i+2]

    registro = {'nombre': nombre, 'nacimiento': nacimiento, 'genero': genero}

    if genero == 'm':
        hombres_2008.append(registro)
    else:
        mujeres_2008.append(registro)
#print(hombres_2008, '\n','\n', mujeres_2008)

hombres_2008.sort(key=lambda x: int(x['nacimiento']), reverse=True)
mujeres_2008.sort(key=lambda x: int(x['nacimiento']), reverse=True)

# clave para 2018
clave_2018 = f"rank{posicion}"

# Comparar los datos según el género
if sexo == "Hombre":
    if clave_2018 in hombres_2018 and posicion <= len(hombres_2008):
        nombre_2018 = hombres_2018[clave_2018]['name']
        nacimientos_2018 = int(hombres_2018[clave_2018]['number'])

        registro_2008 = hombres_2008[posicion-1]  # Tomar el nombre ordenado
        nombre_2008 = registro_2008['nombre']
        nacimientos_2008 = int(registro_2008['nacimiento'])

        diferencia = abs(nacimientos_2018 - nacimientos_2008)

        print(f"Comparando posición {posicion} para hombres:")
        print(f"{nombre_2008} (2008): {nacimientos_2008} nacimientos")
        print(f"{nombre_2018} (2018): {nacimientos_2018} nacimientos")
        print(f"Diferencia: {diferencia}")

    else:
        print("No se encontraron datos para esa posición.")
elif sexo == "Mujer":
    if clave_2018 in mujeres_2018 and posicion <= len(mujeres_2008):
        nombre_2018 = mujeres_2018[clave_2018]['name']
        nacimientos_2018 = int(mujeres_2018[clave_2018]['number'])

        registro_2008 = mujeres_2008[posicion-1]
        nombre_2008 = registro_2008['nombre']
        nacimientos_2008 = int(registro_2008['nacimiento'])

        diferencia = abs(nacimientos_2018 - nacimientos_2008)

        print(f"Comparando posición {posicion} para mujeres:")
        print(f"{nombre_2008} (2008): {nacimientos_2008} nacimientos")
        print(f"{nombre_2018} (2018): {nacimientos_2018} nacimientos")
        print(f"Diferencia: {diferencia}")

    else:
        print("No se encontraron datos para esa posición.")

else:
    print("Sexo no válido. Escriba 'Hombre' o 'Mujer'.")
    

# Filtrar nombres que comiencen con la letra ingresada
nombres_filtrados = []

# Buscar en la lista de 2008
for persona in hombres_2008 + mujeres_2008:
    if persona['nombre'][0] == letra: 
        nombres_filtrados.append(persona['nombre'])

# Buscar en el diccionario de 2018
for rank, data in nacidos2018.items():
    for nombre in [data['male_name'], data['female_name']]:
        if nombre[0] == letra:
            nombres_filtrados.append(nombre)

if nombres_filtrados:
    print("Nombres que comienzan con", letra)
    for nombre in nombres_filtrados:
        print(nombre)
else:
    print("No se encontraron nombres que comiencen con", letra)


