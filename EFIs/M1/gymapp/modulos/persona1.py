from datetime import date
class Personaa:
    def __init__(self,nombre:str,apellido:str,dni:int):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni


    #Encapsulamiento

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def dni(self):
        return self._dni

    #Setters

    @nombre.setter
    def nombre(self,nuevo_nombre):
        if not isinstance(nuevo_nombre, str):
            raise ValueError(f'Debe ingresar solo texto.')

        self._nombre = nuevo_nombre

    @apellido.setter
    def apellido(self, nuevo_apellido):
        if not isinstance(nuevo_apellido, str):
            raise ValueError(f'Debe ingresar solo texto.')

        self._apellido = nuevo_apellido

    @dni.setter
    def dni(self, nuevo_dni):
        if not isinstance(nuevo_dni, int):
            raise TypeError(f'Debe ingresar solo numeros.')

        self._dni = nuevo_dni


    #Dunders
    def __str__(self):
        return f'Nombre: {self._nombre}, {self._apellido}, DNI: {self._dni}'

class Alumno(Personaa):
    def __init__(self, nombre, apellido, dni, fecha_alta):
        super().__init__(nombre,apellido,dni)
        self.fecha_alta = fecha_alta

    #Encapsulamiento
    
    @property
    def fecha_alta(self):
        return self._fecha_alta

    @fecha_alta.setter
    def fecha_alta(self, nueva_fecha_alta):
        #validacion de tipo
        if not isinstance(nueva_fecha_alta, date):
            raise TypeError(f'Debe ser una fecha valida.')

        self._fecha_alta = nueva_fecha_alta

    #dunder
    def __str__(self):
        fecha_formateada = self._fecha_alta.strftime('%d/%m/%Y')
        return f'Alumno: {self._nombre}, {self._apellido}. DNI: {self._dni}. Fecha Alta: {fecha_formateada}'


class Profesor(Personaa):
    def __init__(self,nombre,apellido,dni,especializacion):
        super().__init__(nombre,apellido,dni)
        self.especializacion = especializacion

    #Encapsulamiento Getter y Setter

    @property
    def especializacion(self):
        return self._especializacion

    @especializacion.setter
    def especializacion(self,nueva_especializacion):
        if not isinstance(nueva_especializacion, str):
            raise TypeError(f'Debe ingresar texto.')

        self._especializacion = nueva_especializacion

    #Dunder
    def __str__(self):
        return f'Nombre: {self._nombre}, {self._apellido}. DNI: {self._dni}, Especializado en: {self._especializacion}'

    
#info


persona1 = Personaa('Jorge', 'Fernandez', 95888458)
alumno1 = Alumno('Luis', 'Fernandez', 27820016, date(2000,1,10))
#profesor1 = Profesor('Jacobo', 'Zunino', 45132321, 'Musculacion')
# # print(persona1)
print(alumno1)
# # print(profesor1)