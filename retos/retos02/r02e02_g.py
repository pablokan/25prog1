def codificar_mensaje(msg, *palabras_clave, mayusculas_resaltado=True, **sustituciones):
    set_palabras_clave = set(palabras_clave)
    palabras = msg.split(' ')
    palabras_codificadas = [
        (palabra.upper() if mayusculas_resaltado else f'*{palabra}*')
        if palabra in set_palabras_clave
        else "".join(sustituciones.get(c, c) for c in palabra)
        for palabra in palabras
    ]
    print(' '.join(palabras_codificadas))

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

