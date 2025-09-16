class Arma:
    def __init__(self, nombre, danio):
        self.nombre = nombre
        self.danio = danio

class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        self.arma = None  # Composición: Un personaje "tiene un" arma.

    def equipar_arma(self, arma):
        if isinstance(arma, Arma):
            self.arma = arma
            print(f"{self.nombre} ha equipado {self.arma.nombre}.")
        else:
            print(f"Error: {arma} no es una instancia de la clase Arma.")

    def atacar(self, objetivo):
        if self.arma:
            dano_total = self.arma.danio
            print(f"{self.nombre} ataca a {objetivo.nombre} con {self.arma.nombre} y causa {dano_total} de daño.")
            objetivo.recibir_dano(dano_total)
        else:
            print(f"{self.nombre} no tiene un arma equipada y no puede atacar.")

    def recibir_dano(self, dano):
        """Reduce la vida del personaje al recibir daño."""
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nombre} ha sido derrotado.")
        else:
            print(f"La vida de {self.nombre} ahora es {self.vida}.")

class Guerrero(Personaje):
    def __init__(self, nombre, vida, fuerza):
        super().__init__(nombre, vida)
        self.fuerza = fuerza

    def atacar(self, objetivo):
        if self.arma:
            dano_total = self.arma.danio + self.fuerza
            print(f"{self.nombre} (Guerrero) ataca a {objetivo.nombre} con su {self.arma.nombre} y un bono de fuerza, causando {dano_total} de daño.")
            objetivo.recibir_dano(dano_total)
        else:
            print(f"{self.nombre} no tiene un arma equipada y no puede atacar.")

class Mago(Personaje):
    def __init__(self, nombre, vida, mana):
        super().__init__(nombre, vida)
        self.mana = mana

    def atacar(self, objetivo):
        if self.arma and self.mana > 0:
            dano_total = self.arma.danio * 2  # Los ataques mágicos son más poderosos
            self.mana -= 10
            print(f"{self.nombre} (Mago) lanza un hechizo a {objetivo.nombre} con su {self.arma.nombre}, consumiendo 10 de maná y causando {dano_total} de daño.")
            objetivo.recibir_dano(dano_total)
        elif self.mana <= 0:
            print(f"{self.nombre} no tiene suficiente maná para lanzar un hechizo.")
        else:
            print(f"{self.nombre} no tiene un arma equipada y no puede atacar.")


if __name__ == "__main__":
    espada_larga = Arma("Espada Larga", 20)
    baston_magico = Arma("Bastón Mágico", 15)

    heroe_guerrero = Guerrero("Aragorn", 100, 5)
    enemigo_mago = Mago("Malekith", 80, 50)

    heroe_guerrero.equipar_arma(espada_larga)
    enemigo_mago.equipar_arma(baston_magico)

    print("\n--- ¡Comienza el combate! ---")
    
    # Turno 1
    heroe_guerrero.atacar(enemigo_mago)
    print("---")
    enemigo_mago.atacar(heroe_guerrero)
    print("---")

    # Turno 2
    heroe_guerrero.atacar(enemigo_mago)
    print("---")
    enemigo_mago.atacar(heroe_guerrero)
    print("---")

    # Turno 3
    heroe_guerrero.atacar(enemigo_mago)