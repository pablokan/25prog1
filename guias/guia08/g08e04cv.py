def input_str(msg, mini=0, maxi=100000000000):
    texto = ''
    len_texto = -1
    while not (mini <= len_texto <= maxi):
        if len_texto >= 0:
            print(f'La longitud es {len_texto} y se pedía entre {mini} y {maxi}')
        texto = input(msg)
        len_texto = len(texto)
    return texto    


# password0 = input_str('Password (entre 5 y 8 caracteres): ', 5, 8)
# password1 = input_str('Password (al menos 4): ', 4)
# password2 = input_str('Password (a lo sumo 5): ', maxi=5)
# password3 = input_str('Password (sin rango): ')
