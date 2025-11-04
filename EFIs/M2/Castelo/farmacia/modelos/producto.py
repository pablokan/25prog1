from modelos.clases import Medicamento, Perfumeria, Proveedor

def crear_medicamento():
    nombre = input('Ingrese nombre del medicamento: ')
    fecha = input('Ingrese el vencimiento (DD-MM-AAAA): ')
    codigo = input('Ingrese el codigo: ')
    cantidad = input('Ingrese la cantidad: ')
    venta_libre = input('Ingrese si es de venta libre (s/n): ')
    precio = input('Ingrese el precio del producto: ')
    proveedor_nombre = input('Ingrese el nombre del proveedor: ')
    proveedor_telefono = input('Ingrese el telefono del proveedor: ')
    proveedor_direccion = input('Ingrese la direccion del proveedor: ')
    proveedor = Proveedor(proveedor_nombre, proveedor_telefono, proveedor_direccion)
    medicamento = Medicamento(nombre, fecha, codigo, cantidad, venta_libre, precio, proveedor)
    return medicamento

def crear_perfumeria():
    nombre = input('Ingrese el nombre del producto: ')
    fecha = input('Ingrese el vencimiento (DD-MM-AAAA): ') # separar el ingreso de la fecha
    codigo = input('Ingrese el codigo: ')
    cantidad = input('Ingrese la cantidad del producto: ')
    precio = input('Ingrese el precio del producto: ')
    perfumeria = Perfumeria(nombre, fecha, codigo, cantidad, precio)
    return perfumeria

def almacenar_producto(producto):
    if isinstance(producto, Medicamento):
        archivo = "datos/archivero.txt"
        with open(archivo, "a", encoding="utf-8") as file:
            file.write(
                f"Medicamento,{producto.nombre},{producto.fecha},"
                f"{producto.codigo},{producto.cantidad},{producto.venta_libre},"
                f"{producto.precio},{producto.proveedor.nombre},{producto.proveedor.telefono}\n"
            )
            
    elif isinstance(producto, Perfumeria):
        archivo = "datos/archivero.txt"
        with open(archivo, "a", encoding="utf-8") as file:
            file.write(
                f"Perfumeria,{producto.nombre},{producto.codigo},{producto.cantidad},"
                f"{producto.precio},{producto.fecha}\n"
            )

def listar_productos():
    archivo = "datos/archivero.txt"
    print("Lista de Productos:")
    with open(archivo, "r", encoding="utf-8") as file:
        for linea in file:
            print(linea.strip())