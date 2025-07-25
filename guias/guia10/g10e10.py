class Empleado:
    def __init__(self, nombre, salario) -> None:
        self.nombre = nombre
        self.salario = salario
        self.aumento = False

    def aumentar_salario(self, porcentaje):
        self.salario *= (porcentaje / 100) + 1
        self.aumento = True


datos = [
    ('A', 100),
    ('B', 100),
    ('C', 100),
    ('D', 100),
    ('E', 100),
]

empleados = [Empleado(*dato) for dato in datos]

nombre_aumento = 'B'
porcentaje_aumento = 10

for empleado in empleados:
    if empleado.nombre == nombre_aumento:
        empleado.aumentar_salario(porcentaje_aumento)
        print(f"\nSalario de {empleado.nombre} aumentado a ${empleado.salario:g}\n")
        break # Salir del bucle una vez que el empleado sea encontrado y actualizado

for empleado in empleados:
    if not empleado.aumento:
        print(empleado.nombre)


