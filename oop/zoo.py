class Animal:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.esta_durmiendo = False

    def comer(self):
        print(f"{self.nombre} ({self.especie}) está comiendo.")

    def dormir(self):
        if not self.esta_durmiendo:
            print(f"{self.nombre} ({self.especie}) se ha dormido.")
            self.esta_durmiendo = True
        else:
            print(f"{self.nombre} ({self.especie}) ya está durmiendo.")

    def despertar(self):
        if self.esta_durmiendo:
            print(f"{self.nombre} ({self.especie}) se ha despertado.")
            self.esta_durmiendo = False
        else:
            print(f"{self.nombre} ({self.especie}) ya está despierto.")

    def info(self):
        return f"Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad} años, Durmiendo: {self.esta_durmiendo}"

class Leon(Animal):
    def __init__(self, nombre, edad, melena_frondosa=True):
        super().__init__(nombre, "León", edad)
        self.melena_frondosa = melena_frondosa

    def rugir(self):
        print(f"¡{self.nombre} ({self.especie}) ruge fuertemente: GRRRR!")

    def cazar(self):
        print(f"{self.nombre} ({self.especie}) está al acecho, buscando presas.")

    def info(self):
        base_info = super().info()
        return f"{base_info}, Melena frondosa: {'Sí' if self.melena_frondosa else 'No'}"

class Pinguino(Animal):
    def __init__(self, nombre, edad, tipo_pinguino):
        super().__init__(nombre, "Pingüino", edad)
        self.tipo_pinguino = tipo_pinguino # Ej: Rey, Adelia, Emperador

    def nadar(self):
        print(f"{self.nombre} ({self.especie}) del tipo {self.tipo_pinguino} está nadando elegantemente.")

    def deslizarse_sobre_hielo(self):
        print(f"{self.nombre} ({self.especie}) se desliza graciosamente sobre el hielo.")

    def info(self):
        base_info = super().info()
        return f"{base_info}, Tipo: {self.tipo_pinguino}"

class Serpiente(Animal):
    def __init__(self, nombre, edad, es_venenosa):
        super().__init__(nombre, "Serpiente", edad)
        self.es_venenosa = es_venenosa

    def sisear(self):
        print(f"{self.nombre} ({self.especie}) sisea: Ssssss...")

    def mudar_piel(self):
        print(f"{self.nombre} ({self.especie}) está mudando su piel.")

    def info(self):
        base_info = super().info()
        return f"{base_info}, Venenosa: {'Sí' if self.es_venenosa else 'No'}"

# Uso de las clases
print("--- Animales del Zoológico ---")
simba = Leon("Simba", 7, True)
print(simba.info())
simba.comer()
simba.rugir()
simba.dormir()
simba.despertar()
print("\n")

pingu = Pinguino("Pingu", 3, "Adelia")
print(pingu.info())
pingu.nadar()
pingu.deslizarse_sobre_hielo()
print("\n")

kass = Serpiente("Kass", 5, True)
print(kass.info())
kass.sisear()
kass.mudar_piel()
kass.dormir()
kass.despertar()
print("\n") 