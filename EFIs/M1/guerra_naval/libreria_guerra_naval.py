# Bibliotecas

# Clases

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #    

    # Clase Madre Barco
class barco():

    def __init__(self, posicion, tamanio):

        self.posicion = posicion  # Se guarda una lista de tuplas
        self.tamanio = tamanio
        self.estado = ['B'] * tamanio  # Lista de estados: '~' (agua), '1' (impactado), 'X' (hundido), 'B' (barco)
        self.hundido = False  # Booleano para verificar si fue hundido

   # Metodos
    def verificar_hundido(self):

        if all(estado == '1' for estado in self.estado): # Verifica si todas las partes son 1 (Impactos)
            self.estado = ['X'] * self.tamanio
            self.hundido = True
      
    def  impacto(self,tupla):
        if tupla in self.posicion:
            i = self.posicion.index(tupla)
            if self.estado[i] == 'B':
                self.estado[i] = '1'
                self.verificar_hundido()
                return True
        return False
    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #        
    
    # Clase Hijas      

class acorazado(barco):
    def __init__(self, posicion):
        super().__init__(posicion, tamanio = 4)

class crucero(barco):
    def __init__(self, posicion):
        super().__init__(posicion,tamanio = 3)

class destructores(barco):
     def __init__(self, posicion):
        super().__init__(posicion, tamanio = 2)

class submarino(barco):
     def __init__(self, posicion):
        super().__init__(posicion, tamanio = 1)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #    

class Cuadricula:
    def __init__(self, filas=10, columnas=10):
        self.filas = filas
        self.columnas = columnas
        self.tablero = [['~' for _ in range(self.columnas)] for _ in range(self.filas)]  # Lista 2D para compatibilidad
        self.barcos = []  # Lista de barcos
        # No necesitamos _inicializar_tablero() ya que se hace en __init__

    def imprimir_tablero(self, ocultar_barcos=True):
        # Generar los números para las columnas (0, 1, 2, ..., hasta el número de columnas - 1)
        numeros_columnas = [str(j) for j in range(self.columnas)]
        
        # Imprimir la fila de encabezado con los números de las columnas
        print("  " + " ".join(numeros_columnas))
        
        # Imprimir cada fila con su número (empezando en 0) y los valores del tablero
        for i in range(self.filas):
            fila = f"{i} "  # Número de fila (empezando en 0)
            valores = []
            for j in range(self.columnas):
                valor = self.tablero[i][j]
                if ocultar_barcos and valor == 'B':
                    valores.append('~')  # Ocultar barcos para no revelar posiciones
                else:
                    valores.append(valor)
            fila += " ".join(valores)
            print(fila)

# Funciones

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
def validar_entrada(entrada, cuadricula, verificar_no_repetido=False):
    try:
        if isinstance(entrada, str):
            entrada = eval(entrada)
        if not isinstance(entrada, tuple) or len(entrada) != 2:
            return None, "Entrada invalida: Debe ser una tupla de dos elementos, ej. (0, 5)."
        x, y = entrada
        if not (isinstance(x, int) and isinstance(y, int)): # Verifica si x e y son enteros
            return None, "Entrada invalida: Usa numeros enteros."
        if not (0 <= x < cuadricula.filas and 0 <= y < cuadricula.columnas):
            return None, f"Posicion fuera de limites: Debe estar entre (0,0) y ({cuadricula.filas-1},{cuadricula.columnas-1})."
        if verificar_no_repetido and cuadricula.tablero[x][y] in ['O', 'X']:
            return None, "Ya atacaste este lugar."
        return (x, y), "Entrada valida." #Retorna la tupla si es verdadero
    except:
        return None, "Error al procesar la entrada. Usa formato (x, y)."   
    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
def turno(barcos_oponente, tablero_oponente, posicion, tamaño=10):
    fila, columna = posicion
    if not (0 <= fila < tamaño and 0 <= columna < tamaño):
        print("Coordenadas fuera del tablero.")
        return None
    if tablero_oponente[fila][columna] in ['O', 'X']:
        print("Ya disparaste ahí.")
        return None
    
    impacto = False
    for barco in barcos_oponente:
        if barco.impacto((fila, columna)):
            impacto = True
            break
    
    if impacto:
        tablero_oponente[fila][columna] = 'X'
        print("¡Impacto!")
        return True
    else:
        tablero_oponente[fila][columna] = 'O'
        print("Agua.")
        return False
    

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
def verificar_ganador(barcos):
    """Verifica si todos los barcos de una lista están hundidos."""
    return all(barco.hundido for barco in barcos)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
def posicionamiento(barcos_jugador, tablero_jugador, tamaño=10):
    tipos_barcos = [
        ("Acorazado", 4, acorazado),
        ("Crucero", 3, crucero),
        ("Destructor", 2, destructores),
        ("Submarino", 1, submarino)
    ]
    
    print("Colocación de barcos para el jugador:")
    for nombre, tamanio, clase_barco in tipos_barcos:
        while True:
            try:
                print(f"Colocando {nombre} (tamaño {tamanio}).")
                fila = int(input(f"Fila inicial (0-{tamaño-1}): "))
                col = int(input(f"Columna inicial (0-{tamaño-1}): "))
                orientacion = input("Orientación (H para horizontal, V para vertical): ").upper()
                
                posiciones = generar_posiciones(fila, col, tamanio, orientacion)
                valida, mensaje = posicion_valida(tablero_jugador, posiciones, tamaño)
                if valida:
                    nuevo_barco = clase_barco(posiciones)
                    barcos_jugador.append(nuevo_barco)
                    for f, c in posiciones:
                        tablero_jugador[f][c] = 'B'
                    print(f"{nombre} colocado exitosamente.")
                    break
                else:
                    print(f"Posición inválida: {mensaje} Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Usa números para fila/columna.")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

def generar_posiciones(fila, col, tamanio, orientacion):
    posiciones = []
    if orientacion == 'H':  # Horizontal
        for i in range(tamanio):
            posiciones.append((fila, col + i))
    elif orientacion == 'V':  # Vertical
        for i in range(tamanio):
            posiciones.append((fila + i, col))
    return posiciones
               
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
def posicion_valida(tablero, posiciones, tamaño):
    for fila, col in posiciones:
        if not (0 <= fila < tamaño and 0 <= col < tamaño):
            return False, "Posición fuera del tablero."
        if tablero[fila][col] != '~':
            return False, "Posición ocupada por otro barco (superposición)."
    return True, ""

#Programa Principal
def main():
    print('Libreria')
    # Entrada inválida: no es tupla
if __name__ == "__main__":
    main()        