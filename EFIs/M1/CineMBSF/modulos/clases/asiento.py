class Asiento:
    def __init__(self, fila:str, numero:int)-> None: 
        self.fila = fila.upper()
        self.numero = numero 
        self.ocupado = False

    def reservar (self)-> bool: 
        if not self.ocupado:
            self.ocupado = True
            return True
        else: 
            return False

    def liberar (self)-> bool: 
        if self.ocupado:
            self.ocupado = False
            return True
        else: 
            return False

    @property
    def fila(self): 
        return self._fila 
    
    @fila.setter
    def fila(self, nuevafila:str):
        filas = "ABCDE"
        if isinstance(nuevafila,str) and len(nuevafila) == 1 and nuevafila in filas:
            self._fila = nuevafila
        else: 
            raise TypeError ("Debes ingresar una letra de la A-E y en formato string")    
        
    @property
    def numero(self): 
        return self._numero

    @numero.setter
    def numero(self, nuevonumero:int):  
        if isinstance(nuevonumero,int) and 1 <= int(nuevonumero) <= 10: 
            self._numero = nuevonumero
        else: 
            raise TypeError ("Debes ingresar un numero en formato int y dentro del rango del 1-10")
        
    def __str__(self):
        estado = ""
        if self.ocupado: 
            estado = "ocupado" 
        else: 
            estado = "disponible"

        return f"El asiento de la fila {self.fila} y numero {self.numero} esta {estado}"





