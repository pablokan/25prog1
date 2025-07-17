# Composición propiamente dicha
# clase dependiente DEBE ser obligatoriamente instanciada

class Puerta():
    def __init__(self, uv, uh) -> None:
        self.uv = uv
        self.uh = uh

    def abrir_puerta(self):
        print(f"Abierta la puerta {self.uv} {self.uh}")
        
    def cerrar_puerta(self):
        print(f"Cerrada la puerta {self.uv} {self.uh}")

class Auto():
    def __init__(self, tipo_auto, nombre) -> None:
        # Composición
        print(nombre, end=": ")
        self.di = Puerta("delantera", "izquierda") # agrega una puerta
        self.dd = Puerta("delantera", "derecha") # agrega otra puerta
        if tipo_auto == "sedán":
            self.ti = Puerta("trasera", "izquierda")
            self.td = Puerta("trasera", "derecha")

cupecita = Auto("cupé", "Cupecita")
cupecita.di.abrir_puerta()
cupecita.di.cerrar_puerta()
duna = Auto("sedán", "Duna")
duna.td.abrir_puerta()
