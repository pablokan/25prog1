
# idea de botones basicos

'''
from textual.app import App, ComposeResult
from textual.widgets import Button, Static, Input
from modelos.clases import Producto, Medicamento, Perfumeria, Proveedor
from modelos.producto import guardar_producto, listar_productos

class FormProducto(Static):
    def compose(self) -> ComposeResult:
        yield Static("=== Cargar Producto ===\n")

        self.nombre_input = Input(placeholder="Nombre")
        yield Static("Nombre:")
        yield self.nombre_input

        self.tipo_input = Input(placeholder="Tipo (Medicamento/Perfumeria)")
        yield Static("Tipo:")
        yield self.tipo_input

        self.codigo_input = Input(placeholder="Código")
        yield Static("Código:")
        yield self.codigo_input

        self.cantidad_input = Input(placeholder="Cantidad")
        yield Static("Cantidad:")
        yield self.cantidad_input

        self.fecha_input = Input(placeholder="Fecha (DD-MM-YYYY)")
        yield Static("Fecha (solo Medicamento):")
        yield self.fecha_input

        self.concentracion_input = Input(placeholder="Concentración")
        yield Static("Concentración (solo Medicamento):")
        yield self.concentracion_input

        self.venta_libre_input = Input(placeholder="Venta Libre? (si/no)")
        yield Static("Venta Libre (solo Medicamento):")
        yield self.venta_libre_input

        self.proveedor_nombre_input = Input(placeholder="Proveedor Nombre")
        yield Static("Proveedor Nombre (solo Medicamento):")
        yield self.proveedor_nombre_input

        self.proveedor_telefono_input = Input(placeholder="Proveedor Teléfono")
        yield Static("Proveedor Teléfono (solo Medicamento):")
        yield self.proveedor_telefono_input

        self.marca_input = Input(placeholder="Marca (solo Perfumeria)")
        yield Static("Marca (solo Perfumeria):")
        yield self.marca_input

        yield Button("Guardar", id="guardar_producto")
        yield Button("Volver", id="volver_producto")
        self.resultado = Static("")
        yield self.resultado

class ListarProductos(Static):
    def compose(self) -> ComposeResult:
        yield Static("=== Lista de Productos ===\n")
        self.resultado = Static("")
        yield self.resultado
        yield Button("Volver", id="volver_listar")

    def mostrar_productos(self):
        productos = listar_productos()
        texto = ""
        for p in productos:
            texto += f"ID:{p[0]} | {p[1]} | Tipo:{p[2]} | Cod:{p[3]} | Cant:{p[4]}\n"
        self.resultado.update(texto)

class MiApp(App):
    def compose(self) -> ComposeResult:
        yield Static("=== Menú Principal ===\n")
        yield Button("Cargar Producto", id="cargar_producto")
        yield Button("Listar Productos", id="listar_productos")

        self.form_producto = FormProducto()
        self.form_producto.visible = False
        yield self.form_producto

        self.lista_productos = ListarProductos()
        self.lista_productos.visible = False
        yield self.lista_productos

    async def on_button_pressed(self, event):
        
        if event.button.id == "cargar_producto":
            self.form_producto.visible = True
            self.lista_productos.visible = False

        elif event.button.id == "listar_productos":
            self.lista_productos.mostrar_productos()
            self.lista_productos.visible = True
            self.form_producto.visible = False

        elif event.button.id == "guardar_producto":
            tipo = self.form_producto.tipo_input.value.lower()
            if tipo == "medicamento":
                proveedor = Proveedor(
                    self.form_producto.proveedor_nombre_input.value,
                    self.form_producto.proveedor_telefono_input.value
                )
                producto = Medicamento(
                    nombre=self.form_producto.nombre_input.value,
                    fecha=self.form_producto.fecha_input.value,
                    concentracion=self.form_producto.concentracion_input.value,
                    codigo=self.form_producto.codigo_input.value,
                    cantidad=int(self.form_producto.cantidad_input.value),
                    venta_libre=self.form_producto.venta_libre_input.value.lower() in ["si", "s"],
                    proveedor=proveedor
                )
            elif tipo == "perfumeria":
                producto = Perfumeria(
                    nombre=self.form_producto.nombre_input.value,
                    codigo=self.form_producto.codigo_input.value,
                    cantidad=int(self.form_producto.cantidad_input.value),
                    marca=self.form_producto.marca_input.value
                )

            guardar_producto(producto)
            self.form_producto.resultado.update("Producto guardado correctamente.")

        elif event.button.id == "volver_producto":
            self.form_producto.visible = False
        elif event.button.id == "volver_listar":
            self.lista_productos.visible = False

if __name__ == "__main__":
    MiApp().run()

'''
from modelos.clases import Farmacia
from modelos.producto import crear_medicamento, crear_perfumeria, almacenar_producto, listar_productos

if __name__ == "__main__":
    mi_farmacia = Farmacia("Farmacia Ibuprofeno&Fe")

    while True:
        print("\n--- Menú de Farmacia ---")
        print("1. Agregar medicamento")
        print("2. Agregar producto de perfumería")
        print("3. Listar productos actuales")
        print("4. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            med = crear_medicamento()
            almacenar_producto(med)

        elif opcion == "2":
            perf = crear_perfumeria()
            mi_farmacia.almacenar_producto(perf)
            

        elif opcion == "3":
            listar_productos()

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción inválida, intente de nuevo.")