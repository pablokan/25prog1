# parametrización

# posicionales obligatorios
"""
def suma(n1, n2):
    return n1 + n2
    
print(suma(2, 3))

def saluda(nombre, edad):
    if edad >= 18:
        mensaje = 'es mayor de edad'
    else:
        mensaje = 'es menor de edad'
    print(f'Hola {nombre}, veo que sos {mensaje}')
    
saluda('Ana', 66)
saluda('Pepito', 11)
"""

# posicionales opcionales
def suma(*args):
    total = 0
    for n in args:
        total += n
    return total    

print(suma(2, 3, 4))
print(suma())

""" 
# parámetros con valores por defecto
def alumno(nombre, localidad='Río Cuarto'):
    print(f'El alumno {nombre} es de {localidad}')
    
alumno('Juan', 'Las Higueras')
alumno('Ema')
 """

