'''
(Herencia por Generalizacion)
CajaAhorro y CuentaCorriente a CuentaBancaria
Paso1:Clases:
-Crea una clase CajaAhorro con los atributos privados _numero_cuenta, _saldo, _tasa_interes(flotante).
-Agrega un metodo obtener_saldo()
-Crea una clase Clase CuentaCorriente con los atributos privados _numero_cuenta, _saldo, _limite_giro_descubierto(floatante).
-Agrega un metodo saldo_positivo() que retorne verdadero o falso
Paso2: Generalizacion
Paso3: Pruebas
-Superar el limite de giro en descubierto.
-Avisar si se tiene saldo negativo
'''

class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self._numero_cuenta = numero_cuenta
        self._saldo = saldo

    def __str__(self):
        return f'Numero_cuenta: {self._numero_cuenta} \nSaldo: ${self._saldo} \n'

class CajaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, tasa_interes):
        super().__init__(numero_cuenta, saldo)
        self._tasa_interes = tasa_interes

    def obtener_saldo(self):
        return self._saldo
    
    def __str__(self):
        return f'Caja de Ahorro \n{super().__str__()}Tasa_interes: {self._tasa_interes}'

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, limite_giro_descubierto):
        super().__init__(numero_cuenta, saldo)
        self._limite_giro_descubierto = limite_giro_descubierto
    
    def saldo_positivo(self):
        if self._saldo > 0:
            return True
        else:
            print('El saldo se encuentra negativo')
            return False

    def retirar(self, monto):
        if self._saldo - monto < -self._limite_giro_descubierto:
            print(f'No se puede retirar ${monto}: excede el limite de giro en descubierto')
            return False
        
        else:
            self._saldo -= monto
            print(f'Se retiro ${monto} - Saldo Actual: ${cuenta_corriente._saldo}')
            return True

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f'Se deposito ${monto} - Saldo Actual: ${cuenta_corriente._saldo}')
            return True
        
        else:
            print(f'El monto {monto} debe ser  positivo')
            return False
        
    def __str__(self):
        return f'\nCuenta Corriente \n{super().__str__()}Limite de giro en descubierto: {self._limite_giro_descubierto}\n'


caja_ahorro = CajaAhorro(2425, 5000.0, 0.05)
cuenta_corriente = CuentaCorriente(3420, 1500.0, 1000.0)
print(caja_ahorro)
print(cuenta_corriente)

cuenta_corriente.retirar(2000)

cuenta_corriente.retirar(1500)
cuenta_corriente.saldo_positivo()
cuenta_corriente.depositar(700)