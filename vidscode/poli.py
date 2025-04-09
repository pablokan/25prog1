from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self) -> None:
        ...

class Perro(Animal):
    def hablar(self) -> None:
        print('guau')

class Gato(Animal):
    def hablar(self) -> None:
        print('miau')

def dice(animal: Animal):
    animal.hablar()

firulais = Perro()
michifuz = Gato()

dice(firulais)
dice(michifuz)
