class Pelicula: 
    def __init__ (self,nombre: str, duracion: str, genero: str, anio_lanzamiento: str, descripcion: str, elenco: str)-> None:
        self.nombre = nombre
        self.duracion = duracion
        self._idiomas = ["Español","Ingles"]
        self.genero = genero
        self.anio_lanzamiento = anio_lanzamiento
        self.descripcion = descripcion
        self.elenco = elenco

    @property 
    def nombre(self): 
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if isinstance (nuevo_nombre, str):
            self._nombre = nuevo_nombre
        else:
            raise TypeError ("Debes ingresar un nombre de tipo string")
          
    @property
    def duracion(self): 
        return self._duracion 

    @duracion.setter 
    def duracion(self, nueva_duracion: str): 
        if isinstance(nueva_duracion,str): 
            self._duracion = nueva_duracion
        else:
            raise TypeError ("Debes ingresar la duracion de la pelicula con formato string")
            
    @property 
    def idiomas(self): 
        return self._idiomas

    @idiomas.setter
    def idioma(self, nuevo_idiooma: str): 
        if not isinstance (nuevo_idiooma, str):
            raise TypeError ("El idioma de la pelicula debe ser un valor tipo string")
        if nuevo_idiooma in self.idiomas:
            raise TypeError ("La pelicula ya esta en ese idioma") 
        self.idiomas.append(nuevo_idiooma)

    def listado_idioma(self):
        salida = ""
        for idioma in self.idiomas: 
            salida += idioma + " "
        return salida

    @property 
    def genero(self): 
        return self._genero

    @genero.setter
    def genero(self, nuevo_genero: str): 
        if isinstance (nuevo_genero, str):
            self._genero = nuevo_genero
        else: raise TypeError ("El genero de la pelicula debe ser un valor tipo string")
       

    @property
    def anio_lanzamiento(self): 
        return self._anio_lanzamiento

    @anio_lanzamiento.setter 
    def anio_lanzamiento(self, nuevo_anio_de_lanzamiento: str): 
        if isinstance(nuevo_anio_de_lanzamiento, str): 
            self._anio_lanzamiento = nuevo_anio_de_lanzamiento
        else:
            raise TypeError ("Debes ingresar el año de la pelicula en formato string")

    @property
    def descripcion (self): 
        return self._descripcion

    @descripcion.setter 
    def descripcion(self, nueva_descripcion: str): 
        if isinstance(nueva_descripcion, str): 
            self._descripcion = nueva_descripcion
        else:
            raise TypeError ("Debes ingresar la descripcion de la pelicula con formato strin")
           
    @property
    def elenco (self): 
        return self._elenco

    @elenco.setter 
    def elenco (self, nuevo_elenco: str): 
        if isinstance(nuevo_elenco,str): 
            self._elenco = nuevo_elenco
        else:
            raise TypeError ("Debes ingresar el elenco de la pelicula en formato string")
            
    def __str__(self): 
        return f" Nombre de la pelicula: {self.nombre} \n Duracion de la pelicula: {self.duracion} \n Idioma: {self.listado_idioma()} \n Genero de la pelicula: {self._genero} \n Año de lanzamineto: {self.anio_lanzamiento} \n descripcion: {self.descripcion} \n elenco: {self.elenco}"
