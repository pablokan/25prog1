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
        return f"{self.__class__.__name__}(valor={self.valor})"

    def __add__(self, otro_numero):
        if isinstance(otro_numero, (int, float)):
            nuevo_contador = self.__class__()
            nuevo_contador._valor = self.valor + otro_numero
            return nuevo_contador
        else:
            raise TypeError("Se esperaba un tipo numérico")
        
class ContadorDecremento(ContadorSimple):
    def decrementar(self):
        if self._valor > 0:
            self._valor -= 1
        else:
            print("El valor no puede ser menor a 0.")

# Probar la clase
contador = ContadorDecremento()
contador.incrementar()
contador.incrementar()
nuevo_contador = contador + 5.5
nuevo_contador.decrementar()
print(contador)
print(repr(nuevo_contador))