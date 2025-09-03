class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo) -> None:
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        
    @property
    def numero_cuenta(self):
        return self._numero_cuenta
    
    @numero_cuenta.setter
    def numero_cuenta(self, nueva_cuenta):
        self._numero_cuenta = nueva_cuenta
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        if isinstance(nuevo_saldo, (int, float)):
            self._saldo = nuevo_saldo
        else:
            raise ValueError('El saldo debe ser un numero')
             
    def obtener_saldo(self, retiro):
        self.saldo -= retiro
        return self.saldo
        
    def saldo_positivo(self):
        if self.saldo > 0:
            return True
        elif self.saldo < 0:
            return False
        else:
            return 'Saldo 0'
        
    def __str__(self) -> str:
        return f'Datos Cuenta {self.numero_cuenta} ----> Saldo {self.saldo}'
        
class CajaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, tasa_interes) -> None:
        super().__init__(numero_cuenta, saldo)
        self.tasa_interes = tasa_interes
        
    @property
    def tasa_interes(self):
        return self._tasa_interes
    
    @tasa_interes.setter
    def tasa_interes(self, tasa):
        if isinstance(tasa, (int, float)) and 0 <= tasa <= 100:
            self._tasa_interes = tasa
        else:
            raise ValueError('Error: Revisar que la tasa se encuentre entre 0 y 100')
        
class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, limite_giro_descubierto) -> None:
        super().__init__(numero_cuenta, saldo)
        self.limite_giro_descubierto = limite_giro_descubierto
        
    @property
    def limite_giro_descubierto(self):
        return self._limite_giro_descubierto
    
    @limite_giro_descubierto.setter
    def limite_giro_descubierto(self, limite):
        if isinstance(limite, float):
            self._limite_giro_descubierto = limite
        else:
            raise ValueError('Coloque un numero flotante')
        
    def obtener_saldo(self, retiro):
        self.saldo -= retiro
        if self.saldo < (-1*self.limite_giro_descubierto):
            print('Su limite no alcanza, operación rechazada')
            self.saldo += retiro
            return self.saldo
        else:
            return self.saldo
        
    
        
# cuenta1 = CajaAhorro('9999', 10000, 35)
# print(cuenta1)
# print(cuenta1.obtener_saldo(1000))


cuenta2 = CuentaCorriente('5555', 10000, 5000.0)
print(cuenta2)

cuenta2.obtener_saldo(5000)
cuenta2.obtener_saldo(5000)
print(cuenta2)
cuenta2.obtener_saldo(3000)
print(cuenta2)
cuenta2.obtener_saldo(5000)
print(cuenta2)
