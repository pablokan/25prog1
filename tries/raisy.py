from typing import Callable, Any

def procesar_edad(edad: int) -> None:
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero.")
    if edad < 0:
        raise ValueError("La edad no puede ser un número negativo.")
    # Código para procesar la edad...
    print(f"Edad procesada: {edad}")


def ftry(funcion: Callable[..., Any], *args: Any) -> None:
    try:
        funcion(*args)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

ftry(procesar_edad, "veinte")
ftry(procesar_edad, -12)
ftry(procesar_edad, 24)