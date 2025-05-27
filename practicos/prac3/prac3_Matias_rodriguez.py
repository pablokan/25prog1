# Lista de nombres y cantidades de nacimientos en 2008
datos2008 = [
    ("Eva", 17039, "f"), ("Daniel", 19005, "m"),
    ("Emily", 17434, "f"), ("Emma", 18813, "f"),
    ("Ethan", 20216, "m"), ("Julia", 18616, "f"),
    ("Jacob", 22594, "m"), ("Joshua", 19205, "m"),
    ("Michael", 20626, "m"), ("Olivia", 17081, "f")
]

# Lista de nombres y cantidades de nacimientos en 2018
datos2018 = [
    ("Liam", 19837, "m"), ("Emma", 18688, "f"),
    ("Noah", 18267, "m"), ("Olivia", 17921, "f"),
    ("Michael", 14516, "m"), ("Ava", 14924, "f"),
    ("James", 13525, "m"), ("Isabella", 14464, "f"),
    ("Oliver", 13389, "m"), ("Sophia", 13928, "f")
]

# 1. Comparar nacimientos entre 2008 y 2018
for i in range(5):  # Solo las primeras 5 posiciones
    nombre2008, cant2008, sexo2008 = datos2008[i]
    nombre2018, cant2018, sexo2018 = datos2018[i]

    if sexo2008 == sexo2018:  # Si son del mismo género
        diferencia = cant2008 - cant2018
        if diferencia > 0:
            print(f"{sexo2008.upper()} en puesto {i+1}: {nombre2008} tuvo {diferencia} nacimientos más en 2008 que {nombre2018} en 2018.")
        else:
            print(f"{sexo2008.upper()} en puesto {i+1}: {nombre2018} tuvo {-diferencia} nacimientos más en 2018 que {nombre2008} en 2008.")

# 2. Buscar nombres por letra inicial
letra = input("Introduce una letra inicial: ").capitalize()
nombres_por_letra = {nombre for nombre, _, _ in datos2008 if nombre.startswith(letra)} | {nombre for nombre, _, _ in datos2018 if nombre.startswith(letra)}

if nombres_por_letra:
    print(f"Nombres que comienzan con {letra}: {', '.join(sorted(nombres_por_letra))}")
else:
    print(f"No hay nombres que empiecen con {letra}.")

# 3. Encontrar nombres repetidos en ambos años
nombres_2008 = {nombre for nombre, _, _ in datos2008}
nombres_2018 = {nombre for nombre, _, _ in datos2018}

nombres_repetidos = nombres_2008 & nombres_2018
if nombres_repetidos:
    print(f"Nombres repetidos en ambos años: {', '.join(sorted(nombres_repetidos))}")
else:
    print("No hay nombres que se repitan entre ambos años.")
