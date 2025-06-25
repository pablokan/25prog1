#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def agregar_texto_a_jpg(ruta_archivo, texto="hola mundo"):
    """
    Agrega texto al final de un archivo JPG.
    
    Args:
        ruta_archivo (str): Ruta al archivo JPG
        texto (str): Texto a agregar al final del archivo
    """
    try:
        # Abrir el archivo en modo binario para lectura
        with open(ruta_archivo, 'rb') as archivo:
            contenido_original = archivo.read()
        
        # Convertir el texto a bytes usando UTF-8
        texto_bytes = texto.encode('utf-8')
        
        # Abrir el archivo en modo binario para escritura
        with open(ruta_archivo, 'wb') as archivo:
            # Escribir el contenido original
            archivo.write(contenido_original)
            # Agregar el texto al final
            archivo.write(texto_bytes)
        
        print(f"Texto '{texto}' agregado exitosamente al archivo {ruta_archivo}")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
    except PermissionError:
        print(f"Error: No se tienen permisos para modificar {ruta_archivo}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def crear_copia_con_texto(ruta_original, ruta_nueva, texto="hola mundo"):
    """
    Crea una copia del archivo JPG con el texto agregado al final.
    
    Args:
        ruta_original (str): Ruta al archivo JPG original
        ruta_nueva (str): Ruta para el nuevo archivo con texto
        texto (str): Texto a agregar al final del archivo
    """
    try:
        # Leer el archivo original
        with open(ruta_original, 'rb') as archivo:
            contenido_original = archivo.read()
        
        # Convertir el texto a bytes
        texto_bytes = texto.encode('utf-8')
        
        # Crear el nuevo archivo con el contenido original + texto
        with open(ruta_nueva, 'wb') as archivo:
            archivo.write(contenido_original)
            archivo.write(texto_bytes)
        
        print(f"Nueva imagen creada: {ruta_nueva} con texto '{texto}' agregado")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_original}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    # Opción 1: Modificar el archivo original
    nombre_archivo = "2024-10-22-193257.jpg"
    
    print("=== Modificar archivo original ===")
    agregar_texto_a_jpg(nombre_archivo)
    
    # Opción 2: Crear una copia con el texto agregado
    print("\n=== Crear copia con texto ===")
    archivo_original = "2024-10-22-193257.jpg"
    archivo_copia = "imagen_con_texto.jpg"
    
    crear_copia_con_texto(archivo_original, archivo_copia)
    
    # Verificar que se agregó el texto
    print("\n=== Verificar contenido agregado ===")
    try:
        with open(nombre_archivo, 'rb') as f:
            contenido = f.read()
            # Mostrar los últimos 20 bytes del archivo
            print(f"Últimos 20 bytes: {contenido[-20:]}")
            # Intentar decodificar los últimos bytes como texto
            try:
                texto_final = contenido[-11:].decode('utf-8')
                print(f"Texto al final: '{texto_final}'")
            except UnicodeDecodeError:
                print("Los últimos bytes no son texto UTF-8 válido")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe")
