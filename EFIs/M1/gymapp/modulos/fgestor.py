from .persona import *
import datetime
from datetime import date

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
       return f"El alumno tiene la cuota vencida {fecha_vencimiento}"
    else:
       dias = (fecha_vencimiento - hoy).days
       return f"El alumno esta al dia. Faltan {dias} dias para el vencimiento" 


# alumno1 = Alumno('Luis', 'Fernandez', 27820016, date(2000,1,10))
##SETTER


# print(f"Su registro se vence el:", vencimiento(alumno1))
# print(f"ALERTA DE VENCIMIENTO:", alerta(alumno1))
