import customtkinter as ctk
from tkinter import ttk
from ui.ventana_info import ANCHO_MONITOR, ALTO_MONITOR
from sgif.database.crud import Vehiculo
from ui.estados.estado.editar_info_movil import EditarInformacion
from ui.estados.estado.habilitar import HabilitarMovil

class Mantenimiento:
    def __init__(self, ventana):
        self.ventana = ventana
        self.vehiculos_db = Vehiculo()  

        self.frame_contenido = ctk.CTkFrame(
            self.ventana,
            width=ANCHO_MONITOR / 1.7,
            height=ALTO_MONITOR / 1.5,
            fg_color='#65768D')
        self.frame_contenido.pack(side='left')
        self.frame_contenido.pack_propagate(False)

        self.frame_contenedor_moviles = ctk.CTkFrame(
            self.frame_contenido,
            width=int(ANCHO_MONITOR / 6),
            height=int(ALTO_MONITOR / 1),
            fg_color='#65768D')
        
        self.frame_contenedor_moviles.pack(
            side='left',
            pady=int(ALTO_MONITOR / 130),
            padx=int(ANCHO_MONITOR / 130))
        self.frame_contenedor_moviles.pack_propagate(False)

        self._crear_botones_habilitar()

        self.frame_moviles = ctk.CTkScrollableFrame(
            self.frame_contenedor_moviles,
            width=int(ANCHO_MONITOR / 4),
            height=int(ALTO_MONITOR / 1),
            fg_color='#5F6977',
            scrollbar_button_color='white')
        self.frame_moviles.pack(pady=int(ALTO_MONITOR / 130))

        ctk.CTkLabel(
            self.frame_moviles,
            text='MÓVILES',
            font=('Impact', 30),
            text_color='white'
        ).pack(pady=int(ALTO_MONITOR / 130))

        self._crear_frame_mantenimiento()
        self.crear_botones_filtrados()

    def _crear_botones_habilitar(self):
        self.frame_botones_habilitar_moviles = ctk.CTkFrame(
            self.frame_contenedor_moviles,
            width=int(ANCHO_MONITOR / 4),
            height=int(ALTO_MONITOR / 17),
            fg_color='#65768D')
        self.frame_botones_habilitar_moviles.pack(pady=int(ALTO_MONITOR / 130))

        self.boton_habilitar = ctk.CTkButton(
            self.frame_botones_habilitar_moviles,
            text='HABILITAR',
            width=int(ANCHO_MONITOR / 15),
            height=int(ALTO_MONITOR / 18),
            font=('Impact', 15),
            fg_color='white',
            text_color='black',
            hover_color='#5F6977',
            command=lambda: HabilitarMovil())
        self.boton_habilitar.pack(padx=int(ANCHO_MONITOR / 130), side='left')

        self.boton_deshabilitar = ctk.CTkButton(
            self.frame_botones_habilitar_moviles,
            text='DESHABILITAR',
            width=int(ANCHO_MONITOR / 15),
            height=int(ALTO_MONITOR / 18),
            font=('Impact', 15),
            fg_color='white',
            text_color='black',
            hover_color='#5F6977')
        self.boton_deshabilitar.pack(padx=int(ANCHO_MONITOR / 130), side='left')

    def _crear_frame_mantenimiento(self):
        self.frame_mantenimiento_moviles = ctk.CTkFrame(
            self.frame_contenido,
            width=int(ANCHO_MONITOR / 2),
            height=int(ALTO_MONITOR / 1),
            fg_color='#65768D')
        self.frame_mantenimiento_moviles.pack(pady=int(ALTO_MONITOR / 130))
        self.frame_mantenimiento_moviles.pack_propagate(False)

        # Título
        self.frame_moviles_fuera_servicio = ctk.CTkScrollableFrame(
            self.frame_mantenimiento_moviles,
            width=int(ANCHO_MONITOR / 3),
            height=int(ALTO_MONITOR / 10),
            fg_color='#5F6977',
            scrollbar_button_color='white')
        self.frame_moviles_fuera_servicio.pack(pady=int(ALTO_MONITOR / 130))

        ctk.CTkLabel(
            self.frame_moviles_fuera_servicio,
            text='MANTENIMIENTO',
            font=('Impact', 30),
            text_color='white'
        ).pack(pady=int(ALTO_MONITOR / 130))

        # Botones AGREGAR / ELIMINAR
        self.frame_botones_estado = ctk.CTkFrame(
            self.frame_mantenimiento_moviles,
            width=int(ANCHO_MONITOR / 4),
            height=int(ALTO_MONITOR / 15),
            fg_color='#65768D'
        )
        self.frame_botones_estado.pack(pady=int(ALTO_MONITOR / 130))

        ctk.CTkButton(
            self.frame_botones_estado,
            text='AGREGAR',
            width=int(ANCHO_MONITOR / 8),
            height=int(ALTO_MONITOR / 22),
            fg_color='white',
            text_color='black',
            font=('Impact', 15),
            hover_color='#5F6977',
            command=lambda: self.cambiar_estado_vehiculo(agregar=True)
        ).pack(side='left', padx=10)

        ctk.CTkButton(
            self.frame_botones_estado,
            text='ELIMINAR',
            width=int(ANCHO_MONITOR / 8),
            height=int(ALTO_MONITOR / 22),
            fg_color='white',
            text_color='black',
            font=('Impact', 15),
            hover_color='#5F6977',
            command=lambda: self.cambiar_estado_vehiculo(agregar=False)
        ).pack(side='left', padx=10)

    def crear_botones_filtrados(self):
        self.limpiar_botones()
        self.frame_moviles.update_idletasks()
        self.frame_moviles_fuera_servicio.update_idletasks()

        todos_vehiculos = self.vehiculos_db.listar_columnas('patente', 'estado_id')

        for v in todos_vehiculos:
            patente = v['patente']
            estado_id = v['estado_id']

            frame_destino = self.frame_moviles_fuera_servicio if estado_id == 3 else self.frame_moviles

            boton = ctk.CTkButton(
                frame_destino,
                text=patente,
                fg_color='white',
                text_color='black',
                font=('Impact', 20),
                width=int(ANCHO_MONITOR / 8),
                height=int(ALTO_MONITOR / 20),
                command=lambda p=patente: self.mostrar_informacion('patente', p))
            boton.pack(pady=3)

    def cambiar_estado_vehiculo(self, agregar=True):
        if agregar:
            vehiculos_combo = [v['patente'] for v in self.vehiculos_db.listar_columnas('patente', 'estado_id') if v['estado_id'] != 3]
            nuevo_estado = 3
            titulo = "Agregar a Mantenimiento"
        else:
            vehiculos_combo = [v['patente'] for v in self.vehiculos_db.listar_columnas('patente', 'estado_id') if v['estado_id'] == 3]
            nuevo_estado = 1
            titulo = "Sacar de Mantenimiento"

        if not vehiculos_combo:
            ctk.CTkLabel(self.frame_moviles_fuera_servicio, text="No hay vehículos disponibles",
                         text_color='white', font=('Arial', 14)).pack(pady=5)
            return

        ventana_popup = ctk.CTkToplevel(self.ventana)
        ventana_popup.title(titulo)
        ventana_popup.geometry("300x150")
        ventana_popup.attributes("-topmost", True)

        ctk.CTkLabel(ventana_popup, text="Selecciona vehículo:", font=("Arial", 14)).pack(pady=10)

        combo = ttk.Combobox(ventana_popup, values=vehiculos_combo, state="readonly")
        combo.pack(pady=5)

        def confirmar():
            seleccionado = combo.get()
            if seleccionado:
                self.vehiculos_db.actualizar('estado_id', nuevo_estado, 'patente', seleccionado)
                ventana_popup.destroy()
                self.crear_botones_filtrados()

        ctk.CTkButton(ventana_popup, text="Confirmar", command=confirmar).pack(pady=10)

    def mostrar_informacion(self, columna, valor):
        info_movil = ctk.CTkToplevel(self.ventana)
        info_movil.title(f"Información del Móvil: {valor}")
        info_movil.geometry("300x420")
        info_movil.attributes("-topmost", True)
        info_movil.configure(fg_color="#5F6977")

        frame_info = ctk.CTkScrollableFrame(info_movil, width=250, height=350, fg_color='white')
        frame_info.pack(pady=5)

        ctk.CTkLabel(
            frame_info,
            text=f"Detalles de {valor}",
            text_color="black",
            font=("Impact", 22)
        ).pack(pady=10)

        datos = self.vehiculos_db.obtener_datos(columna, valor)
        if not datos:
            ctk.CTkLabel(
                frame_info,
                text="No se encontraron datos.",
                text_color="white",
                font=("Arial", 14)
            ).pack(pady=5)
            return

        for clave, val in datos[0].items():
            if "id" in clave.lower():
                continue

            clave_formateada = clave.replace("_", " ").capitalize()

            fila = ctk.CTkFrame(frame_info, fg_color="#6B7A8F", corner_radius=8)
            fila.pack(fill="x", padx=15, pady=3)

            ctk.CTkLabel(
                fila,
                text=f"{clave_formateada}:",
                text_color="white",
                font=("Arial", 13, "bold"),
                anchor="w",
                width=120,
                justify="left"
            ).grid(row=0, column=0, sticky="w", padx=8, pady=3)

            ctk.CTkLabel(
                fila,
                text=str(val),
                text_color="white",
                font=("Arial", 13),
                anchor="w",
                justify="left"
            ).grid(row=0, column=1, sticky="w", padx=8, pady=3)

        self.boton_editar = ctk.CTkButton(info_movil, text='EDITAR', width=100, height=30, fg_color='white', text_color='black', font=('impact', 20), command=lambda: EditarInformacion(info_movil, columna, valor, ventana_principal=self))
        self.boton_editar.pack(pady=5)

    def limpiar_botones(self):
        for widget in self.frame_moviles.winfo_children():
            widget.destroy()
        for widget in self.frame_moviles_fuera_servicio.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.destroy()

    def refrescar_pantalla(self):
        """Recrea todo el contenido del frame de mantenimiento."""
        # Destruye el frame actual
        self.frame_contenido.destroy()
        # Crea una nueva instancia del mismo frame en la ventana principal
        nuevo = Mantenimiento(self.ventana)
        # Reemplaza la referencia
        self.frame_contenido = nuevo.frame_contenido