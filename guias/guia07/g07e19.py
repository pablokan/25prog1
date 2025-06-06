def recu(cadena):
    esi, eii, esd, eid, hor, ver = '╔', '╚', '╗', '╝', '═', '║'
    print(esi, end='')
    print(hor * (len(cadena)+2), end='')
    print(esd)
    print(ver, end='')
    print(' '+ cadena + ' ', end='')
    print(ver)
    print(eii, end='')
    print(hor * (len(cadena)+2), end='')
    print(eid)

recu('pablokan')
recu('La única verdad es la realidad')