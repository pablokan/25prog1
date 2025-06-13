def calcular_salario(nombre, salario, **adicionales):
    print(f'Salario de {nombre}: ', end='')
    print(f'Base=${salario}', end=' - ')
    total_adicionales = 0
    for adicional, monto in adicionales.items():
        print(f'{adicional}=${monto}', end=' ')
        total_adicionales += monto
    print(f'Total a cobrar=${salario+total_adicionales}')

calcular_salario('Ana', 1_000_000, presentismo=10, simpatia=20)
calcular_salario('Luis', 1_100_000, simpatia=-10, eficiencia=100, antiguedad=70)
calcular_salario('Pedro', 700_000)
