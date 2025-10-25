from .funciones_generales import input_choice

#refactorizar a una funcion mas general
def input_inventario(personaje,msj = "",msj_salida = ""):
    try:
        opciones = generar_opciones(personaje)
        opcion_elegida = input_choice(opciones,msj,msj_salida)
        opcion_elegida = int(opcion_elegida)
        opcion_final = opcion_elegida - 1
        return opcion_final
    except:
        raise ValueError("Error input_inventario")  


def generar_opciones(jugador):
    limite_inventario = jugador.inventario._limite
    lista_opciones = []
    for i in range(limite_inventario):
        opcion = i+1
        opcion = str(opcion)
        lista_opciones.append(opcion)

    return lista_opciones


