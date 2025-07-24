class Circulo:
    def __init__(self, radio) -> None:
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio**2
    
    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio
    

circulos = []

for i in range(3):
    c = Circulo(i+1)
    circulos.append(c)

for c in circulos:
    print(c.calcular_area())
