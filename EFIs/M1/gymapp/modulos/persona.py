#Imports
from datetime import date, datetime


class Persona:
    def __init__(self, nombre:str, apellido:str, dni:int ):
        self.valida = True
        self.nombre = nombre 
        self.apellido = apellido 
        self.dni = dni 

#---------------------------------------- geter y seter 
    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def dni(self):
        return self._dni

    @nombre.setter 
    def nombre(self, valor):
        texto = str(valor).strip()

        if len(texto) == 0:
            self.valida = False
            self._nombre = None     

        else: 
            self._nombre = texto  

    @apellido.setter 
    def apellido(self,valor):
        texto = str(valor).strip()
        if len(texto) == 0:
            self.valida = False
            self._apellido = None
        else:
            self._apellido = texto


    @dni.setter
    def dni(self, valor):
        dni_str = str(valor).strip()
        if dni_str.isdigit() and int(dni_str) > 0:
            self._dni = int(dni_str)
        else:
            self.valida = False
            self._dni = None



    def __str__(self): 
        return f"Nombre: {self._nombre}, Apellido: {self._apellido}, Dni: {self._dni}"

class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, fecha_alta, activo : bool = True):
        super().__init__(nombre, apellido, dni)
        self.fecha_alta = fecha_alta
        self.activo = activo

    #Getter y Setter
    @property
    def fecha_alta(self):
        return self._fecha_alta

    @property
    def activo(self):
        return self._activo

    @fecha_alta.setter
    def fecha_alta(self, nueva_fecha_alta):
        #validacion de tipo
        if not isinstance(nueva_fecha_alta, date):
            raise TypeError(f'Debe ser una fecha valida.')

        self._fecha_alta = nueva_fecha_alta

    @activo.setter
    def activo(self, valor):
        if not isinstance(valor, bool):
            raise TypeError("El valor debe ser booleano: True o False.")
        self._activo = valor


#Repr para ver codigo 
    def __repr__(self):

        return   f"Nombre: {self.nombre}, Apellido: {self.apellido}, Dni: {self.dni}, Fecha_alta: {self.fecha_alta}, Activo: {self.activo}"

#Metodos de clase para convertir a objeto
    @classmethod
    def from_line(cls, linea):
        linea = linea.strip()
        if not linea:  # si la línea está vacía, no hacer nada
            return None
        partes = linea.split(";")
        if len(partes) < 4:  # si la linea esta incompleta no devolvemos nada
            return None
        dni, nombre, apellido, fecha_str = partes[:4]    
        fecha_alta = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        return cls(nombre, apellido, int(dni), fecha_alta, activo=True)



class Profesor(Persona):
    def __init__(self, nombre, apellido, dni, especialidad , fecha_alta : bool = True , pago_realizado : bool = False ):
        super().__init__(nombre, apellido, dni)

        self._fecha_alta = fecha_alta
        self._especialidad = especialidad
#Repr para ver codigo 
    def __repr__(self):
     
        return   f"Nombre: {self.nombre}, Apellido: {self.apellido}, Dni: {self.dni}, Especialidad: {self.especialidad} "





# alumno1 = Alumno('Jorge','Lopez', 12345678, date(2025,9,10), True)
# profesor1 = Profesor("Ana", "Gomez", 87654321, "Musculación")


# Prints para probar
# print(alumno1)
# print(profesor1)
