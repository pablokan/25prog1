from modulos.alumno import *
from datetime import datetime, date

ruta_archivo = "alumnos.txt"

#Guardamos alumnos
def guardar_alumnos(alumnos):
   with open(ruta_archivo, "w", encoding="utf-8") as file:
      for a in alumnos:
         linea = f"{a.nombre};{a.apellido};{a.dni};{a.fecha_alta.isoformat()};{a.activo}\n"
         file.write(linea)

def cargar_alumnos():
   alumnos = []
   try: 
      with open(ruta_archivo, "r", encoding="utf-8") as f:
         for linea in f:
            nombre, apellido, dni, fecha_str, activo_str = linea.strip().split(";")
            fecha_alta = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            activo = activo_str == "True"
            alumno = Alumno(nombre, apellido, dni, fecha_alta, activo)
            alumnos.append(alumno)
   except FileNotFoundError:
      print("Archivos de alumnos no encontrado. Se creara uno en su defecto.")
   return alumnos

def inscribir_alumno_en_actividad(alumnos, actividades):
    # Mostramos alumnos
        print("\n--- Alumnos disponibles ---")
        for i, a in enumerate(alumnos, 1):
            print(f"{i}. {a.nombre} {a.apellido} - DNI: {a.dni}")

        idx_alumno = int(input("Seleccione el número del alumno: ")) - 1
        alumno = alumnos[idx_alumno]

        # Mostramos actividades
        print("\n--- Actividades disponibles ---")
        for i, act in enumerate(actividades, 1):
            print(f"{i}. {act.nombre}")

        idx_actividad = int(input("Seleccione la actividad: ")) - 1
        actividad = actividades[idx_actividad]

        # Inscribimos usando tu método
        actividad.inscribir_alumno(alumno)


def valores_cuota(dia_actividad, precioxdia):
    if dia_actividad == 3:
       mensual = (precioxdia*3)*4
    elif dia_actividad == 5:
       mensual = (precioxdia*5)*4
    else:
       raise ValueError ("LA OPCIONES SON 3 0 5 DIAS")
    return mensual 
    
def vencimiento(alumno):
   if not isinstance(alumno, Alumno):
         raise TypeError(f'Se necesita un Alumno')
   vencimiento = alumno.fecha_alta + datetime.timedelta(days=30)
   return vencimiento

def alerta(alumno):
    hoy = datetime.date.today()
    fecha_vencimiento = vencimiento(alumno)

    if hoy >= fecha_vencimiento:
         alumno.activo = False
         return(f"El alumno tiene la cuota vencida {fecha_vencimiento} y sera dado de baja.")
    else:
         dias = (fecha_vencimiento - hoy).days
         if dias <= 10:
            return f" FALTAN {dias} DIAS PARA EL VENCIMIENTO" 
