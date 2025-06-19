def codificar_mensaje(msg, *palabras_clave, mayusculas_resaltado=True, **sustituciones):
    print('-'*80)
    print(f'{msg=}')
    
    caracteres_msg = list(msg)
    palabras_originales = msg.split()

    print(f'{sustituciones=}')
    
    for i in range(len(caracteres_msg)):
        if caracteres_msg[i] in sustituciones:
            caracteres_msg[i] = sustituciones[caracteres_msg[i]]

    msg_modif = ''.join(caracteres_msg)
    palabras_modificadas = msg_modif.split()
    print(f'{palabras_originales=}')
    print(f'{palabras_modificadas=}')
    
    for palabra_clave in palabras_clave:
        for i in range(len(palabras_originales)):
            if palabra_clave == palabras_originales[i]:
                # restituyo las palabras clave originales con asteriscos o en mayúsculas
                palabras_modificadas[i] = palabras_originales[i].upper() if mayusculas_resaltado else f'*{palabras_originales[i]}*'

    print(' '.join(palabras_modificadas))

# Programa Principal
codificar_mensaje("el agente llega mañana al amanecer", "agente", "amanecer", mayusculas_resaltado=False, a="4", e="3", o="0")
codificar_mensaje("cuando venga mi primo tomaremos un whisky antes de la cena", "primo", "whisky", "cena", a="4", e="3", o="0", i='1', g='9')


# 3l *agente* ll3g4 m4ñ4n4 4l *amanecer*
# cu4nd0 v3n94 m1 PRIMO t0m4r3m0s un WHISKY 4nt3s d3 l4 CENA
