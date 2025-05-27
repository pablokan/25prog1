def crear_menu(funciones, titulo="MENÚ DE OPCIONES"):
    """
    Crea un menú interactivo dinámico basado en las funciones proporcionadas.
    
    Args:
        funciones (dict): Diccionario donde las claves son los nombres de las opciones
                         y los valores son las funciones a ejecutar
        titulo (str): Título del menú
    
    Returns:
        None
    """
    while True:
        print("\n" + "="*50)
        print(f"{titulo:^50}")
        print("="*50)
        
        # Mostrar opciones del menú
        opciones = list(funciones.keys())
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        print(f"{len(opciones) + 1}. Salir")
        
        print("-"*50)
        
        try:
            eleccion = int(input("Seleccione una opción: "))
            
            if eleccion == len(opciones) + 1:
                print("¡Hasta luego!")
                break
            elif 1 <= eleccion <= len(opciones):
                opcion_elegida = opciones[eleccion - 1]
                print(f"\nEjecutando: {opcion_elegida}")
                print("-"*30)
                
                # Ejecutar la función correspondiente
                funciones[opcion_elegida]()
                
                input("\nPresione Enter para continuar...")
            else:
                print("❌ Opción no válida. Intente nuevamente.")
                
        except ValueError:
            print("❌ Por favor ingrese un número válido.")
        except Exception as e:
            print(f"❌ Error al ejecutar la función: {e}")


# Funciones de ejemplo para demostrar el uso
def saludar():
    nombre = input("Ingrese su nombre: ")
    print(f"¡Hola {nombre}! ¡Bienvenido!")

def calcular():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Suma: {a + b}")
        print(f"Resta: {a - b}")
        print(f"Multiplicación: {a * b}")
        if b != 0:
            print(f"División: {a / b}")
        else:
            print("No se puede dividir por cero")
    except ValueError:
        print("❌ Por favor ingrese números válidos")

def mostrar_fecha():
    from datetime import datetime
    fecha_actual = datetime.now()
    print(f"Fecha y hora actual: {fecha_actual.strftime('%d/%m/%Y %H:%M:%S')}")

def contar_palabras():
    texto = input("Ingrese un texto: ")
    palabras = len(texto.split())
    caracteres = len(texto)
    print(f"Palabras: {palabras}")
    print(f"Caracteres: {caracteres}")

def tabla_multiplicar():
    try:
        numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
        print(f"\nTabla de multiplicar del {numero}:")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    except ValueError:
        print("❌ Por favor ingrese un número válido")


# Ejemplo de uso
if __name__ == "__main__":
    # Diccionario con las opciones del menú y sus funciones correspondientes
    menu_opciones = {
        "Saludar Usuario": saludar,
        "Calculadora Básica": calcular,
        "Mostrar Fecha y Hora": mostrar_fecha,
        "Contador de Palabras": contar_palabras,
        "Tabla de Multiplicar": tabla_multiplicar
    }
    
    # Crear y ejecutar el menú
    crear_menu(menu_opciones, "MI APLICACIÓN")


# Ejemplo alternativo más simple
def menu_simple(funciones):
    """
    Versión simplificada del menú que solo ejecuta una vez
    
    Args:
        funciones (list): Lista de tuplas (nombre, función)
    """
    print("\n--- MENÚ ---")
    for i, (nombre, _) in enumerate(funciones, 1):
        print(f"{i}. {nombre}")
    
    try:
        opcion = int(input("Seleccione una opción: ")) - 1
        if 0 <= opcion < len(funciones):
            nombre, funcion = funciones[opcion]
            print(f"\nEjecutando: {nombre}")
            funcion()
        else:
            print("Opción no válida")
    except ValueError:
        print("Ingrese un número válido")


# Ejemplo de uso del menú simple
def ejemplo_menu_simple():
    opciones = [
        ("Opción 1", lambda: print("Ejecutando opción 1")),
        ("Opción 2", lambda: print("Ejecutando opción 2")),
        ("Opción 3", lambda: print("Ejecutando opción 3"))
    ]
    menu_simple(opciones)