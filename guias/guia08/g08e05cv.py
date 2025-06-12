
from g08e04cv import input_str

def input_user(msg):
    #letras = [chr(i) for i in range(97, 123)] 
    #digitos = [str(d) for d in range(10)]
    especiales = '#$%&'
    validado = False
    while not validado:
        val_letras = False
        val_digitos = False
        val_especiales = False
        usuario = input_str(msg, 8)
        usuario = usuario.lower()
        for car in usuario:
            #if car in letras:
            if car.isalpha():
                val_letras = True
            # elif car in digitos
            elif car.isdigit():
                val_digitos = True
            elif car in especiales:
                val_especiales = True
        if val_letras and val_digitos and val_especiales:
            validado = True

usuario = input_user('Ingrese un nombre de usuario válido (debe contener como mínimo una letra, un dígito y al menos uno de estos caracteres especiales:  #, $, %,&): ')
# 1$1$1$1$1$1 # wrong - no tiene una letra
# abc%abc% # wrong - no tiene un dígito
# abc#123 # wrong - no llega a 8 caracteres
# quic0*grosso # wrong - el * es especial pero no es uno de los 4 requeridos
# qwerty9& # yes!
