from .manager_base import ManagerBase 

persona_db = ManagerBase(tabla="Persona") 
admin_db = ManagerBase(tabla="admin")
paciente_db = ManagerBase(tabla="Paciente")
mutual_db = ManagerBase(tabla="Mutuales")


def registrar_paciente():
    print("\n--- INGRESE SUS DATOS PARA REGISTRARSE ---")
    dni = input("DNI (será su usuario): ").strip()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    telefono = input("Teléfono: ").strip()
    
    if not dni or not nombre or not apellido:
        print("Error: DNI, Nombre y Apellido no pueden estar vacíos.")
        return False

    if persona_db.get_by_dni(dni):
        print("Error: Ya existe una persona registrada con ese DNI.")
        return False

    datos_persona = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
        
    }
    
    id_persona_insertada = persona_db.insert(datos_persona)

    if not id_persona_insertada:
        print("Error al registrar los datos personales.")
        return False

    mutual_particular = mutual_db.get_one_by_field('nombre', 'Particular')
    if not mutual_particular:
        print("Error: No se encontró la mutual 'Particular' por defecto.")
        return False
        
    id_mutual_default = mutual_particular['id']

    datos_paciente = {
        "id_persona": id_persona_insertada,
        "id_mutual": id_mutual_default
    }
    
    id_paciente_insertado = paciente_db.insert(datos_paciente)

    if not id_paciente_insertado:
        print("Error al registrar los datos del paciente.")
        return False

    print(f"¡Registro exitoso! Paciente {nombre} {apellido} (DNI: {dni}) creado.")
    return True

def login_paciente():
    
    dni = input("DNI de paciente: ").strip()
    persona = persona_db.get_by_dni(dni)
    
    if persona:
        print(f"Login de Paciente exitoso (DNI: {dni}).")
        return {"dni": dni, "rol": "paciente"} 
    
    print("Login fallido. El DNI no se encuentra registrado.")
    return None

def login_admin():
    user = input("Usuario Admin: ").strip()
    password = input("Contraseña: ").strip()
    
    admin = admin_db.get_one_by_field('USER', user)
    
    if admin and admin['PASSWORD'] == password:
        print(f"Login de Administrador exitoso (Usuario: {user}).")
        return {"user": user, "rol": "admin"}
    
    print("Login fallido. Usuario o contraseña incorrectos.")
    return None