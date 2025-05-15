numeros1 = []
for x in range(5):
    if x % 2 == 0:
        numeros1.append(x)
print(numeros1)

numeros2 = [x for x in range(5) if x % 2 == 0]
print(numeros2)

