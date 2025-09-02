""" 
# Paso 1: Clases
class CajaAhorro:
    def __init__(self, numero_cuenta, saldo, tasa_interes):
        self._numero_cuenta = numero_cuenta
        self._saldo = saldo
        self._tasa_interes = tasa_interes

    def obtener_saldo(self):
        return self._saldo

class CuentaCorriente:
    def __init__(self, numero_cuenta, saldo, limite_giro_descubierto):
        self._numero_cuenta = numero_cuenta
        self._saldo = saldo
        self._limite_giro_descubierto = limite_giro_descubierto

    def saldo_positivo(self):
        return self._saldo > 0
"""
# Paso 2: Generalización
class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self._numero_cuenta = numero_cuenta
        self._saldo = saldo

    def obtener_saldo(self):
        return self._saldo

class CajaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, tasa_interes):
        super().__init__(numero_cuenta, saldo)
        self._tasa_interes = tasa_interes

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo, limite_giro_descubierto):
        super().__init__(numero_cuenta, saldo)
        self._limite_giro_descubierto = limite_giro_descubierto

    def saldo_positivo(self):
        return self._saldo > 0

# Paso 3: Pruebas
caja_ahorro = CajaAhorro("CA-123", 5000, 0.05)
cuenta_corriente = CuentaCorriente("CC-456", 200, 1000)
print(f"Saldo de la caja de ahorro: {caja_ahorro.obtener_saldo()}")
print(f"¿La cuenta corriente tiene saldo positivo? {cuenta_corriente.saldo_positivo()}")