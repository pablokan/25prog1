from pathlib import Path

# Ruta actual
ruta = Path('.')
ruta = Path.cwd()  # directorio actual

# Ruta específica
archivo = Path('mi_archivo.txt')
carpeta = Path('carpeta/subcarpeta')

# Ruta absoluta
ruta_abs = Path('/home/usuario/documentos')

ruta = Path('carpeta') / 'subcarpeta' / 'archivo.txt'

archivo = Path('documentos/texto.txt')
print(archivo.name)        # 'texto.txt'
print(archivo.stem)        # 'texto'
print(archivo.suffix)      # '.txt'
print(archivo.parent)      # 'documentos'

if archivo.exists():
    print("El archivo existe")

if ruta.is_file():
    print("Es un archivo")

if ruta.is_dir():
    print("Es un directorio")

for item in Path('.').iterdir():
    print(item)

# Solo archivos .txt
for txt in Path('.').glob('*.txt'):
    print(txt)