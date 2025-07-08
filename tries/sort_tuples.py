# Define una lista de tuplas
data = [('manzana', 3), ('banana', 1), ('cereza', 2), ('dátil', 5), ('baya_de_saúco', 4)]

# Imprime la lista original
print("Lista original de tuplas:")
print(data)

# Ordena la lista de tuplas por el segundo elemento
# El argumento `key` en el método `sort()` especifica una función que se llamará en cada elemento de la lista
# antes de realizar las comparaciones. El valor devuelto por esta función se utiliza para la ordenación real.
# En este caso, `lambda x: x[1]` es una función anónima (función lambda) que toma un elemento `x`
# (que es una tupla de la lista) y devuelve su segundo ítem (índice 1).
# Por lo tanto, la lista `data` se ordenará según los valores en el índice 1 de sus tuplas.
data.sort(key=lambda x: x[1])

# Imprime la lista ordenada
print("\nLista de tuplas ordenada (por el segundo elemento):")
print(data)

# Ejemplo con diferentes tipos de datos en el segundo elemento
datos_mixtos = [('Juan', 25), ('Juana', 30), ('Pérez', 22), ('Alicia', 28)]
print("\nLista original de datos mixtos:")
print(datos_mixtos)

datos_mixtos.sort(key=lambda x: x[1])
print("\nLista de datos mixtos ordenada (por edad):")
print(datos_mixtos)

# Ejemplo con segundos elementos de tipo cadena de texto
datos_cadena = [('Tarea A', 'Alta'), ('Tarea B', 'Baja'), ('Tarea C', 'Media')]
print("\nLista original de datos de cadena:")
print(datos_cadena)

# Al ordenar con elementos de cadena, la `key` todavía extrae el elemento por el cual ordenar.
# Por defecto, las cadenas se ordenan alfabéticamente.
datos_cadena.sort(key=lambda x: x[1]) # Ordena alfabéticamente según el segundo elemento de las tuplas.
print("\nLista de datos de cadena ordenada (por prioridad - alfabética):")
print(datos_cadena)

# Para ordenar cadenas en un orden personalizado (por ejemplo, Baja, Media, Alta),
# podemos usar un diccionario para mapear las prioridades de cadena a valores numéricos.
# La función `key` luego busca este valor numérico para la ordenación.
orden_prioridad = {'Baja': 0, 'Media': 1, 'Alta': 2}
# `orden_prioridad.get(x[1], -1)` recupera el valor de `orden_prioridad` para la cadena `x[1]`.
# Si la cadena no se encuentra en el diccionario, por defecto es -1 (o cualquier otro valor que ayude en la ordenación).
datos_cadena.sort(key=lambda x: orden_prioridad.get(x[1], -1))
print("\nLista de datos de cadena ordenada (por orden de prioridad personalizado):")
print(datos_cadena)