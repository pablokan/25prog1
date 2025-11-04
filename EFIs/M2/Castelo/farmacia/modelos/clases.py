from datetime import date

class Producto:
  def __init__(self, nombre, tipo, codigo, cantidad, precio, fecha):
    self.nombre = nombre
    self.tipo = tipo
    self.codigo = codigo
    self.cantidad = cantidad
    self.precio = precio
    self.fecha = fecha
    def __str__(self):
        return f"{self.tipo}: {self.nombre} - Código: {self.codigo} - Precio: ${self.precio}"
    

class Receta:
  def __init__(self, det_receta):
    self.det_receta = det_receta

class Factura:
  def __init__(self, monto, tipo, det_producto):
    self.monto = monto
    self.tipo = tipo
    self.det_producto = det_producto

class Venta:
  def __init__(self, observacion, cliente, usuario, producto):
    self.observacion = observacion
    self.cliente = cliente
    self.usuario = usuario
    self.producto = producto
    self.fecha = date.today()

class Personas:
    def __init__(self, nombre, apellido, dni, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f'{self.nombre} {self.apellido}, {self.dni}, {self.correo}, {self.telefono}'

class Proveedor(Personas):
    def __init__(self, nombre: str, telefono: str, direccion: str):
        super().__init__(nombre=nombre, apellido=None, dni=None, correo=None, telefono=telefono)
        self.direccion = direccion

class Medicamento(Producto):
  def __init__(self, nombre, fecha, codigo, cantidad ,venta_libre, precio ,proveedor: Proveedor):
    super().__init__(nombre,tipo="Medicamento", codigo=codigo, cantidad=cantidad, fecha=fecha, precio=precio)
    self.proveedor = proveedor
    self.venta_libre = venta_libre
    self.precio = precio

class Perfumeria(Producto):
  def __init__(self, nombre, codigo, cantidad, precio, fecha):
    super().__init__(nombre, tipo="Perfumeria", cantidad=cantidad, codigo=codigo, fecha=fecha)
    self.precio = precio

''''
class Receta:
    def _init_(self, ):
'''
class Farmacia():
  def __init__(self, nombre):
    self.nombre = 'Ibuprofeno&Fe'
    self.productos = []
  def __str__(self):
        return f"Farmacia: {self.nombre} con {len(self.productos)} productos"

class Usuario(Personas):
    def __init__(self, nombre, apellido, correo, contraseña):
        super().__init__(nombre, apellido, dni=None, correo=correo, telefono=None)
        self.contraseña = contraseña

    def __str__(self):
        return f'{self.nombre} {self.apellido}, {self.correo}, {self.contraseña}'

class Cliente(Personas):
    def __init__(self, nombre, apellido, dni, correo, telefono):
        super().__init__(nombre, apellido, dni, correo, telefono)

    def __str__(self):
        return f'{self.nombre} {self.apellido}, {self.dni}, {self.correo}, {self.telefono}'
