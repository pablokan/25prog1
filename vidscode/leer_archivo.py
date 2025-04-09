a = open("nombres.txt", "r", encoding="UTF-8") # modo de apertura r (lectura)
""" print(f"Posición del puntero: {a.tell()}")
todo = a.read() # leo todo el archivo
print(f"Posición del puntero: {a.tell()}")
print(todo)
a.seek(2) # mueve el puntero al byte 2
letra = a.read(1) # lee la cantidad que dice el argumento
print(f"{letra=}") # print("letra=", letra)
tresCaracteres = a.read(3)
print(f"{tresCaracteres=}")
a.close()
"""

#lineas = a.readlines()
#print(lineas)

#a.seek(0)
# para que vean que pasa pero NO recomendado
""" linea = " "
while linea != "":
    linea = a.readline()
    print(linea)
"""
a.seek(0)
for linea in a:
    print(linea, end="")