class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def obtener_estado(self):
        if self.nota >= 7.0:
            estado = 'Aprobado'
        else:
            estado = 'Reprobado'
        return estado
    
def main():
    print(f'\n{'-'*80}')
    alumno = Estudiante('Juan', 9)
    print(f'El alumno {alumno.nombre} está {alumno.obtener_estado()}')
    print(f'{'-'*80}\n')

if __name__ == '__main__':
    main()
