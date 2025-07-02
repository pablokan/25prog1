

def saludo(nombre: str, edad: int) -> str:
    return f'Hola {nombre} tenés {edad} años'

def main() -> None:
    altura: float = 1.98
    caracteristicas: list[int] = [11, 22]
    print(altura)
    print(saludo())

if __name__ == "__main__":
    main()

