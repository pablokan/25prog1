from modulos.actividad import *
from modulos.gestor import *
from modulos.alumno import Alumno
from datetime import date

#Funciones 
def mostrar_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos registrados")
    else:
        print("\n --- Lista de Alumnos --- ")
        for i, a in enumerate(alumnos, 1):
            print(f"{i}. {a.nombre} {a.apellido} | DNI: {a.dni} | Alta: {a.fecha_alta} | Activo: {a.activo}")

def mostrar_alumnos_actividad(actividades):
    print("\n --- Alumnos por Actividad --- ")
    for act in actividades:
        print(f"\n {act.nombre.upper()}")
        if not act.alumnos:
            print("No hay alumnos inscriptos en esta activdad.")
        else:
            for i, a in enumerate(act.alumnos, 1):
                print(f" {i}. {a.nombre} {a.apellido} | DNI: {a.dni}")

def agregar_alumno(alumnos):
    print("\n--- Nuevo Alumno ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    #Validacion de DNI.
    if not dni.isdigit() or len(dni) > 8:
        print("El DNI debe contener exactamente 8 numeros o menos ")
        return

    for a in alumnos:
        if str(a.dni) == dni.strip():
            print(f"Ya existe un alumno con el DNI {dni}: {a.nombre} {a.apellido}.")
            return

    fecha = date.today()
    nuevo = Alumno(nombre, apellido, dni, fecha, True)
    alumnos.append(nuevo)
    print(f"Alumno: {nombre} {apellido} agregado con exito.")


#Submenus
def menu_agregar_alumnos(alumnos, actividades):
    while True: 
        print("\n --- Menu Inscripcion ---")
        print("1. Inscribir alumno")
        print("2. Inscribir alumno a actividad.")
        print("7. Volver al menu principal.")

        opcion = input("Elija una opcion: ")

        if opcion == "1":
            agregar_alumno(alumnos)
            guardar_alumnos(alumnos)
        elif opcion == "2":
            inscribir_alumno_en_actividad(alumnos, actividades)
        elif opcion == "7":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")

def menu_mostrar_alumnos(alumnos, actividades): 
    while True:
        print("\n --- Menu Datos ---")
        print("1. Mostrar todos los Alumnos")
        print("2. Mostrar Alumnos por actividad.")
        print("7. Volver al menu principal.")


        opcion = input("Elija una opcion: ")

        if opcion == "1":
            mostrar_alumnos(alumnos)
        elif opcion == "2":
            mostrar_alumnos_actividad(actividades)
        elif opcion == "7":
            break
        else:
            print("Opcion invalida. Intente de nuevo.")

        



#Menu

def menu():
    actividades = [
        Actividad("Musculacion"),
        Actividad("Crossfit"),
        Actividad("Yoga")
    ]

    alumnos = cargar_alumnos()

    while True:
        print("\n--- GESTOR ALUMNOS GYM APP --- ")
        print("1. Informacion de Alumnos")
        print("2. Gestion alumnos")
        print("3. Salir")

        opcion = input("Elija una opcion: ")

        if opcion == "1":
            menu_mostrar_alumnos(alumnos, actividades)
        elif opcion == "2":
            menu_agregar_alumnos(alumnos, actividades)
        elif opcion == "3":
            break
        else:
            print("Opcion invalida. Intente de nuevo")

         

if __name__ == "__main__":
    menu()   