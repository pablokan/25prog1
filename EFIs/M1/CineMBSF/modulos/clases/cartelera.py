from .pelicula import Pelicula
class Cartelera: 
    def __init__(self)-> None:
        self.peliculas: list[Pelicula] = []
        self.horarios: list[str] = [] 

    def agregar_pelicula(self, pelicula: Pelicula): 
        if isinstance (pelicula, Pelicula):
            self.peliculas.append(pelicula)
        else: 
            print("Debe ingresar una instancia de la clase Película.")   

    def agregar_horario(self, horario: str):
        if isinstance (horario,str):
            self.horarios.append(horario) 

        else: 
            print("Ingrese el horario de la pelicula en formato string.")   
        
    def mostrar_cartelera(self):
        salida = ''
        for x in range(len(self.peliculas)):
            salida += f'Película: {self.peliculas[x].nombre} \nHorario: {self.horarios[x]}\n'
        return salida
            