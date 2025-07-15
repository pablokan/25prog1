# Polimorfismo (duck typing)
class Gato:
    especie = 'gato'
    def actividad(self):
        return "Saltar"

class Auto:
    especie = 'auto'
    def actividad(self):
        return "Gastar nafta" # No es un animal, pero tiene un método 'actividad'

# Usando Duck Typing:
objetos_varios = [Gato(), Auto()]

for obj in objetos_varios:
    print(f"El {obj.especie} se dedica a: {obj.actividad()}")
    