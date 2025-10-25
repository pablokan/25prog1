from personaje_clases.personajes import ClasesPersonaje
from .funciones_generales import input_choice
from .funciones_inventario import input_inventario
def ingresar_nombre_jugador(min_caracteres=2,max_caracteres = 18):
    verificar = False
    while verificar == False:
        nombre_jugador = input("Ingrese su nombre : ")
        nombre_jugador = str(nombre_jugador)
        if len(nombre_jugador) > max_caracteres:
            print(f"El máximo de carácteres permitidos son : {max_caracteres}")
        elif len(nombre_jugador) < min_caracteres:
            print(f"El mínimo de carácteres permitidos son : {min_caracteres}")
        else:
            verificar = True
            return nombre_jugador
        

#--------------------------------------------------------------------------------------

#Funcion para cambiar Inventario del jugador = refactorizar para un input general para el inventario
def cambiar_equipamiento(personaje:ClasesPersonaje):
    
    if isinstance(personaje,ClasesPersonaje):
        verificacion = False
        personaje.inventario.listar_equipamiento_inventario()
    
        while verificacion == False:
            opcion = input_inventario( personaje,msj="Selecciona el slot del equipamiento que desea cambiar: ",msj_salida="Opcion incorrecta\n")
            
            try:
                msj = f"{personaje.cambiar_items_activos(opcion)}\n"
                print(msj)
                msj_cambiar = input_choice(["1","2"],msj="Quiere seguir intercambiando items\n1-Si\n2-No\nEleccion: ",msj_error = "Opcion Incorrecta\n")
                personaje.inventario.listar_equipamiento_inventario()
                if msj_cambiar == "2":
                    verificacion = True
                    
            except:
               print("No tiene ese item")