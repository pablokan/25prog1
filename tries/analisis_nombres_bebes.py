# -*- coding: utf-8 -*-

def procesar_datos_2008(nacidos_str):
    """
    Procesa la cadena de datos de 2008, separa por sexo y ordena por cantidad.
    Devuelve dos listas (masculinos, femeninos) de tuplas (nombre, cantidad).
    """
    items = nacidos_str.split(',')
    nombres_m = []
    nombres_f = []
    
    i = 0
    while i < len(items):
        nombre = items[i]
        cantidad = int(items[i+1])
        sexo = items[i+2]
        
        if sexo == 'm':
            nombres_m.append((nombre, cantidad))
        elif sexo == 'f':
            nombres_f.append((nombre, cantidad))
        i += 3
        
    # Ordenar por cantidad descendente (el segundo elemento de la tupla)
    nombres_m.sort(key=lambda x: x[1], reverse=True)
    nombres_f.sort(key=lambda x: x[1], reverse=True)
    
    return nombres_m, nombres_f

def comparar_rankings(datos_2008_m, datos_2008_f, datos_2018_m, datos_2018_f):
    """
    Compara los nombres por ranking y sexo entre 2008 y 2018.
    """
    print("--- Comparación de Rankings (2008 vs 2018) ---")
    
    ordinales = {1: "primero", 2: "segundo", 3: "tercero", 4: "cuarto", 5: "quinto"}

    # Comparación para nombres masculinos
    for i in range(min(len(datos_2008_m), len(datos_2018_m))):
        rank = i + 1
        nombre_2008, cant_2008 = datos_2008_m[i]
        # En datos_2018, el rank está en el primer elemento, nombre en el segundo, cantidad en el tercero
        rank_2018, nombre_2018, cant_2018 = datos_2018_m[i] 

        diff = cant_2008 - cant_2018
        
        # Replicar formatos de ejemplo si aplican
        if rank == 1 and diff > 0:
            print(f"Varones en posición #{rank}: {diff} nacimientos de varones más del {ordinales[rank]} del ranking de 2008 {nombre_2008} sobre {nombre_2018} del 2018")
        elif rank == 4 and diff > 0:
             print(f"Varones en posición #{rank}: {diff} a favor de {nombre_2008}(2008) sobre {nombre_2018}(2018)")
        else:
            if diff > 0:
                print(f"Varones en posición #{rank}: {nombre_2008} (2008) tuvo {diff} más nacimientos que {nombre_2018} (2018).")
            elif diff < 0:
                print(f"Varones en posición #{rank}: {nombre_2018} (2018) tuvo {-diff} más nacimientos que {nombre_2008} (2008).")
            else:
                print(f"Varones en posición #{rank}: {nombre_2008} (2008) y {nombre_2018} (2018) tuvieron la misma cantidad de nacimientos.")

    # Comparación para nombres femeninos
    for i in range(min(len(datos_2008_f), len(datos_2018_f))):
        rank = i + 1
        nombre_2008, cant_2008 = datos_2008_f[i]
        rank_2018, nombre_2018, cant_2018 = datos_2018_f[i]
        
        diff_abs = abs(cant_2008 - cant_2018)
        
        if rank == 2: # Formato específico para Femenino Posición #2
             print(f"Mujeres en posición #{rank}: {diff_abs} es la diferencia entre {nombre_2008} del 2008 sobre {nombre_2018} del 2018")
        else:
            diff = cant_2008 - cant_2018
            if diff > 0:
                print(f"Mujeres en posición #{rank}: {nombre_2008} (2008) tuvo {diff} más nacimientos que {nombre_2018} (2018).")
            elif diff < 0:
                print(f"Mujeres en posición #{rank}: {nombre_2018} (2018) tuvo {-diff} más nacimientos que {nombre_2008} (2008).")
            else:
                print(f"Mujeres en posición #{rank}: {nombre_2008} (2008) y {nombre_2018} (2018) tuvieron la misma cantidad de nacimientos.")


def nombres_por_letra(letra_inicial, nombres_2008_m, nombres_2008_f, nombres_2018_m, nombres_2018_f):
    """
    Encuentra y muestra nombres que comienzan con una letra dada de ambos periodos.
    """
    print(f"\n--- Nombres que comienzan con la letra '{letra_inicial.upper()}' ---")
    letra_inicial = letra_inicial.lower()
    nombres_encontrados = set()

    for nombre, _ in nombres_2008_m + nombres_2008_f:
        if nombre.lower().startswith(letra_inicial):
            nombres_encontrados.add(nombre)
            
    for _, nombre, _ in nombres_2018_m + nombres_2018_f:
        if nombre.lower().startswith(letra_inicial):
            nombres_encontrados.add(nombre)
            
    if nombres_encontrados:
        print(f"Nombres con {letra_inicial.upper()}: " + " ".join(sorted(list(nombres_encontrados))))
    else:
        print(f"No se encontraron nombres que comiencen con la letra '{letra_inicial.upper()}'.")

def nombres_repetidos(nombres_2008_m, nombres_2008_f, nombres_2018_m, nombres_2018_f):
    """
    Encuentra y muestra los nombres que se repiten en ambos años.
    """
    print("\n--- Nombres que se repiten en ambos años (2008 y 2018) ---")
    
    set_nombres_2008 = set()
    for nombre, _ in nombres_2008_m + nombres_2008_f:
        set_nombres_2008.add(nombre)
        
    set_nombres_2018 = set()
    for _, nombre, _ in nombres_2018_m + nombres_2018_f:
        set_nombres_2018.add(nombre)
        
    repetidos = sorted(list(set_nombres_2008.intersection(set_nombres_2018)))
    
    if repetidos:
        print("Nombres que se repiten: " + " ".join(repetidos))
    else:
        print("No hay nombres que se repitan en ambos años.")

# --- Datos ---
nacidos2008_str = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

# Datos 2018 (Rank, Male name, Number of males, Female name, Number of females)
# Almacenaremos como listas de tuplas: (Rank, Name, Count)
datos_2018_m_raw = [
    (1, "Liam", 19837),
    (2, "Noah", 18267),
    (3, "Michael", 14516),
    (4, "James", 13525),
    (5, "Oliver", 13389)
]

datos_2018_f_raw = [
    (1, "Emma", 18688),
    (2, "Olivia", 17921),
    (3, "Ava", 14924),
    (4, "Isabella", 14464),
    (5, "Sophia", 13928)
]

# --- Procesamiento ---
nombres_2008_m_top, nombres_2008_f_top = procesar_datos_2008(nacidos2008_str)

# Asegurarnos de que solo tomamos el top 5 para la comparación, si hay más
nombres_2008_m_top5 = nombres_2008_m_top[:5]
nombres_2008_f_top5 = nombres_2008_f_top[:5]


# --- Salidas ---
# 1. Diferencia en cantidad de bebés por misma posición y sexo
comparar_rankings(nombres_2008_m_top5, nombres_2008_f_top5, datos_2018_m_raw, datos_2018_f_raw)

# 2. Nombres que comienzan con una letra (solicitar al usuario)
letra = input("\nIngrese la letra inicial para buscar nombres: ")
nombres_por_letra(letra, nombres_2008_m_top, nombres_2008_f_top, datos_2018_m_raw, datos_2018_f_raw) # Usar todos los nombres de 2008 para esta búsqueda

# 3. Nombres que se repiten
nombres_repetidos(nombres_2008_m_top, nombres_2008_f_top, datos_2018_m_raw, datos_2018_f_raw) # Usar todos los nombres de 2008

print("\nAnálisis completado.")