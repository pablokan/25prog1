from creacion_objetos.creacion_inventario import casco_hades,casco_hola,espadita
from creacion_objetos.creacion_personajes import jugador_barbaro,jugador_mago
from funciones.funciones_personajes import cambiar_equipamiento
from funciones.funciones_generales import mensaje_delay

#mini pruebas de inventario

jugador_barbaro.inventario.guardar_objeto(casco_hades)
jugador_barbaro.inventario.guardar_objeto(casco_hola)
jugador_barbaro.inventario.guardar_objeto(espadita)

mensaje_delay("-------------------Este es el inventario-----------------------")
msjm=cambiar_equipamiento(jugador_barbaro)
jugador_barbaro.inventario.listar_equipamiento_inventario()
jugador_barbaro.calcular_estadisticas()
#jugador_barbaro.calcular_estadisticas()

print((jugador_barbaro))