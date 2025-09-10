class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Gato(Animal):
    def hablar(self):
        print(f'{self.nombre} hace miau')

g = Gato('Shevek')
g.hablar()
