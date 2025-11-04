from clases import Cliente, Usuario
import os

def crear_usuario():
    usuarios = []
    print('carga de datos del usuario')
    respuesta = 'si'
    while respuesta == 'si':
        nombre = input('Ingrese el nombre completo: ')        
        apellido = input('Ingrese el apellido completo: ')
        dni = input('Ingresa tu DNI: ')
        correo = input('Ingresa tu correo electronico: ')
        telefono = input('Ingresa tu numero de telefono: ')
        try:
            while True:
                contraseña = input('Escriba su contraseña: ')
                if len(contraseña) >= 7:
                    break
                else:
                    print(f'Contraseña invalida, debe contener mas de 7 caracteres')
        except:
               None
        usuarios.append(Usuario(nombre, apellido, correo, contraseña))
        print('¿Desea agregar otro usuario?')
        respuesta = input('escribir(si/no): ').lower()
    print('usuarios cargados!')
    return usuarios

def crear_cliente():
    clientes = []
    respuesta = 'si'
    print('carga de datos del cliente')
    while respuesta == 'si':
        nombre = input('Ingrese el nombre completo: ')
        apellido = input('Ingrese el apellido completo: ')
        dni = input('Ingresa tu DNI: ')
        correo = input('Ingresa tu correo electronico: ')
        telefono = input('Ingresa tu numero de telefono: ')
        obra_social = input('Posee obra social(si/no): ').lower()
        receta = input('Posee receta(si/no): ').lower()
        clientes.append(Cliente(nombre, apellido, dni, correo, telefono))
        print('¿Desea agregar otro cliente?')
        respuesta = input('escribir(si/no): ').lower()
    print('clientes cargados!')
    return clientes

def almacenar_personas(persona):
    os.makedirs('datos', exist_ok=True)  #Asegura que la carpeta exista
    if isinstance(persona, Usuario):
        archivo = os.path.join('datos', 'usuario.txt') #Recorrido al usuario.txt
        with open(archivo, 'a', encoding='utf-8') as file:
            file.write(f'usuario:\nNombre completo: {persona.nombre} {persona.apellido}\ncontraseña: {persona.contraseña}\ncorreo: {persona.correo}\n')
    elif isinstance(persona, Cliente): #Recorrido al cliente.txt
        archivo = os.path.join('datos', 'cliente.txt')
        with open(archivo, 'a', encoding='utf-8') as file:
            file.write(f'cliente:\nNombre completo: {persona.nombre} {persona.apellido}\nDNI: {persona.dni}\nCorreo: {persona.correo}\nTelefono: {persona.telefono}\n')

def main():
    usuarios = crear_usuario()
    print('Datos cargados: ')
    for usuario in usuarios:
        almacenar_personas(usuario)
        print(usuario)
    clientes = crear_cliente()
    for cliente in clientes:
        almacenar_personas(cliente)
        print(cliente)
if __name__ == '__main__':
    main()
