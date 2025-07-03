def codificar_mensaje(msg, *palabras_clave, mayusculas_resaltado=True, **sustituciones):
    msg_codificado = []
    palabras = msg.split(' ')

    for palabra in palabras:
        if palabra in palabras_clave:
            palabra_resaltada = palabra.upper() if mayusculas_resaltado else f'*{palabra}*'
            msg_codificado.append(palabra_resaltada)
        else:
            palabra_codificada = "".join(sustituciones.get(c, c) for c in palabra)
            msg_codificado.append(palabra_codificada)

    print(' '.join(msg_codificado))


codificar_mensaje(
    "el agente llega mañana al amanecer",
    "agente", "amanecer",
    mayusculas_resaltado=False,
    a="4", e="3", o="0"
)
codificar_mensaje(
    "cuando venga mi primo tomaremos un whisky antes de la cena",
    "primo", "whisky", "cena",
    a="4", e="3", o="0", i='1', g='9'
)
