paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Francia': 'París',
    'UK': 'London'
}

pais_a_buscar = 'Frana'

if pais_a_buscar in paises_capitales.keys():
    print(paises_capitales[pais_a_buscar])
else:
    print('no ta')
