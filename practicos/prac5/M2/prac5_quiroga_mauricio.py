from funciones_practico5 import cantidad_de_clientes,total_deuda_clientes,escritura_apellido
def main():
    # cantidad de clientes por localidad literal y variable
    cantidad_de_localidad_literal = cantidad_de_clientes('clientes.txt', 'La Carlota')     
    print(f'La cantidad de clientes de La Carlota son: {cantidad_de_localidad_literal} clientes')
    cant_localidad_variable = cantidad_de_clientes('clientes.txt')
    print(f'La cantidad de clientes de la localidad ingresada es: {cant_localidad_variable} clientes')
    
    # monto total de deuda acumulada segun se ingrese el monto que se ingrese y la opcion (mayor que o menor que)
    monto_total_de_deuda = total_deuda_clientes('clientes.txt')
    print(monto_total_de_deuda)

    # apellidos de los clientes con documento mayor a un numero ingresado
    escritura_apellido('clientes.txt','apellidos.txt')

if __name__ == '__main__':
     main()