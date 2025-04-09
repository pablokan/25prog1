print('Ingrese precios de autos (para terminar ingrese 0). Contaremos cuantos de ellos cuestan entre $27.460.000 y $33.850.000')
contador_autos = 0
precio = -1 # esta inicialización GARANTIZA el ingreso al while
while precio != 0:
    precio = input('Ingrese valor del auto: ')
    precio = int(precio)
    if 27_460_000 < precio < 33_850_000:
        contador_autos = contador_autos + 1
print(f'El total de autos en el rango de precios solicitado es {contador_autos}')

