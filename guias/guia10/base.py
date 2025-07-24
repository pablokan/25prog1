class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(self.marca, self.modelo)

def main():
    print(f'\n{'-'*80}\n')
    fitito = Auto('Fiat', '600')
    r12 = Auto('Renault', 'R12')
    fitito.mostrar_info()
    r12.mostrar_info()
    
if __name__ == '__main__':
    main()

