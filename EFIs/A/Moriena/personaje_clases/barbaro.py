from .personajes import ClasesPersonaje
from creacion_objetos.creacion_inventario import inventario_inicial_barbaro

class Barbaro(ClasesPersonaje):
    
    #estadisticas de pruba 
    vida_base = 200
    stamina_base = 100
    daño_base = 20
    nivel_base = 1
    exp_obtenida = 0
    exp_subir_nivel = 100
    furia_base = 0
    furia_max = 100
    furia_necesaria_berserker = 50
    inv_inicial = inventario_inicial_barbaro


    def __init__(self,nombre):
        super().__init__(nombre,
                         vida_base = self.vida_base, 
                         stamina_base = self.stamina_base, 
                         daño_base = self.daño_base, 
                         nivel = self.nivel_base, 
                         exp_personaje = self.exp_obtenida, 
                         exp_subir_nivel = self.exp_subir_nivel,
                         inventario = self.inv_inicial)
        
        self.furia = self.furia_base
        self.berserker = False
       
        
    #---------------Getters y Setters---------------#
    
    #furia
    @property
    def furia(self):
        return self._furia
    
    @furia.setter
    def furia(self,furia:int):
        if isinstance(furia,(int,float)):
            furia = int(furia)
            if furia < 0 :
                self._furia = 0
            elif furia > self.furia_max:
                self._furia = self.furia_max
            else:
                self._furia = furia
        else:
            raise ValueError("Formato de furia invalido")
        
    #berserker
    @property
    def berserker(self):
        return self._berserker
    
    @berserker.setter
    def berserker(self,estado:bool):
        if isinstance(estado,bool):
            self._berserker = estado
        else:
            raise ValueError("Solo booleanos TRUE/FALSE")


    
    #---------------Metodos---------------#

    #Cambiar mensajes que devuelven los metodos
    
    def activar_berserker(self):
        if self.furia >= self.furia_necesaria_berserker and self.berserker == False: 
            self.berserker = True
            return f"Haz activado el modo 'Berserker'"
        if self.berserker == True:
            return f"Ya estas en modo 'BERSERKER'"
        else:
            return f"No tienes la furia suficiente necesitas {self.furia_necesaria_berserker - self.furia} de furia"
    

    #Por ahora el metodo se queda como esta en codigo(para probar como funciona) -> luego va a recibir como parametro clase enemigo don de se aplicara daño etc...
    
    def atacar(self):
        if self.berserker == True:
            porcentaje_aumento_daño = 1.5
            daño= int(self.daño*porcentaje_aumento_daño)
            self.vida -= 10
            self.furia -= 10
            if self.furia <= 0 :
                self.berserker = False
                msj=f"{self.nombre} en estado BERSERKER hace {daño} al enemigo pero BERSERKER se desactiva."
                return daño,msj
            msj = f"{self.nombre} en estado BERSERKER hace {daño} daño  al enemigo"
            return daño,msj
        elif self.stamina < 0:
            return 0,f"No tienes suficiente stamina para realizar el ataque"
        else:
            daño = self.daño
            self.stamina -= 15
            self.furia += 15
            msj = f"{self.nombre} ataca al enemigo hace {daño} de daño"
            return daño,msj

    def __str__(self):
        return f"vida:{self.vida},stamina:{self.stamina},daño:{self.daño},furia:{self.furia},nivel:{self.nivel},exp_personaje:{self.exp_obtenida}"
    

    