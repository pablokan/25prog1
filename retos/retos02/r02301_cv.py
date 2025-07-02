def calcular_puntaje(jugador, *puntos, aumento=1.0, **bonificaciones):
    total = 0
    for punto in puntos:
        total += punto
    total *= aumento
    tv = 0
    for v in bonificaciones.values():
        tv += v
    return print(f'Puntuación final de {jugador} = {total + tv} puntos.')


calcular_puntaje('Thor', 50, 100, 25, aumento=1.5, combo=50, rapida=20)
calcular_puntaje('Black Widow', 300, 10, aumento=3.3)
calcular_puntaje('Flash', rapida=200, destruccion=100, diversion=40)
calcular_puntaje('Hulk', 250, aumento=2.0, destruccion=2500)