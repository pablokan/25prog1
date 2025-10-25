from .personajes import ClasesPersonaje
from creacion_objetos.creacion_inventario import inventario_inicial_mago

class Mago(ClasesPersonaje):
   
   #determinar cuales van a ser los stats bases de clases
    vida_base = 100
    stamina_base = 50
    daño_base = 10
    nivel_base = 1
    exp_personaje = 0
    exp_subir_nivel = 100
    mana_base = 50
    mana_max = 100
    inv_inicial = inventario_inicial_mago

   
    def __init__(self,nombre):
        super().__init__(nombre, 
                        vida_base=self.vida_base,
                        stamina_base = self.stamina_base,
                        daño_base = self.daño_base,
                        nivel = self.nivel_base,
                        exp_personaje = self.exp_personaje,
                        exp_subir_nivel = self.exp_subir_nivel,
                        inventario = self.inv_inicial)
        
        self.mana = self.mana_base
    
    
    #------------------------Getters y Setters--------------------------#

    #Mana
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self,mana:int):
        if mana <= 0 :
            self._mana = 0
        elif mana > self.mana_max:
            self._mana = self.mana_max

        else:
            self._mana = mana

    #-----------------------------------Metodos--------------------------------------

    def subir_nivel(self):
        while self.exp_personaje >= self.exp_subir_nivel:
            self.nivel +=1
            self.vida += 5
            self.stamina += 7
            self.daño += 2
            self.exp_personaje-=self.exp_subir_nivel
            self.exp_subir_nivel+=50 *int(self.nivel*0.3)
            print(f"Subiste de nivel")


    def descansar(self):
        cantidad_recuperacion_mana = int(20 + (self.nivel*0.20))
        mana_antes_recuperacion = self.mana
        self.mana += cantidad_recuperacion_mana
        msj = f"Haz descansado recuperas {cantidad_recuperacion_mana} | {mana_antes_recuperacion} -> {self.mana}"
        return msj

    def atacar(self):
        daño = self.daño
        msj = f"Golpeaste al enemigo haz hecho {daño} de daño"
        return daño,msj

    def ataque_especial(self):
        if self.mana >= 20:
            daño = int(self.daño + 30 +(self.nivel*0.2)) 
            self.mana -= 20
            self.stamina -= 20
            msj = f"Atacaste al enemigo con bola de fuego haces {daño} de daño"
            return daño,msj
        elif self.mana < 20 and self.stamina < self.stamina:
            daño = 0
            msj = f"No tienes mana y stamina suficientes"
            return daño,msj        
        else:
            daño=0
            msj = f"No tienes el mana suficiente"
            return daño,msj
        
    #falta
    def proyectil_hielo(self):
        pass
   
   
    def __str__(self):
        return f"{self.mana},{self.stamina},{self.vida},{self.daño}"
        
    





