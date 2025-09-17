class Auto:
    def __init__(self) -> None:
        self.pdi = Puerta('d', 'i')
        self.pdd = Puerta('d', 'd')

    def __str__(self):
        return f'Este auto tiene: {str(self.pdi)} {self.pdd}'


class Puerta:
    def __init__(self, uv, uh) -> None:
        self.uv = uv
        self.uh = uh

    def __str__(self):
        pos_vertical = 'delantera' if self.uv == 'd' else 'trasera'
        pos_horizontal = "izquierda" if self.uh == 'i' else 'derecha'
        return f'Puerta {pos_vertical} {pos_horizontal}'


autito = Auto()
print(autito)
