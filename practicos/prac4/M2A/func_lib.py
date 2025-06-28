def input_choice(opciones, msg='Elija una opción'):
    msg = f'{msg}: '
    opciones = opciones.split('/')
    op = ''
    while op not in opciones:
        op = input(f'{opciones} {msg}')
    return op

def calcular_edad(fecha_nacimiento):
    from datetime import date
    hoy = date.today()
    dia_nac, mes_nac, anio_nac = [int(n) for n in fecha_nacimiento.split('-')]
    edad = hoy.year - anio_nac
    if (mes_nac > hoy.month) or (mes_nac == hoy.month and dia_nac > hoy.day):
        edad -= 1
    return edad

if __name__ == "__main__":
    q = input_choice('si/no/a veces') # ['si', 'no', 'a veces']
    r = input_choice('rojo/verde', 'Elija un color')
