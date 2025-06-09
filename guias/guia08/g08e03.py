def promedio(*args, sinNegativos=False):
    numeros = list(args)
    if sinNegativos:
        numeros = [n for n in numeros if n>=0]
    total = 0
    for n in numeros:
        total += n
    prom = total / len(numeros)
    return int(prom) if prom.is_integer() else prom

print(promedio(121,65,-88,34,-9,27)) # 150/6=25
print(promedio(121,65,-88,34,-9,27, sinNegativos=True)) # 247/4=61.75
print(promedio(2,4)) # 3
