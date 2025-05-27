# Dada la string en la variable persona, quiero obtener el apellido
persona = "Elisabeth Cleeve,Norway(Europe),04-03-1991"

# Cuales funciones u operaciones conozco?
# find, split, slicing

anio_solicitado = 2000
lista_persona = persona.split(',')
nombre_completo = lista_persona[0]
lista_nombre_apellido = nombre_completo.split()
_, apellido = lista_nombre_apellido
anio_nacimiento = int(persona[-4:])
if anio_nacimiento < anio_solicitado:
    print(apellido)

