import os

def logeo_usuario():
    correo = input('Introduzca el correo: ').strip()
    contraseña = input('introduzca la contraseña: ').strip()
    try:
        archivo = os.path.join('datos', 'usuario.txt')
        with open(archivo, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
            datos = []
            bloque = []
            usuario_encontrado = False
            for linea in lineas:
                if linea.strip() == '':
                    if bloque: #Busca y verifica si existe el correo y la contraseña
                        tiene_correo = any(f'Correo: {correo}'.lower() in linea for linea in bloque)
                        tiene_contraseña = any(f'Contraseña: {contraseña}'.lower() in linea for linea in bloque)
                        if tiene_correo and tiene_contraseña:
                            datos = bloque
                            usuario_encontrado = True
                            break
                        bloque = []
                else:
                    bloque.append(linea)
            if not usuario_encontrado and bloque: #verifica en el bloque si el archivo (usuario.txt) termina con linea vacia
                tiene_correo = any(f'Correo: {correo}'.lower() in linea for linea in bloque)
                tiene_contraseña = any(f'Contraseña: {contraseña}'.lower() in linea for linea in bloque)
                if tiene_correo and tiene_contraseña:
                    datos = bloque
                    usuario_encontrado = True
            if usuario_encontrado:
                print('Usuario encontrado: ')
                print(''.join(datos))
                return ''.join(datos)
            else:
                print('Usuario no encontrado')
                return 'Usuario no encontrado'
    except FileNotFoundError:
        return 'Usuario no registrado'

def main():
    logeo_usuario()
if __name__ == '__main__':
    main()

