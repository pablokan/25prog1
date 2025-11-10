#imports
from datetime import date, datetime
from .persona import Alumno #necesito la clase alumno



def cargar_txt(nombre_archivo="alumnnos.txt"):
    alumnos = []
    try:
        with open(nombre_archivo, 'r', encoding="utf-8") as file:
            next(file) # saltamos aca el encabezado
            for linea in file:
                alumno = Alumno.from_line(linea)
                if alumnos is not None:
                    alumnos.append(Alumno)
    except FileNotFoundError:
        print("No se encontro el archivo solicitado. Se creara en su lugar.")
    return alumnos

def cargar_alumno(lista_total):
    #Carga de datos
    dni_str = (input('DNI: '))
    if not dni_str.isdigit() or len(dni_str) > 8:
        print(f"ERROR: DNI invalido. Debe tener hasta 8 digitos numericos.")
        return None
    dni =int(dni_str)
    
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    fecha_str = input('Fecha de alta(Formato DD/MM/AAAA):  ')
    
    #Validacion duplicado
    for alumno in lista_total:
        if alumno.dni == dni:
            print(f"ERROR: Ya existe un alumno con DNI {dni}: {alumno.nombre} {alumno.apellido}")
            return None

    try:
        fecha_alta = datetime.strptime(fecha_str, '%d/%m/%Y').date()
    except ValueError:
        print("Fecha inválida. Se usará la fecha de hoy.")
        fecha_alta = datetime.today().date()

    alumno = Alumno(nombre, apellido, dni, fecha_alta, activo = True)
    print(f"Alumno {alumno.nombre}, {alumno.apellido} cargado correctamente.")
    return alumno

#Cargar alumno a TXT
def guardar_alumno_txt(alumno, archivo="alumnos.txt"):
    with open(archivo, "a", encoding="utf-8") as file:
        file.write(f"{alumno.dni};{alumno.nombre};{alumno.apellido};{alumno.fecha_alta.strftime('%Y-%m-%d')};{alumno.activo}\n")
    print(f"Alumno {alumno.nombre} guardado en archivo.")
    