from .cliente import Cliente
from .boleto import Boleto
from .producto import Producto
from .asiento import Asiento

class Reserva:
    def __init__(self, cliente, fecha: str)-> None:
        self.cliente = cliente
        self.fecha = fecha
        self.boletos: list[Boleto] = []
        self.productos_comprados: list[Producto] = []
    
    @property
    def cliente(self):
        return self._cliente
    
    @cliente.setter
    def cliente(self, cliente)-> None:
        if not isinstance(cliente, Cliente):
            raise TypeError('El cliente debe ser una instancia de la clase Cliente.')
        else:
            self._cliente = cliente
    
    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self, fecha: str)-> None:
        if not isinstance(fecha, str):
            raise TypeError('La fecha ingresada debe ser tipo string en el siguiente formato: "DD/MM/AA".')
        else:
            self._fecha = fecha
    
    def agregar_producto(self, producto: Producto):
        if not isinstance(producto, Producto):
            raise TypeError('Solo se pueden agregar objetos de tipo Producto.')
        else:
            self.productos_comprados.append(producto)

    def agregar_boleto(self, boleto: Boleto):
        if not isinstance(boleto.asiento, Asiento):
            raise TypeError('El asiento del boleto no es válido.')
        
        reservado = boleto.asiento.reservar()
        if reservado:
            self.boletos.append(boleto)
            print('Boleto agregado con éxito.')
        else:
            print('Error: El asiento del boleto ya está ocupado.')

    def calcular_total(self):
        total = 0.0
        for boleto in self.boletos:
            total += boleto.obtener_precio()
        for item in self.productos_comprados:
            total += item.obtener_precio()
        return total

    def guardar_en_archivo(self):
        with open('base_de_datos/reservas.txt', 'a', encoding='utf-8') as f:

            datos_reserva = str(self)
            f.write(datos_reserva)
            f.write('\n====================================================\n')

    def __str__(self):
        info = f'--- RESERVA (total: ${self.calcular_total()}) ---\n'
        info += f'Cliente: {self.cliente.nombre} {self.cliente.apellido}\n'
        info += f'Fecha: {self.fecha}\n'
        info += '\nBoletos:\n'
        for b in self.boletos:
            info += f' -{str(b)}\n'
        info += '\nAnexos:\n'
        for anexo in self.productos_comprados:
            info += f' -{str(anexo)}\n'
        
        return info