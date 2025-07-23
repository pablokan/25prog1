class Base:
    def __init__(self):
        self.__data = "Datos de la clase base" # Nombre mangled a _Base__data

class SubClase(Base):
    def __init__(self):
        super().__init__()
        self.__data = "Datos de la subclase" # Nombre mangled a _SubClase__data

    def get_data(self):
        return self._Base__data
s = SubClase()

# Si __data no hiciera mangling, SubClase.__data sobrescribiría Base.__data
# Pero gracias al mangling, son variables distintas:
print(s._Base__data) 
print(s._SubClase__data)
