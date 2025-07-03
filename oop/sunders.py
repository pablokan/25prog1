class A:
    def __init__(self) -> None:
        self._uno = 1
        self.__dos = 2
        self.tres = 3

        @property
        def uno(self):
            return self._uno
        
        @property
        def tres(self):
            return self.tres
        

a = A()
print(a._uno)  # Acceso a atributo protegido
#print(A.__dos)  # Esto causará un error porque __dos es privado
print(a._A__dos)  # Acceso al atributo privado usando el nombre mangled

#print(a.uno)  # Acceso a través del método de propiedad
print(a.tres)  # Acceso al atributo público
