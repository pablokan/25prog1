# parámetros con nombre y valor de cantidad variable (diccionario)

def alumno(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(f"{k} -> {v}")

alumno(nombre="Juan", apellido="Torres", localidad="Río Cuarto")

""" 
def alumno(nombre, *args, apellido, localidad="Río Cuarto", **kwargs):
    otros_nombres = " ".join(args)
    print(f"El alumno {nombre} {otros_nombres} es de {localidad} y su apellido es {apellido}")
    if kwargs != {}:
        print("Otra data:")
        for k, v in kwargs.items():
            print(f"{k}: {v}")

alumno("Juan", apellido="Torres", localidad="San Basilio")
alumno("Pablo", 'Esteban', 'Miguel', apellido="Sosa")
#alumno("Pipo", 'Sosa')
alumno("Ana", apellido='Torres', localidad="Jovita", Observaciones="abanderada")



def foo(a, b, *args, n1="ene uno", **kwargs):
    print(a, b, args, n1, kwargs)

foo(1, 2, 3, 4, 5, xX="equisequis", n1="nuevo ene uno", nN="algo")
 """