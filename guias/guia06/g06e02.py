inventario = {"camisetas": 10, "pantalones": 5, "zapatos": 3, "camisas": 8}
del(inventario["zapatos"])
for articulo in inventario.keys():
    inventario[articulo] *= 2

print(inventario)


