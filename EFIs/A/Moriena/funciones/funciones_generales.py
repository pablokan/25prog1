import time


def mensaje_delay(mensaje: str, delay: float = 0.05,salto_linea:bool = True):
    for letra in mensaje:
        print(letra, end='', flush=True)
        time.sleep(delay)
    if salto_linea == True:
        print()

#---------------------------------------------------------------------------------------

def input_choice(lista_opciones,msj="",msj_error = ""):
    validar=False
    while validar == False:
        opcion_elegir=input(msj)
        if opcion_elegir in lista_opciones:
            opcion_final=opcion_elegir
            validar=True
        else:
            print(msj_error)

    return opcion_final
