from abc import ABC, abstractmethod

class Animal(ABC): # Clase Base Abstracta (ABC)
    @abstractmethod
    def habla(self) -> str:
        # Este método debe ser implementado por cualquier subclase de Animal
        pass

    def dormir(self): # Este es un método concreto, no abstracto
        return "zzz..."
    
class Perro(Animal): # Subclase Concreta 1
    def habla(self):
        return "Guau guau!"
    
    def __str__(self):
        return 'perro'

class Gato(Animal): # Subclase Concreta 2
    def habla(self):
        return "Miau!"

    def __str__(self):
        return 'gato'

animales = [Perro(), Gato()]
#a = Animal()
for animal in animales:
    print(f"El {animal} hace: {animal.habla()}")
    print(f"y duerme así: {animal.dormir()}") # También podemos llamar a métodos concretos