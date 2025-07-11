def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    print("Edad válida.")

try:
    verificar_edad(-5)
except ValueError as error:
    print(type(error))
    print(f"Se produjo un error: {error}")