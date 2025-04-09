a = open("nuevos_nombres.txt", "w", encoding="UTF-8") # modo de apertura w (escritura)
print(f"Posición del puntero: {a.tell()}")
a.write("Benjamín\n")
a.write("Etelvina\n")
listaNombres = ["n1\n", "n2\n", "n3\n"]
a.writelines(listaNombres)
a.close()

a = open("nuevos_nombres.txt", "a", encoding="UTF-8") # add
print(f"Posición del puntero: {a.tell()}")
a.write("despues de abrir en modo a")
a.close()
