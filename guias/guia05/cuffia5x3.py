#3)Recibir por teclado una cadena de números, dejarlo en formato string e insertar  un punto cada 3 dígitos como divisorio de miles.
# Ej.  “1234567890” debería devolver “1.234.567.890”

cadena_con_punto = ''
incio_sub_cadena = 1
final_sub_cadena = 4
cadena = input('Ingrese una cadena de numeros cualquiera: ') # 1205364

sub_cadena = cadena[0:1] + '.'  #1.

mitad_cadena = len(cadena)//3

for i in range(mitad_cadena):
    cadena_con_punto = cadena_con_punto + cadena[incio_sub_cadena:final_sub_cadena] + '.'
    incio_sub_cadena = final_sub_cadena
    final_sub_cadena = final_sub_cadena + 3
     
cadena_final = sub_cadena + cadena_con_punto  
print(cadena_final[:-1])
 