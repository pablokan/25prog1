import customtkinter as ctk
from datetime import date
from sgif.database.crud import Vehiculo, Modelo, Marca, Estado
import tkinter.messagebox as CTKmessagebox

class HabilitarMovil:
    def __init__(self):
        self.bd_vehiculo = Vehiculo()
        self.bd_modelo = Modelo()
        self.bd_marca = Marca()
        self.bd_estado = Estado()

        self.ventana_habilitar = ctk.CTkToplevel()
        self.ventana_habilitar.title("Habilitar Nuevo Móvil")
        self.ventana_habilitar.geometry("600x720")
        self.ventana_habilitar.attributes("-topmost", True)
        self.ventana_habilitar.configure(fg_color="#2B2B2B")

        self.frame_principal = ctk.CTkFrame(self.ventana_habilitar, fg_color="#39424E", corner_radius=15)
        self.frame_principal.pack(padx=20, pady=20, fill="both", expand=True)

        titulo = ctk.CTkLabel(
            self.frame_principal,
            text="Habilitar Nuevo Móvil",
            font=("Arial", 22, "bold"),
            text_color="white"
        )
        titulo.pack(pady=10)

        self.frame_campos = ctk.CTkScrollableFrame(self.frame_principal, fg_color="#505B6D", corner_radius=10)
        self.frame_campos.pack(fill="both", padx=10, pady=10, expand=True)

        self.entries = {}
        campos_entry = {
            "patente": "Patente",
            "n_chasis": "Número de chasis",
            "n_motor": "Número de motor",
            "anio": "Año de fabricación",
            "fecha_adquisicion": "Fecha de adquisición (YYYY-MM-DD)",
            "km_adquisicion": "Kilometraje al adquirir",
            "km_actual": "Kilometraje actual",
            "empresa_aseguradora": "Empresa aseguradora",
            "n_poliza": "N° de póliza"
        }

        for campo, texto in campos_entry.items():
            fila = ctk.CTkFrame(self.frame_campos, fg_color="#6B7A8F", corner_radius=8)
            fila.pack(fill="x", pady=5, padx=5)

            label = ctk.CTkLabel(fila, text=f"{texto}:", width=200, anchor="w", text_color="white")
            label.grid(row=0, column=0, padx=5, pady=5)

            entry = ctk.CTkEntry(fila, placeholder_text=texto, fg_color="white", text_color="black")
            entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
            fila.grid_columnconfigure(1, weight=1)

            self.entries[campo] = entry

        self.combos = {}

        self.modelos = self.bd_modelo.listar_columnas("modelo_id", "nombre")
        self.marcas = self.bd_marca.listar_columnas("marca_id", "nombre")
        self.estados = self.bd_estado.listar_columnas("estado_id", "nombre")

        self.crear_combobox("modelo_id", "Modelo", self.modelos)
        self.crear_combobox("marca_id", "Marca", self.marcas)
        self.crear_combobox("estado_id", "Estado", self.estados)

        boton_guardar = ctk.CTkButton(
            self.frame_principal,
            text="Guardar Móvil",
            fg_color="#4CAF50",
            hover_color="#45A049",
            command=self.guardar_movil
        )
        boton_guardar.pack(pady=20)

    def crear_combobox(self, campo, texto, opciones):
        fila = ctk.CTkFrame(self.frame_campos, fg_color="#6B7A8F", corner_radius=8)
        fila.pack(fill="x", pady=5, padx=5)

        label = ctk.CTkLabel(fila, text=f"{texto}:", width=200, anchor="w", text_color="white")
        label.grid(row=0, column=0, padx=5, pady=5)

        if isinstance(opciones[0], dict):
            nombres = [list(op.values())[1] for op in opciones]
        else:
            nombres = [op[1] for op in opciones]

        combo = ctk.CTkComboBox(
            fila,
            values=nombres,
            fg_color="white",
            button_color="#5F6977",
            button_hover_color="#4B5563",
            text_color="black",
            dropdown_text_color="black",
            dropdown_fg_color="white" )
        combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        fila.grid_columnconfigure(1, weight=1)
        self.combos[campo] = combo

    def guardar_movil(self):
        try:
            modelo_nombre = self.combos["modelo_id"].get()
            marca_nombre = self.combos["marca_id"].get()
            estado_nombre = self.combos["estado_id"].get()

            modelo_id = self.obtener_id_por_nombre(self.modelos, modelo_nombre)
            marca_id = self.obtener_id_por_nombre(self.marcas, marca_nombre)
            estado_id = self.obtener_id_por_nombre(self.estados, estado_nombre)

            datos = {
                "modelo_id": modelo_id,
                "patente": self.entries["patente"].get().upper(),
                "n_chasis": self.entries["n_chasis"].get(),
                "n_motor": self.entries["n_motor"].get(),
                "comb_id": 1,  
                "anio": self.entries["anio"].get(),
                "fecha_adquisicion": self.entries["fecha_adquisicion"].get() or str(date.today()),
                "km_adquisicion": self.entries["km_adquisicion"].get(),
                "km_actual": self.entries["km_actual"].get(),
                "estado_id": estado_id,
                "empresa_aseguradora": self.entries["empresa_aseguradora"].get(),
                "n_poliza": self.entries["n_poliza"].get(),
            }

            valores = tuple(datos[col] for col in self.bd_vehiculo.columnas)

            self.bd_vehiculo.insertar(valores)

            ctk.CTkMessagebox(title="Éxito!", message="Móvil habilitado correctamente.")
            self.ventana_habilitar.destroy()

        except Exception as e:
            ctk.CTkMessagebox(title="Error", message=f"Ocurrió un error: {e}")

    def obtener_id_por_nombre(self, lista, nombre):
        for item in lista:
            if isinstance(item, dict):
                if list(item.values())[1] == nombre:
                    return list(item.values())[0]
            else:
                if item[1] == nombre:
                    return item[0]
        return None