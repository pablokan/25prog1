from func_lib import calcular_edad, input_choice

personas = [
    "Vikki Tewkesbury,France,30-01-2000",
    "Virgie Brach,France,04-06-1994",
    "Adeline LaPadula,France,18-06-2002",
    "Willy Branscombe,Argentina,21-11-1997",
    "Diane Piffe,France,07-08-1993",
    "Britta Causbey,France,24-04-1991",
    "Elisabeth Cleeve,France,04-03-1991",
    "Rafael Ivanchenkov,France,28-04-2002",
    "Zerk Milsom,Norway,03-12-1994",
    "Adorne Ovington,United States,17-08-1991",
    "Kathryn Backshell,United States,04-10-1992",
    "Blake Colbeck,United States,18-01-1999",
    "Arron Bresnahan,United States,30-06-2001",
    "Deloria Dominguez,France,31-07-1990",
    "Grenville Aldersea,Argentina,11-01-2001",
    "Jemimah Haughian,Argentina,30-11-1998",
    "Con Gethen,United States,06-06-1992",
    "Roxie Igoe,France,31-03-2002",
    "Hollyanne Mottley,United States,05-01-1996",
    "Ambrosio Cadore,Norway,09-12-2002"
]

# "Vikki Tewkesbury,France,30-01-2000"
def obtener_poblacion_pais(datos, pais_buscado):
    c = 0
    for dato in datos:
        _, pais, _ = dato.split(',')
        if pais == pais_buscado:
            c += 1
    return f'La cantidad de personas de {pais_buscado} es {c}'

# "Vikki Tewkesbury,France,30-01-2000"
# "Adorne Ovington,United States,17-08-1991"
def obtener_nombres_edades(datos, inicial):
    inicial = inicial.upper()
    for dato in datos:
        nombre, apellido, *_ = dato.split()
        if apellido[0] == inicial:
            print(f'{nombre} tiene {calcular_edad(dato[-10:])} años')
        

def main():
    print('1)')
    print(obtener_poblacion_pais(personas, "Argentina"))

    print('2)')
    p = input_choice('Germany/United States/Norway/France', 'País a buscar')
    print(obtener_poblacion_pais(personas, p))

    print('3)')
    inicial_apellido = input('Ingrese inicial de apellido a buscar: ')
    obtener_nombres_edades(personas, inicial_apellido)


if __name__ == "__main__":
    main()