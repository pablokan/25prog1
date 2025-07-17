# escribe una clase Persona que reciba una edad, que use dataclasses y luego instancia un objeto y muestra el uso
from dataclasses import dataclass

@dataclass
class Persona:
    edad: int

    def __post_init__(self):
        if self.edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        
    def doble(self):
        return self.edad * 2

persona = Persona(25)
print(persona.edad)
print(persona.doble())



