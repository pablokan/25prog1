def calcular_puntaje(jugador, *puntos, aumento=1.0, **bonificaciones):
    total = (sum(puntos) * aumento) + sum(bonificaciones.values())
    cadena_bonificaciones = ', '.join(bonificaciones.keys()) if bonificaciones else 'ninguna'
    print(f'Puntuación final de {jugador} = {total:g} puntos. (Bonificaciones: {cadena_bonificaciones})')

calcular_puntaje('Thor', 50, 100, 25, aumento=1.5, combo=50, rapida=20)
calcular_puntaje('Black Widow', 300, 10, aumento=3.3)
calcular_puntaje('Flash', rapida=200, destruccion=100, diversion=40)
calcular_puntaje('Hulk', 250, aumento=2.0, destruccion=2500)
