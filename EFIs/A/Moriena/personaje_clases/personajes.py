from inventario.inventario_j import Inventario
from items.clase_equipamiento import Equipamiento,Casco,Pechera,Arma


class ClasesPersonaje:
   
    def __init__(self,nombre:str,vida_base:int,stamina_base:int,daño_base:int,nivel:int,exp_personaje:int,exp_subir_nivel:int,inventario:object):
        self.nombre = nombre
        
        #Falta terminar
        #estadisticas bases de personaje,se calculan segun la clase particular
        self._vida_base = vida_base
        self._stamina_base = stamina_base
        self._daño_base = daño_base
        #estadisticas tope para cada personaje
        self._vida_max = vida_base
        self._stamina_max = stamina_base
        self._daño_max = daño_base
        #estadisticas bases de personaje,se calculan segun la clase particular
        self.vida = vida_base
        self.stamina = stamina_base
        self.daño = daño_base

        #otros
        self.nivel = nivel
        self.exp_personaje = exp_personaje
        self.exp_subir_nivel = exp_subir_nivel
        self.inventario:Inventario = inventario
        self._equipamiento_activo = {"Casco":None,"Pechera":None,"Arma":None}#"Tener en cuenta que es se puede extender"
        

    #---------------Getters y Setters---------------#
    
    #Nombre
    @property

    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre_jugador:str):
        if isinstance(nombre_jugador,str):
            nombre_jugador=str(nombre_jugador)
            self._nombre = nombre_jugador
        else:
            raise ValueError("Formato de Nombre invalido")

    #--------------------vida,stamina,daño bases-------------------#

    @property
    def vida_base(self):
        return self._vida_base
    
    @property
    def stamina_base(self):
        return self._stamina_base
    
    @property
    def daño_base(self):
        return self._daño_base

    #-------------------vida,stamina max-----------------------#
    @property
    def vida_max(self):
        return self._vida_max
    
    @property
    def stamina_max(self):
        return self._stamina_max
    
    @property
    def daño_max(self):
        return self._daño_max

    #Vida
    @property

    #-----------------vida,stamina,daño------------------------#
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self,vida:int):
        if isinstance(vida,(int,float)):
            if vida < 0:
               self._vida = 0
            elif vida > self.vida_max:
                self._vida = self.vida_max
            else:
                self._vida = vida
        else:
            raise ValueError("Formato de vida invalido")

    #Stamina
    @property

    def stamina(self):
        return self._stamina
    
    @stamina.setter
    def stamina(self,stamina:int):
        if isinstance(stamina,(int,float)):
            stamina=int(stamina)
            if stamina < 0:
                self._stamina = 0
            
            elif stamina > self.stamina_max:
                self._stamina = self.stamina_max
            
            else:
                self._stamina = stamina        
        else:
             raise ValueError("Formato de stamina Invalido")

    #Daño
    @property

    def daño(self):
        return self._daño
    
    @daño.setter
    def daño(self,daño:int):
        if isinstance(daño,(int,float)):
            daño = int(daño)
            if daño > 0 :
                self._daño = daño
            elif daño <= 0:
                self._daño = 0
        else:
            raise ValueError("Formato de daño invalido")

    #Nivel
    @property

    def nivel(self):
        return self._nivel
    
    @nivel.setter
    def nivel(self,nivel:int):
        if isinstance(nivel,int):
            if nivel >= 0 :
                self._nivel = nivel
            elif nivel < 0 :
                self._nivel = 0
        else:
            raise ValueError("Formato de nivel invalido")

    #Exp_personaje
    @property
    def exp_personaje(self):
        return self._exp_personaje
    
    @exp_personaje.setter
    def exp_personaje(self,exp:int):
        if isinstance(exp,(int,float)):
            exp = int(exp)
            if exp >= 0 :
                self._exp_personaje = exp
            elif exp <= 0 :
                self._exp_personaje = 0
        else:
            raise ValueError("Formato de experiencia ganada invalida")

    #Exp_subir_nivel
    @property
    def exp_subir_nivel(self):
        return self._exp_subir_nivel
    
    @exp_subir_nivel.setter
    def exp_subir_nivel(self,exp_requerida:int):
        if isinstance(exp_requerida,(int,float)):
            exp_requerida = int(exp_requerida)
            if exp_requerida >= 0:
                self._exp_subir_nivel = exp_requerida
            elif exp_requerida < 0:
                self._exp_requerida = 0
        else:
            raise ValueError("Formato de experiencia para subir de nivel invalida")
        

    @property
    def inventario(self):
        return self._inventario 
    
    @inventario.setter
    def inventario(self,inventario):
        if isinstance(inventario,Inventario):
            self._inventario = inventario
        else:
            raise ValueError("Formato de inventario invalido tiene que ser objeto 'Inventario' ")
        
            

   
    #---------------Metodos---------------#
    
    def esta_vivo(self):
        if self.vida > 0:
            return True
        else:
            return False     
    
    def sumar_exp(self,cantidad:int):
        self.exp_personaje += cantidad
        self.subir_nivel()

   
    def cambiar_items_activos(self,opcion):
            try:
                item:Equipamiento = self.inventario.lista_equipamiento[opcion]
                tipo_item = item.tipo
                if self._equipamiento_activo[tipo_item] == None:
                    self._equipamiento_activo[tipo_item] = item
                    self.inventario.sacar_objeto(item)
                    return ( f"Has equipado el Item {item}" )
                else:
                    item_anterior = self._equipamiento_activo[tipo_item]
                    self._equipamiento_activo[tipo_item] = item
                    self.inventario.sacar_objeto(item)
                    self.inventario.guardar_objeto(item_anterior)
                    return ( f"Haz reemplazado el item {item_anterior} por {item}" )
            except:
                raise ValueError("Indice fuera de rango")
    
    def calcular_estadisticas(self):#falta terminar
        
        self._stamina_max = self.stamina_base
        self._vida_max = self.vida_base
        self._daño_max = self.daño_base
        
        for item in self._equipamiento_activo.values():
           if item != None:
            for k,v in item.estadisticas.items():
                if k == "vida":
                    self._vida_max += v
                elif k == "stamina":
                    self._stamina_max += v
                elif k == "daño":
                    self._daño_max += v

        self.stamina = self._stamina_max
        self.vida = self._vida_max
        self.daño = self._daño_max


    
    def subir_nivel(self):#cada clase puede escalar de manera diferente al subir de nivel
        pass
    

    def atacar(self,enemigo:object):#Cada clase define el metodo
        pass
        
   
    






   

    

    
    

    


    

    







