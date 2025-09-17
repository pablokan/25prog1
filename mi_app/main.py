# Importación de módulos propios
from modulos.clases import Persona
from modulos.funciones import sumar, es_par

def main():
    # Uso de una clase importada
    persona1 = Persona("kan", 60)
    print(persona1.saludar())

    # Uso de funciones importadas
    num1 = 5
    num2 = 10
    suma_resultado = sumar(num1, num2)
    print(f"La suma de {num1} y {num2} es: {suma_resultado}")

    numero_a_verificar = 7
    if es_par(numero_a_verificar):
        print(f"El número {numero_a_verificar} es par.")
    else:
        print(f"El número {numero_a_verificar} es impar.")

# Esto asegura que la función main() solo se ejecute
# si el script se corre directamente.
if __name__ == "__main__":
    main()
