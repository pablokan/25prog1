class CuentaBancaria:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
        print(f'Saldo inicial ${self.saldo}')

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f'Deposito ${cantidad}. Saldo ${self.saldo}')
        
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print('Saldo insuficiente. Operación cancelada. ', end='')
        else:
            self.saldo -= cantidad
            print(f'Retiro ${cantidad}. ', end='')
        print(f'Saldo ${self.saldo}')

def main():
    print(f'\n{'-'*80}')
    cuenta_pablo = CuentaBancaria(111, 100)
    cuenta_pablo.depositar(100)
    cuenta_pablo.retirar(250)
    cuenta_pablo.retirar(45)
    print(f'{'-'*80}\n')

if __name__ == '__main__':
    main()



