# Datos de nacimientos 2008 (como string según requisitos)
nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

# Datos de nacimientos 2018 organizados por ranking
datos2018 = {
    1: {"m": {"nombre": "Liam", "cantidad": 19837}, "f": {"nombre": "Emma", "cantidad": 18688}},
    2: {"m": {"nombre": "Noah", "cantidad": 18267}, "f": {"nombre": "Olivia", "cantidad": 17921}},
    3: {"m": {"nombre": "Michael", "cantidad": 14516}, "f": {"nombre": "Ava", "cantidad": 14924}},
    4: {"m": {"nombre": "James", "cantidad": 13525}, "f": {"nombre": "Isabella", "cantidad": 14464}},
    5: {"m": {"nombre": "Oliver", "cantidad": 13389}, "f": {"nombre": "Sophia", "cantidad": 13928}}
}

# Procesar datos de 2008
def procesar_datos_2008(cadena):
    elementos = cadena.split(",")
    nombres_2008 = {"m": {}, "f": {}}
    todos_nombres_2008 = []
    
    # Procesar elementos de 3 en 3 (nombre, cantidad, sexo)
    for i in range(0, len(elementos), 3):
        nombre = elementos[i]
        cantidad = int(elementos[i+1])
        sexo = elementos[i+2]
        
        nombres_2008[sexo][nombre] = cantidad
        todos_nombres_2008.append(nombre)
    
    return nombres_2008, todos_nombres_2008

# Crear ranking ordenado de 2008
def crear_ranking_2008(nombres_2008):
    ranking_2008 = {}
    
    # Separar por sexo y ordenar por cantidad (descendente)
    for sexo in ["m", "f"]:
        lista_ordenada = sorted(nombres_2008[sexo].items(), key=lambda x: x[1], reverse=True)
        for posicion, (nombre, cantidad) in enumerate(lista_ordenada, 1):
            if posicion not in ranking_2008:
                ranking_2008[posicion] = {}
            ranking_2008[posicion][sexo] = {"nombre": nombre, "cantidad": cantidad}
    
    return ranking_2008

# Procesar datos
nombres_2008, todos_nombres_2008 = procesar_datos_2008(nacidos2008)
ranking_2008 = crear_ranking_2008(nombres_2008)

# Función 1: Diferencia entre nombres de misma posición y sexo
def comparar_posicion_sexo():
    print("=== COMPARACIÓN POR POSICIÓN Y SEXO ===")
    posicion = int(input("Ingrese la posición (1-5): "))
    sexo = input("Ingrese el sexo (m/f): ").lower()
    
    if posicion in ranking_2008 and sexo in ranking_2008[posicion] and posicion in datos2018 and sexo in datos2018[posicion]:
        nombre_2008 = ranking_2008[posicion][sexo]["nombre"]
        cantidad_2008 = ranking_2008[posicion][sexo]["cantidad"]
        
        nombre_2018 = datos2018[posicion][sexo]["nombre"]
        cantidad_2018 = datos2018[posicion][sexo]["cantidad"]
        
        diferencia = abs(cantidad_2008 - cantidad_2018)
        
        if cantidad_2008 > cantidad_2018:
            tipo_sexo = "Varones" if sexo == "m" else "Mujeres"
            print(f"{tipo_sexo} en posición #{posicion}: {diferencia} nacimientos de {'varones' if sexo == 'm' else 'mujeres'} más del primero del ranking de 2008 {nombre_2008} sobre {nombre_2018} del 2018")
        else:
            tipo_sexo = "Varones" if sexo == "m" else "Mujeres"
            print(f"{tipo_sexo} en posición #{posicion}: {diferencia} es la diferencia entre {nombre_2018} del 2018 sobre {nombre_2008} del 2008")
    else:
        print("Posición o sexo no válidos")

# Función 2: Nombres que comienzan con la misma letra
def nombres_por_letra():
    print("\n=== NOMBRES POR LETRA INICIAL ===")
    letra = input("Ingrese la letra inicial: ").upper()
    
    # Obtener todos los nombres de ambos años
    nombres_encontrados = []
    
    # Nombres de 2008
    for nombre in todos_nombres_2008:
        if nombre[0].upper() == letra:
            nombres_encontrados.append(nombre)
    
    # Nombres de 2018
    for posicion in datos2018:
        for sexo in datos2018[posicion]:
            nombre = datos2018[posicion][sexo]["nombre"]
            if nombre[0].upper() == letra:
                nombres_encontrados.append(nombre)
    
    # Eliminar duplicados y ordenar
    nombres_unicos = list(set(nombres_encontrados))
    nombres_unicos.sort()
    
    if nombres_unicos:
        print(f"Nombres con {letra}: {' '.join(nombres_unicos)}")
    else:
        print(f"No se encontraron nombres que comiencen con {letra}")

# Función 3: Nombres que se repiten en ambos años
def nombres_repetidos():
    print("\n=== NOMBRES REPETIDOS EN AMBOS AÑOS ===")
    
    # Obtener nombres de 2018
    nombres_2018 = []
    for posicion in datos2018:
        for sexo in datos2018[posicion]:
            nombres_2018.append(datos2018[posicion][sexo]["nombre"])
    
    # Encontrar nombres repetidos
    repetidos = []
    for nombre_2008 in todos_nombres_2008:
        if nombre_2008 in nombres_2018:
            repetidos.append(nombre_2008)
    
    # Eliminar duplicados y ordenar
    repetidos_unicos = list(set(repetidos))
    repetidos_unicos.sort()
    
    if repetidos_unicos:
        print(f"Nombres que se repiten: {' '.join(repetidos_unicos)}")
    else:
        print("No hay nombres repetidos entre ambos años")

# Menú principal
def menu_principal():
    while True:
        print("\n" + "="*50)
        print("ANÁLISIS DE NOMBRES DE BEBÉS 2008 vs 2018")
        print("="*50)
        print("1. Comparar por posición y sexo")
        print("2. Buscar nombres por letra inicial")
        print("3. Mostrar nombres repetidos")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            comparar_posicion_sexo()
        elif opcion == "2":
            nombres_por_letra()
        elif opcion == "3":
            nombres_repetidos()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar programa
if __name__ == "__main__":
    menu_principal()