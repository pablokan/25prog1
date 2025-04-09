def alta():
    print("Ejecutando alta de registro...")
    # Aquí iría el código para dar de alta

def baja():
    print("Ejecutando baja de registro...")
    # Aquí iría el código para dar de baja

def modificacion():
    print("Ejecutando modificación de registro...")
    # Aquí iría el código para modificar

def listado():
    print("Mostrando listado de registros...")
    # Aquí iría el código para listar

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Alta")
        print("2. Baja")
        print("3. Modificación")
        print("4. Listado")
        print("5. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción (1-5): "))
            
            match opcion:
                case 1:
                    alta()
                case 2:
                    baja()
                case 3:
                    modificacion()
                case 4:
                    listado()
                case 5:
                    print("¡Hasta luego!")
                    break
                case _:
                    print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

# Ejecutar el menú
if __name__ == "__main__":
    menu_principal()