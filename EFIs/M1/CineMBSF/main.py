from modulos.clases.cliente import Cliente
from modulos.clases.pelicula import Pelicula
from modulos.clases.sala import Sala
from modulos.clases.boleto import Boleto
from modulos.clases.reserva import Reserva
from modulos.clases.producto import Comestible, Bebida
from modulos.clases.cartelera import Cartelera

print()
print('¡Bienvenido al Cine MBSF!')
print()

#creacion de los asientos
sala1 = Sala(1, 50)
sala1.crear_asientos()

#peliculas
pelicula1 = Pelicula('Rocky I', '2:00 hs', 'Acción, Suspenso, Deportes', '1980', 'Boxeador lucha', 'Silvester Stalone, ...')
pelicula2= Pelicula('Rapidos y Furiosos 2', '2:23', 'Accion', '2007', 'Carreras de autos', 'Vin Disel, ...')
precio_entrada = 15000

#cartelera
cartelera1 = Cartelera()
cartelera1.agregar_pelicula(pelicula1)
cartelera1.agregar_horario('20:00')
cartelera1.agregar_pelicula(pelicula2)
cartelera1.agregar_horario('23:00')
print('---------')
print('CARTELERA')
print('---------')
print(cartelera1.mostrar_cartelera())

#cliente
cliente1 = Cliente("Diego Armando","Maradona",358456710)
cliente2 = Cliente('Lionel Andrés', 'Messi', 3585448711)

#reservar
reserva_diego = Reserva(cliente1, '10/10/2025')
reserva_leo = Reserva(cliente2, '22/10/2025')

asiento1 = sala1.buscar_asiento('A', 10)
asiento2 = sala1.buscar_asiento('A', 2)
asiento3 = sala1.buscar_asiento('C', 5)

boleto_d1 = Boleto(pelicula1, asiento1, cartelera1.horarios[0], sala1.numero, precio_entrada)
boleto_d2 = Boleto(pelicula1, asiento2, cartelera1.horarios[0], sala1.numero, precio_entrada)
boleto_l1 = Boleto(pelicula2, asiento3, cartelera1.horarios[1], sala1.numero, precio_entrada)

reserva_diego.agregar_boleto(boleto_d1)
reserva_diego.agregar_boleto(boleto_d2)
reserva_leo.agregar_boleto(boleto_l1)

#consumibles
pochoclos = Comestible(1,"Pochoclo", 3000)
coca = Bebida(2,"Gaseosa",'Coca Cola',5000)
agua = Bebida(3, 'Agua', 'Villavicencio', 3000)
print()
print('Productos disponibles:')
print(pochoclos)
print(coca)
print(agua)

#agregar productos
reserva_diego.agregar_producto(pochoclos)
reserva_diego.agregar_producto(coca)
reserva_leo.agregar_producto(agua)
print()
print(reserva_diego)
print(reserva_leo)
reserva_diego.guardar_en_archivo()
reserva_leo.guardar_en_archivo()



