class Auto:
    def __new__(cls, puertas) -> object:
        objeto = super().__new__(cls)
        print('Yo soy __new__, el constructor: ', end='')
        print(f'Creando instancia de Auto con {puertas} puertas')
        return objeto

    def __init__(self, puertas) -> None:
        auto = 'sedán' if puertas == 4 else 'coupé'
        print('Yo soy __init__, el inicializador: ', end='')
        print(f'Auto {auto} creado')


a1 = Auto(4)
a2 = Auto(2)
