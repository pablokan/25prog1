nombre: str = 'Ana'
edad: int
edad = 22
egresado: bool = False
nombres: list[str] = ['Ana', 'Luis']
persona: dict[str, object] = {'nombre': 'Ana', 'edad': 22, 'notas': [4, 7]}

def main() -> None:
    print('Yo soy main')

def saludo(nombre: str) -> str:
    return f'Hola {nombre}!'

print(saludo('Juan'))

personas: list[dict[str, object]] = [
    {'nombre': 'Juan', 'edad': 35},
    {'nombre': 'Ana', 'edad': 23}
]   




