def inputStr(msg='Ingrese el dato', mini=0, maxi=100000):
    s = ''
    len_s = -1
    while not (mini <= len_s <= maxi):
        s = input(f'{msg}: ')
        len_s = len(s)
    return s

if __name__ == "__main__":
    password0 = inputStr('Password (entre 5 y 8 caracteres): ', 5, 8)
    password1 = inputStr('Password (al menos 4): ', 4)
    password2 = inputStr('Password (a lo sumo 5): ', maxi=5)
    password3 = inputStr('Password (sin rango): ')
