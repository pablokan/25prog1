inventario = {"camisetas": 10, "pantalones": 5, "zapatos": 3, "camisas": 8}
del inventario['zapatos']
""" 
for articulo, cantidad in inventario.items():
    inventario[articulo] = cantidad * 2
print(inventario) 
"""
for cantidad in inventario.values():
    if cantidad > 9:
        print(cantidad)