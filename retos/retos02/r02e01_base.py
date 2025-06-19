def calcular_puntaje(jugador, *puntos, aumento=1.0, **bonificaciones):
    return (sum(puntos) * aumento) + sum(bonificaciones.values())

print(calcular_puntaje('Thor', 50, 100, 25, aumento=1.5, combo=50, rapida=20 ))
