# Bibliotecas
from libreria_guerra_naval import Cuadricula,acorazado, crucero, destructores, submarino,generar_posiciones, posicion_valida, validar_entrada,posicionamiento,turno,verificar_ganador
import os
#Programa Principal

def main():
    tamaño = 10  # Tamaño del tablero (10x10 por defecto)
    
    # Inicializar cuadrículas para Jugador 1 y Jugador 2 usando la clase Cuadricula
    cuadricula_j1 = Cuadricula(tamaño, tamaño)
    cuadricula_j2 = Cuadricula(tamaño, tamaño)
    
    # Fase de colocación de barcos
    print("=== Batalla Naval ===")
    print("Jugador 1, coloca tus barcos:")
    posicionamiento(cuadricula_j1.barcos, cuadricula_j1.tablero, tamaño)
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
    
    print("Jugador 2, coloca tus barcos:")
    posicionamiento(cuadricula_j2.barcos, cuadricula_j2.tablero, tamaño)
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
    
    # Fase de juego: Turnos alternos
    turno_actual = 1  # Empieza Jugador 1
    cuadricula_aux = Cuadricula(tamaño, tamaño)  # Para usar validar_entrada
    
    while True:
        if turno_actual == 1:
            print("Turno de Jugador 1:")
            cuadricula_oponente = cuadricula_j2
        else:
            print("Turno de Jugador 2:")
            cuadricula_oponente = cuadricula_j1
        
        # Mostrar tablero del oponente (usando imprimir_tablero, ocultando barcos)
        print("Tablero del oponente:")
        cuadricula_oponente.imprimir_tablero(ocultar_barcos=True)
        
        # Pedir coordenadas de disparo
        while True:
            entrada = input("Ingresa coordenadas de disparo (ej. (0, 5)): ")
            posicion, mensaje = validar_entrada(entrada, cuadricula_aux, verificar_no_repetido=True)
            if posicion:
                break
            print(mensaje)
        
        # Ejecutar turno
        resultado = turno(cuadricula_oponente.barcos, cuadricula_oponente.tablero, posicion, tamaño)
        if resultado is None:
            continue  # Repetir turno si coordenadas inválidas
        
        # Verificar si hay ganador
        if verificar_ganador(cuadricula_oponente.barcos):
            print(f"¡Jugador {turno_actual} gana! Todos los barcos del oponente están hundidos.")
            break
        
        # Cambiar turno
        turno_actual = 2 if turno_actual == 1 else 1
        input("Presiona Enter para continuar al siguiente turno...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
    
    print("Fin del juego. ¡Gracias por jugar!")
if __name__ == "__main__":
    main()        