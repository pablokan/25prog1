for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz", end=" ")
    elif i % 3 == 0:
        print("fizz", end=" ")
    elif i % 5 == 0:
        print("buzz", end=" ")
    else:
        print(i, end=" ")
    if i % 20 == 0:
        print()

from random import choice

playerWins = 0
computerWins = 0

while playerWins < 3 and computerWins < 3:
    playerChoice = input("Elige piedra, papel o tijera: ").lower()
    computerChoice = choice(['piedra', 'papel', 'tijera'])
    print(f"La computadora eligió: {computerChoice}")

    if playerChoice == computerChoice:
        print("Empate!")
    elif (playerChoice == "piedra" and computerChoice == "tijera") or \
         (playerChoice == "papel" and computerChoice == "piedra") or \
         (playerChoice == "tijera" and computerChoice == "papel"):
        print("¡Ganaste esta ronda!")
        playerWins += 1
    elif (computerChoice == "piedra" and playerChoice == "tijera") or \
         (computerChoice == "papel" and playerChoice == "piedra") or \
         (computerChoice == "tijera" and playerChoice == "papel"):
        print("La computadora ganó esta ronda.")
        computerWins += 1
    else:
        print("Elección inválida. Por favor, elige piedra, papel o tijera.")

    print(f"Puntaje: Jugador {playerWins} - Computadora {computerWins}\n")

if playerWins == 3:
    print("¡Felicitaciones! ¡Has ganado el juego!")
else:
    print("La computadora ha ganado el juego.")

 if alto <= 0 or ancho <= 0:
        print("Las dimensiones del rectángulo deben ser mayores que cero.")
        return

    for _ in range(alto):
        print(caracter * ancho)

if __name__ == "__main__":
    try:
        entrada = input("Ingrese la altura, el ancho y el carácter (separados por espacios): ").split()
        if len(entrada) != 3:
            print("Por favor, ingrese tres valores separados por espacios (ej: 4 7 #).")
        else:
            alto = int(entrada[0])
            ancho = int(entrada[1])
            caracter = entrada[2]

            dibujar_rectangulo(alto, ancho, caracter)

    except ValueError:
        print("Entrada inválida. Por favor, ingrese números enteros para la altura y el ancho.")

def obtener_color_casilla():
    """
    Solicita al usuario el número de fila y columna de un tablero de ajedrez
    y devuelve el color de la casilla (blanca o negra).
    Si la entrada no es válida, muestra "Afuera".
    """
    try:
        fila = int(input("Ingrese el número de fila (1-8): "))
        columna = int(input("Ingrese el número de columna (1-8): "))

        if 1 <= fila <= 8 and 1 <= columna <= 8:
            # En un tablero de ajedrez, la suma de fila y columna par indica un color,
            # y la suma impar indica el otro. Podemos usar esto para determinar el color.
            if (fila + columna) % 2 == 0:
                print("La casilla es blanca.")
            else:
                print("La casilla es negra.")
        else:
            print("Afuera.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números enteros.")

if __name__ == "__main__":
    obtener_color_casilla()

def es_bisiesto(año):
    """
    Verifica si un año dado es bisiesto según las reglas del calendario gregoriano.

    Args:
        año (int): El año a verificar.

    Returns:
        bool: True si el año es bisiesto, False de lo contrario.
    """
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        año_ingresado = int(input("Ingrese un año: "))
        if es_bisiesto(año_ingresado):
            print(f"El año {año_ingresado} es bisiesto.")
        else:
            print(f"El año {año_ingresado} no es bisiesto.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero para el año.")

def dibujar_rectangulo(alto, ancho, caracter):
    """
    Dibuja un rectángulo de las dimensiones especificadas utilizando el carácter dado.

    Args:
        alto (int): La altura del rectángulo.
        ancho (int): El ancho del rectángulo.
        caracter (str): El carácter con el que se dibujará el rectángulo.
    """
    if alto <= 0 or ancho <= 0:
        print("Las dimensiones del rectángulo deben ser mayores que cero.")
        return

    for _ in range(alto):
        print(caracter * ancho)

if __name__ == "__main__":
    try:
        alto = int(input("Ingrese la altura del rectángulo: "))
        ancho = int(input("Ingrese el ancho del rectángulo: "))
        caracter = input("Ingrese el carácter para dibujar el rectángulo: ")

        dibujar_rectangulo(alto, ancho, caracter)

    except ValueError:
        print("Entrada inválida. Por favor, ingrese números enteros para la altura y el ancho.")

