class Archivo:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano

class Directorio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivos: list[Archivo] = []
        self.subdirectorios: list[Directorio] = []

    def agregar_archivo(self, archivo):
        self.archivos.append(archivo)

    def agregar_directorio(self, directorio):
        self.subdirectorios.append(directorio)

    def calcular_tamano_total(self):
        tamano_total = 0
        for archivo in self.archivos:
            tamano_total += archivo.tamano
        for directorio in self.subdirectorios:
            tamano_total += directorio.calcular_tamano_total()
        return tamano_total

un_txt = Archivo("documento.txt", 100)
una_foto = Archivo("imagen.jpg", 500)
un_video = Archivo("video.mp4", 2000)
una_planilla = Archivo("hoja_de_calculo.xlsx", 300)

directorio_raiz = Directorio("directorio_raiz")
documentos = Directorio("documentos")
multimedia = Directorio("multimedia")
informes = Directorio("informes")

documentos.agregar_archivo(un_txt)
documentos.agregar_directorio(informes)
informes.agregar_archivo(una_planilla)
multimedia.agregar_archivo(una_foto)
multimedia.agregar_archivo(un_video)
directorio_raiz.agregar_directorio(documentos)
directorio_raiz.agregar_directorio(multimedia)

tamano_total = directorio_raiz.calcular_tamano_total()

print(f"El tamaño total del directorio_raiz es: {tamano_total} KB")