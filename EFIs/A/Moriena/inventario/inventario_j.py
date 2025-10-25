#IMPORTACIONES
from items.clase_equipamiento import Equipamiento , Casco ,Pechera,Arma
from items.pociones import Pociones
from tabulate import tabulate


#CLASE INVENTARIO

class Inventario:
	def __init__(self,lista_objetos = []):
		self._bolsa_monedas = 0
		self._limite = 6
		self._lista_equipamiento = []
		self._lista_pociones = []
		for objeto in lista_objetos:
			self.guardar_objeto(objeto)
		
	#Getters y Setters--------------------------
	
	@property
	def lista_pociones(self):
		return self._lista_pociones
	@lista_pociones.setter
	def lista_pociones(self, nueva_lista):
		self._lista_pociones = nueva_lista

	@property
	def lista_equipamiento(self):
		return self._lista_equipamiento
	@lista_equipamiento.setter
	def lista_equipamiento(self, nueva_lista):
		self._lista_equipamiento = nueva_lista


	@property
	def bolsa_monedas(self):
		return self._bolsa_monedas
	@bolsa_monedas.setter
	def bolsa_monedas(self, nueva_bolsa):
		self._bolsa_monedas = nueva_bolsa
	
	#Metodos--------------------------------------
	def guardar_objeto(self, objeto):
		if isinstance(objeto,Pociones):
			if len(self._lista_pociones) < self._limite:
				self._lista_pociones.append(objeto)
				return (f"*Se añadio {objeto.nombre} en el inventario*")
			else:
				return (f"*No se puede añadir {objeto.nombre} en el inventario porque no hay espacio*")
		elif isinstance(objeto,Equipamiento):
			if len(self._lista_equipamiento) < self._limite:
				self._lista_equipamiento.append(objeto)
				return (f"*Se añadio {objeto.nombre} en el inventario*")
			else:
				return (f"*No se puede añadir {objeto.nombre} en el inventario porque no hay espacio*")
		else:
			raise ValueError("El objeto no es de ninguna de estas clases (Pociones,Equipamiento)")

	def sacar_objeto(self, objeto): #agregar, el equipo se saca solo si no equipado
		if isinstance(objeto,Pociones):
			self._lista_pociones.remove(objeto)
		elif isinstance(objeto,Equipamiento):
			self._lista_equipamiento.remove(objeto)
		else:
			raise ValueError("El objeto no es de ninguna de estas clases (Pociones,Equipamiento)")


	def listar_inventario(self):
		headers = ["Pocion", "Equipamiento", "Monedas"]
		datos_pociones = []
		datos_equipo = []
		cantidad_monedas = [f"$ {self._bolsa_monedas}"]
		datos = []
		if len(self._lista_pociones) > 0:
			for pocion in self._lista_pociones:
				datos_pociones.append(f"♦ {str(pocion)}")
		for x in range(self._limite):
				if len(datos_pociones) < self._limite:
					datos_pociones.append("")
		if len(self._lista_equipamiento) > 0:
			for equipo in self._lista_equipamiento:
				datos_equipo.append(f"• {str(equipo)}")
		for x in range(self._limite):
				if len(datos_equipo) < 6:
					datos_equipo.append("")
		for x in range(self._limite):
				if len(cantidad_monedas) < self._limite:
					cantidad_monedas.append("")
		for x in range(self._limite):
			datos.append([datos_pociones[x], datos_equipo[x], cantidad_monedas[x]])
		print(tabulate(datos, headers, tablefmt="grid"))


	def listar_equipamiento_inventario(self):
		header = ["Equipamiento","Tipo","Slot"]
		datos_equipo = []
		datos = []
		datos_tipos = []
		datos_orden = []
		numero_espacio_item = 1
		
		#Recorremos la lista de sumamos a la columna equipamiento el nombre objeto y a la columna tipo cual es el tipo del objeto
		
		if len(self._lista_equipamiento) > 0:
			for equipo in self._lista_equipamiento:
				datos_equipo.append(f"• {str(equipo)}")
				datos_orden.append(str(numero_espacio_item))
				tipo_equipo = equipo.tipo
				datos_tipos.append(tipo_equipo)
				numero_espacio_item+=1
				
		#Agregamos toda la informacion 
		
		for x in range(len(datos_equipo)):
			datos.append([datos_equipo[x],datos_tipos[x],datos_orden[x]])
		
		#Mostramos por pantalla
		
		print(tabulate(datos,header,tablefmt="grid"))

	
	def sumar_monedas(self, cantidad):
		self._bolsa_monedas += cantidad

	def restar_monedas(self, cantidad):
		self._bolsa_monedas -= cantidad

"""
#PRUEBAS
inventario = Inventario()
pocion1 = Pociones("Pocion de vida", "Vida", 10)
pocion2 = Pociones("Pocion de fuerza", "Daño", 5)
espada = Equipamiento("Espada")


inventario.guardar_objeto(pocion1)
inventario.guardar_objeto(pocion2)
inventario.guardar_objeto(espada)
inventario.listar_inventario()
#..(2 líneas restantes)
"""