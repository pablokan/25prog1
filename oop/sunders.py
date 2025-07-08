class A:
    def __init__(self) -> None:
        self._uno = 1
        self.__dos = 2
        self.tres = 3
        self.__cuatro = 4

        @property
        def cuatro(self):
            return self.__cuatro
        
        @property
        def tres(self):
            return self.tres
        

a = A()
#print(f'# {a._uno=} #')  # Acceso a atributo protegido
#print(A.__dos)  # Esto causará un error porque __dos es privado
print(f'# {a._A__dos=} #')  # Acceso al atributo privado usando el nombre mangled
print(f'# {a.cuatro=} #')  # Acceso a través del método de propiedad
print(f'# {a.tres=} #')  # Acceso al atributo público
