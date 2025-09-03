class ContadorSimple:
    def __init__(self):
        self._valor = 0

    @property
    def valor(self):
        return self._valor

    def incrementar(self):
        self._valor += 1

    def __str__(self):
        return f"Contador: {self.valor}"

    def __repr__(self):
        return f"ContadorSimple(valor={self.valor})"

    def __add__(self, otro_numero):
        if isinstance(otro_numero, (int, float)):
            nuevo_contador = ContadorSimple()
            nuevo_contador._valor = self.valor + otro_numero
            return nuevo_contador
        else:
            raise TypeError("Se esperaba un tipo numérico")

# Probar la clase
contador = ContadorSimple()
contador.incrementar()
contador.incrementar()
nuevo_contador = contador + 5.5
nuevo_contador.incrementar()
print(contador)
print(repr(nuevo_contador))