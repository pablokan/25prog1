class ColaPrioridad:
    def __init__(self, valor=None, prioridad=None, orden_llegada=None):
        self.valor = valor
        self.prioridad = prioridad
        self.orden_llegada = orden_llegada
        self.elementos = []
        self.contador_llegada = 0

    def insertar(self, elem, prioridad):
        nuevo = {"valor": elem, "prioridad": prioridad, "orden_llegada": self.contador_llegada}
        self.contador_llegada += 1

        i = len(self.elementos) - 1
        while i >= 0 and self.comparar_elems(self.elementos[i], nuevo) > 0:
            i -= 1
        self.elementos.insert(i + 1, nuevo)

    def eliminar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop(0)["valor"]

    def observar(self):
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.elementos[0]["valor"]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamanio(self):
        return len(self.elementos)

    def comparar_elems(self, a, b):
        if a["prioridad"] != b["prioridad"]:
            return a["prioridad"] - b["prioridad"]
        return a["orden_llegada"] - b["orden_llegada"]
