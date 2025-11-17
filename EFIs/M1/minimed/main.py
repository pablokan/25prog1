
from core.auth_manager import login_admin, login_paciente, registrar_paciente
from cliente.admin_menu import start_admin_menu 
from cliente.paciente_menu import start_paciente_menu 

def mostrar_menu_inicial():
    """Muestra el menú de inicio y solicita una opción."""
    print("\n==================================")
    print("      SISTEMA MINI-MED (v1.0)     ")
    print("==================================")
    print("Ingreso al sistema como:")
    print("1 - Administrador")
    print("2 - Paciente")
    print("3 - Registrarse como Paciente")
    print("4 - Salir del Sistema")
    opcion = input("Ingrese su selección (1, 2, 3 o 4): ")
    return opcion

def run_app():
    """Bucle principal de la aplicación."""
    while True:
        opcion = mostrar_menu_inicial()
        if opcion == '1':
            print("\n--- INICIO SESIÓN ADMIN ---")
            auth_data = login_admin()
            if auth_data and auth_data['rol'] == 'admin':
                start_admin_menu(auth_data)
        
        elif opcion == '2':
            print("\n--- INICIO SESIÓN PACIENTE ---")
            auth_data = login_paciente()
            if auth_data and auth_data['rol'] == 'paciente':
                start_paciente_menu(auth_data)

        elif opcion == '3':
            print("\n--- REGISTRO PACIENTE ---")
            registrar_paciente()

        elif opcion == '4':
            print("\nGracias por usar MiniMed. Nos vemos !")
            break
            
        else:
            print("\nERROR: Opción no reconocida. Por favor, ingrese 1, 2, 3 o 4.")

if __name__ == "__main__":
    run_app()