
nombres: list[str] = ['Juan', 'Ana']
def iniciales(ns: list[str]) -> list[str]:
    return [n[0] for n in ns]
print(iniciales(nombres))

persona: dict[str, object] = {'nombre': 'Juan', 'edad': 35}
def datos(d: dict[str, object]) -> str:
    return ' '.join([str(v) for v in d.values()])
print(datos(persona))

nombre: str
nombre = 11
alto: bool = False

personas: list[dict[str, object]] = [
        {'nombre': 'Juan', 'edad': 35},
        {'nombre': 'Ana', 'edad': 23}
]
for persona in personas:
    print(persona[])

