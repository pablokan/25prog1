class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def obtener_estado(self):
        return 'aprobado' if self.nota >= 7.0 else 'reprobado'
    
def main():
    print(f'\n{'-'*35} inicio {'-'*35}\n')
    alumno = Estudiante('Juan', 9)
    print(f'El alumno {alumno.nombre} está {alumno.obtener_estado()}')
    print(f'\n{'-'*35} fin {'-'*35}\n')
        
if __name__ == '__main__':
    main()
