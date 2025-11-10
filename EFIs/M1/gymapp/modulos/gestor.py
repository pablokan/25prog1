#imports
from datetime import timedelta, date
from .persona import Alumno

#Calcular vencimientos
def obtener_fecha_vencimiento(alumno):
  return f'Fecha de vencimiento: {alumno.fecha_alta + timedelta(days=30)}'

#Cuando vence la cuota
def vencio_cuota(alumno):
  vencimiento = alumno.fecha_alta + timedelta(days=30)
  if date.today() > vencimiento:
    print(f"{alumno.nombre} su membresia vencio el: {vencimiento.strftime('%d/%m/%Y')}")
    return True
  else:
    print(f"{alumno.nombre} su membresia sigue vigente.")
  return False

#Funcion para renovar la cuota
def renovar_pago(alumno):
  alumno.fecha_alta = date.today()
  print(f"{alumno.nombre} renovo su cuota. Su nueva fecha de vencimiento es: {alumno.fecha_alta.strftime('%d/%m/%Y')}")