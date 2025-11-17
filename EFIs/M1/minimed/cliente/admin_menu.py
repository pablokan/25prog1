from core.admin_manager import AdminManager

def mostrar_menu_admin():
    print("\n--- MENÚ ADMINISTRADOR ---")
    print("1. Listar Médico")
    print("2. Ver Turnos del dia")
    print("3. Cerrar Sesión")
    return input("Seleccione una opción: ")


def start_admin_menu(admin_data):
    manager = AdminManager(admin_data.get('user')) 
    
    print(f"\n¡Bienvenido/a, {admin_data.get('user')}!")
    
    while True:
        opcion = mostrar_menu_admin()

        if opcion == '1':
            manager.listar_medico()
            
        elif opcion == '2':
       
            print("\n--- LISTADO DE TURNOS ---")
            fecha_input = input("Ingrese la fecha para el reporte (EJEMPLO:2025-06-20), o presioná ENTER para ver TODOS: ").strip()
            
            if fecha_input:
                
                manager.ver_turnos(fecha=fecha_input)
            else:
            
                manager.ver_turnos(fecha=None) 

        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        