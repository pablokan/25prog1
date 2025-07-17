def crear_diccionario(archivo):
    info_dicci={}
    with open(archivo,"r")as f:
        contenido=f.readlines()
    for informacion in contenido[1:]:
        dni,nombre,deuda,localidad=informacion.split("#")
        info_dicci[dni]={"nombre_apellido":nombre,"deuda":int(deuda),"localidad":localidad[0:-1]}
    return info_dicci
            
def contar_localidad(info,localidad):
    contador=0
    for v in info.values():
       if v["localidad"] == localidad:
           contador+=1
    return contador
            
def acumulador_deuda(info,minimo_deuda=0,maximo_deuda=10**10):
    total_deuda=0
    for v in info.values():
        if maximo_deuda >= v["deuda"] >= minimo_deuda:
            total_deuda+=v["deuda"]
    return total_deuda

def modificar_archivo_apellidos(archivo,info,numero_dni=0):
    lista_apellidos_dni=[]
    for k,v in info.items():
        dni_persona=int(k)
        if dni_persona > numero_dni:
            __,apellido=v["nombre_apellido"].split()
            lista_apellidos_dni.append(apellido)
    
    with open(archivo,"w")as f:
        f.write(f"Apellidos de los clientes con DNI mayor a {numero_dni}: \n")
        for apellido in lista_apellidos_dni:
            f.writelines(f"{apellido}\n")
        



def main():
    direccion_archivo_clientes="clientes.txt"
    direccion_archivo_apellidos="apellidos.txt"
    diccionario_personas=crear_diccionario(direccion_archivo_clientes)

    cantidad_personas_lacarlota=contar_localidad(diccionario_personas,"La Carlota")
    print(f"La cantidad de Clientes de La Carlota es {cantidad_personas_lacarlota}")

    otra_localidad=input("Ingrese otra localidad: ")
    cantidad_personas_x=contar_localidad(diccionario_personas,otra_localidad)
    print(f"La cantidad de Clientes de {otra_localidad} es {cantidad_personas_x}")

    deuda1=acumulador_deuda(diccionario_personas,minimo_deuda=90000)
    print(f"El total de deuda acumulada de lo Clientes que deben más de 90.000 pesos es de ${deuda1}")

    deuda2=acumulador_deuda(diccionario_personas,maximo_deuda=40000)
    print((f"El total de deuda acumulada de lo Clientes que deben menos de 40.000 pesos es de ${deuda2}"))

    modificar_archivo_apellidos(direccion_archivo_apellidos,diccionario_personas,numero_dni=40000000)

    
if __name__ == "__main__":
    main()