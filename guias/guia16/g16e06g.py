class Archivo:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano

class Directorio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivos = []
        self.subdirectorios = []

    def agregar_archivo(self, archivo):
        self.archivos.append(archivo)

    def agregar_directorio(self, directorio):
        self.subdirectorios.append(directorio)

    def calcular_tamano_total(self):
        tamano_total = 0
        # Calcular el tamaño de los archivos en el directorio actual
        for archivo in self.archivos:
            tamano_total += archivo.tamano
        # Calcular el tamaño de los subdirectorios de forma recursiva
        for directorio in self.subdirectorios:
            tamano_total += directorio.calcular_tamano_total()
        return tamano_total

# Ejemplo de uso:
# Crear archivos
archivo1 = Archivo("documento.txt", 100)
archivo2 = Archivo("imagen.jpg", 500)
archivo3 = Archivo("video.mp4", 2000)
archivo4 = Archivo("hoja_de_calculo.xlsx", 300)

# Crear directorios
directorio_raiz = Directorio("directorio_raiz")
subdirectorio1 = Directorio("documentos")
subdirectorio2 = Directorio("multimedia")
subsubdirectorio = Directorio("informes")

# Agregar archivos y directorios a los directorios correspondientes
subdirectorio1.agregar_archivo(archivo1)
subdirectorio1.agregar_directorio(subsubdirectorio)
subsubdirectorio.agregar_archivo(archivo4)
subdirectorio2.agregar_archivo(archivo2)
subdirectorio2.agregar_archivo(archivo3)
directorio_raiz.agregar_directorio(subdirectorio1)
directorio_raiz.agregar_directorio(subdirectorio2)

# Calcular el tamaño total
tamano_total = directorio_raiz.calcular_tamano_total()

# Imprimir el resultado
print(f"El tamaño total del directorio_raiz es: {tamano_total} KB")