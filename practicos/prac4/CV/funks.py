def input_choice(opciones, msg='Elija una opción'):
    msg = f'{msg}: '
    opciones = opciones.split('/')
    op = 'not an option yet'
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

def input_str(msg, error='Longitud incorrecta', mini=0, maxi=float('inf')):
    msg = f'{msg}: '
    validado = False
    while not validado:
        s = input(msg)
        if mini <= len(s) <= maxi:
            validado = True
        else:
            print(error)
    return s

def input_alfa(msg, error='Longitud incorrecta', mini=0, maxi=float('inf')):
    validado = False
    while not validado:
            s = input_str(msg, error, mini, maxi)
            if s.isalpha():
                validado = True
            else:
                print('Debe ingresar una letra')
    return s

if __name__ == "__main__":
    #q = input_choice('si/no/a veces')
    #r = input_choice('rojo/verde', 'Elija un color')
    print(calcular_edad('30-06-1965'))