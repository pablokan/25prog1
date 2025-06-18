def codificar_mensaje(msg, *args, mayusculas_resaltado=True, **kwargs):
    lista_cars = list(msg)
    lista_pals = msg.split()
    for i in range(len(lista_cars)):
        if lista_cars[i] in kwargs:
            lista_cars[i] = kwargs[lista_cars[i]]
    qq = ''.join(lista_cars)
    lista_pals_modif = qq.split()
    for p in args:
        for i in range(len(lista_pals)):
            if p == lista_pals[i]:
                if mayusculas_resaltado:
                    lista_pals_modif[i] = lista_pals[i].upper()
                else:
                    lista_pals_modif[i] = f'*{lista_pals[i]}*'
    print(' '.join(lista_pals_modif))

codificar_mensaje("el agente llega mañana al amanecer", "agente", "amanecer", mayusculas_resaltado=False, a="4", e="3", o="0")
codificar_mensaje("cuando venga mi primo tomaremos un whisky antes de la cena", "primo", "whisky", "cena", a="4", e="3", o="0", i='1', g='9')


# 3l *agente* ll3g4 m4ñ4n4 4l *amanecer*
