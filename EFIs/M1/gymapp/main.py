#Imports
from modulos.actividad import Actividad
from modulos.persona import Alumno, Profesor
from datetime import date
from modulos.gestor import *
from modulos.gestion_alumnos import *
from modulos.fgestor import *
#MAIN 

#Datos Base
precio_fijo = 5000
profesor1 = Profesor('Jacobo', 'Zunino', 44543321, 'Musculacion')
actividad1 = Actividad('Musculacion', profesor1)
#Lista Base

alumnos_totales = cargar_txt("alumnos.txt")
alumnos_activos = [a for a in alumnos_totales if a.activo]

#Menu interactivo
def menu():
    while True:
        print("\n--- MENU GYMAPP ---")
        print("1. Inscribir")
        print("2. Renovar Cuota")
        print("3. Verificar vencimientos")
        print("4. Listar alumnos activos")
        print("5. Calcular renumeracion del profesor (No disponible)") 
        print("7. Salir")

        opcion = input('Elegi una opcion: ')

        if opcion == "1":
            menu_inscripcion()

        elif opcion == "2":
            menu_renovar_cuota()

        elif opcion == "3":
            menu_vencimiento()

        elif opcion == "4":
            menu_alumnos_activos()

        elif opcion == "5":
            menu_calculo_renumeraciones()

        elif opcion == "7":
            print("Cerrando sistema...")
            break

        else:
            print("ERROR: Opcion invalida.")

# SUBMENUS
def menu_inscripcion():
    while True:
        print("\n --- Menu de Inscripcion --- ")
        print("1. Inscribir alumno")
        print("2. Inscribir alumno a actividad")
        print("3. Anadir nuevo Profesor (No disponible)")
        print("7. Volver a anterior menu")

        opcion = input("Elegi una opcion: ")

        if opcion == "1":
            nuevo = cargar_alumno(alumnos_totales)
            if nuevo:
                alumnos_totales.append(nuevo)
                guardar_alumno_txt(nuevo)

        elif opcion == "2":
            pass

        elif opcion == "3":
            dni = int(input("DNI del alumno a inscribir: "))
            for alumno in alumnos_totales:
                if alumno.dni == dni:
                    actividad1.alumnos.append(alumno)
                    print(f"{alumno.nombre} fue inscripto en {actividad.nombre}")
                    break
            else:
                print("ERROR: Alumno no encontrado.")

        elif opcion == "7":
            break

        else:
            print("ERROR: Selecciona una opcion valida")

def menu_renovar_cuota():
    while True:
        print("\n --- Menu de Renovacion Cuota --- ")
        print("1. Renovar Cuota")
        print("7. Volver a anterior menu")

        opcion = input("Elegi una opcion: ")
        if opcion == "1":
            dni = int(input("DNI del alumno a renovar: "))
            for alumno in 'alumnos.txt':
                if alumno.dni == dni:
                    renovar_pago(alumno)
                    if alumno not in 'alumnos.txt':
                        alumnos_activos.append(alumno)
                    break
            else:
                print("ERROR: Alumno no encontrado.")
        elif opcion == "7":
            break
        else:
            print("ERROR: Alumno no encontrado.")

def menu_vencimiento():
    while True:
        print("\n --- Menu Vencimientos --- ")
        print("1. Mostrar vencimientos")
        print("7. Volver al menu principal")

        opcion = input("Elegi una opcion: ")

        if opcion == "1":
            vencimiento(alumno)
        elif opcion == "7":
            break
        else:
            print("Error: invalido")

def menu_alumnos_activos():
    while True:
        print("\n --- Menu Alumnos Activos --- ")
        print("1. Mostrar alumnos activos")
        print("7. Volver al menu principal")

        opcion = input("Elegi una opcion: ")

        if opcion == "1":
            print("\n --- Alumnos activos ---")
            for a in alumnos_activos:
                print(f"{a.nombre} {a.apellido} - DNI: {a.dni}")
        elif opcion == "7":
            break
        else: 
            print("ERROR: No se pudo correr la lista")

def menu_calculo_renumeraciones():
     while True:
        print("\n --- Menu de renumeraciones --- ")
        print("1. Calcular renumeraciones")
        print("7. Volver al menu principal")

        opcion = input("Elegi una opcion: ")

        if opcion == "1":
            print("Aun no disponible")
            #deberia printear a  los profesores, no buscarlos por DNI.. mas facil asi
        elif opcion == "7":
            break
        else:
            print("ERROR: Profesor no encontrado")




        

menu()

