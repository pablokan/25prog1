import customtkinter as ctk
from tkinter import ttk
from ui.ventana_info import ANCHO_MONITOR, ALTO_MONITOR
from sgif.database.crud import Vehiculo
from ui.estados.estado.check_list_moviles import CheckList


ESTADOS = {"DISPONIBLE": 1, "OCUPADO": 2, "MANTENIMIENTO": 3, "DESA": 4}

class Moviles:
    def __init__(self, ventana):
        self.ventana = ventana
        self.vehiculos_db = Vehiculo()
        self.boton_seleccionado = None

        self.frame_contenido = ctk.CTkFrame(self.ventana, width=ANCHO_MONITOR / 1.7, height=ALTO_MONITOR / 1.5, fg_color="#65768D")
        self.frame_contenido.pack(side="left", padx=10, pady=10)
        self.frame_contenido.pack_propagate(False)

        self._crear_frames_estado()
        self._actualizar_botones()
        self._crear_boton_estados()

        self.frame_informacion = ctk.CTkScrollableFrame(self.frame_contenido,fg_color='#5F6977', width=int(ANCHO_MONITOR / 1.8), height=ALTO_MONITOR / 18)
        self.frame_informacion.pack(pady=10)

    def _crear_frames_estado(self):
        self.frame_superior = ctk.CTkFrame(self.frame_contenido, fg_color="#65768D")
        self.frame_superior.pack(side="top")

        self.frame_disponibles = ctk.CTkScrollableFrame(
            self.frame_superior,
            width=ANCHO_MONITOR / 6.5,
            height=ALTO_MONITOR / 6,
            fg_color="#5F6977",
            scrollbar_button_color="white")
        self.frame_disponibles.pack(side="left", padx=10, pady=10)

        self.frame_ocupado = ctk.CTkScrollableFrame(
            self.frame_superior,
            width=ANCHO_MONITOR / 6.5,
            height=ALTO_MONITOR / 6,
            fg_color="#5F6977",
            scrollbar_button_color="white")
        self.frame_ocupado.pack(side="left", padx=10, pady=10)

        self.frame_mantenimiento = ctk.CTkScrollableFrame(
            self.frame_superior,
            width=ANCHO_MONITOR / 6.5,
            height=ALTO_MONITOR / 6,
            fg_color="#5F6977",
            scrollbar_button_color="white")
        self.frame_mantenimiento.pack(side="left", padx=10, pady=10)

        # Títulos
        ctk.CTkLabel(self.frame_disponibles, text='DISPONIBLE', text_color='white', font=('Impact', 20)).pack(pady=5)
        ctk.CTkLabel(self.frame_ocupado, text='OCUPADO', text_color='white', font=('Impact', 20)).pack(pady=5)
        ctk.CTkLabel(self.frame_mantenimiento, text='MANTENIMIENTO', text_color='white', font=('Impact', 20)).pack(pady=5)

        # Frame botones inferiores
        self.frame_botones = ctk.CTkFrame(
            self.frame_contenido,
            fg_color='#65768D',
            width=ANCHO_MONITOR / 2,
            height=ALTO_MONITOR / 10)
        self.frame_botones.pack(pady=10)

    def _crear_boton_individual(self, patente, estado_num):
        if estado_num == 1:
            frame = self.frame_disponibles
            color = "#7EC468"
        elif estado_num == 2:
            frame = self.frame_ocupado
            color = "#C96666"
        else:
            frame = self.frame_mantenimiento
            color = "#C4D2E2"

        boton = ctk.CTkButton(
            master=frame,
            text=patente,
            width=ANCHO_MONITOR / 8,
            height=ALTO_MONITOR / 15,
            fg_color=color,
            text_color="black",
            hover_color="#65768D",
            command=lambda b=patente: self.mostrar_informacion('patente', b))
        boton.pack(padx=5, pady=5)

    def _crear_boton_estados(self):
        ctk.CTkButton(
            self.frame_botones,
            text="ESTADOS",
            text_color='white',
            fg_color='#5F6977',
            font=('Impact', 30),
            command=self._abrir_ventana_patentes
        ).pack(padx=10, side='left')

    def _abrir_ventana_patentes(self):
        ventana_patentes = ctk.CTkToplevel(self.ventana)
        ventana_patentes.geometry("400x300")
        ventana_patentes.title("Seleccionar Movil")
        ventana_patentes.attributes('-topmost', True)

        ctk.CTkLabel(ventana_patentes, text="Seleccione un vehículo:", font=("Arial", 14)).pack(pady=10)

        estados_actuales = self.vehiculos_db.listar_columnas('patente', 'estado_id')
        datos_dict = {}

        for fila in estados_actuales:
            patente = fila['patente']
            estado = fila['estado_id']
            datos_dict[patente] = estado

        for patente, estado in datos_dict.items():
            if estado != ESTADOS["MANTENIMIENTO"]:
                ctk.CTkButton(
                    ventana_patentes,
                    text=patente,
                    width=200,
                    command=lambda p=patente, v=ventana_patentes: self._abrir_ventana_cambiar_estado(p, v)
                ).pack(pady=5)

    def _abrir_ventana_cambiar_estado(self, patente, ventana_anterior):
        ventana_anterior.destroy()

        ventana_estado = ctk.CTkToplevel(self.ventana)
        ventana_estado.geometry("300x150")
        ventana_estado.title(f"Cambiar estado: {patente}")

        ctk.CTkLabel(ventana_estado, text=f"Seleccione nuevo estado para {patente}", font=("Arial", 12)).pack(pady=10)

        combo = ttk.Combobox(ventana_estado, values=["DISPONIBLE", "OCUPADO"])

        estados_actuales = self.vehiculos_db.listar_columnas('patente', 'estado_id')
        datos_dict = {}

        for fila in estados_actuales:
            patente_db = fila['patente']
            estado = fila['estado_id']
            datos_dict[patente_db] = estado

        estado_actual_nombre = [nombre for nombre, num in ESTADOS.items() if num == datos_dict.get(patente, 1)][0]
        combo.set(estado_actual_nombre)
        combo.pack(pady=5)

        def guardar_estado():
            nuevo_estado_nombre = combo.get()
            nuevo_estado_num = ESTADOS[nuevo_estado_nombre]

            estado_actual = datos_dict.get(patente, 1)

            if estado_actual == 2 and nuevo_estado_num == 1:
                checklist = CheckList(self.ventana)
                km_agregados = checklist.resultado or 0
                print(km_agregados)
                self.vehiculos_db.actualizar('km_actual', km_agregados, 'patente', patente)

            self.vehiculos_db.actualizar('estado_id', nuevo_estado_num, 'patente', patente)
            self._actualizar_botones()
            ventana_estado.destroy()

        ctk.CTkButton(ventana_estado, text="Guardar", command=guardar_estado).pack(pady=10)


    def _actualizar_botones(self):
        for frame in [self.frame_disponibles, self.frame_ocupado, self.frame_mantenimiento]:
            for widget in frame.winfo_children():
                if isinstance(widget, ctk.CTkButton):
                    widget.destroy()

        estados_actuales = self.vehiculos_db.listar_columnas('patente', 'estado_id')
        for fila in estados_actuales:
            self._crear_boton_individual(fila['patente'], fila['estado_id'])

    def mostrar_informacion(self, columna, valor):
        for widget in self.frame_informacion.winfo_children():
            widget.destroy()

        datos = self.vehiculos_db.obtener_datos(columna, valor)
        if not datos:
            ctk.CTkLabel(
                self.frame_informacion,
                text="No se encontraron datos.",
                text_color="white",
                font=("Arial", 14)
            ).pack(pady=5)
            return

        for clave, valor in datos[0].items():
            if "id" in clave.lower():  
                continue

            clave_formateada = clave.replace("_", " ").capitalize()

            fila = ctk.CTkFrame(self.frame_informacion, fg_color="#6B7A8F")
            fila.pack(fill="x", padx=10, pady=2)

            ctk.CTkLabel(
                fila,
                text=f"{clave_formateada}:",
                text_color="white",
                font=("Arial", 13, "bold"),
                anchor="w",
                width=180,  
                justify="left"
            ).grid(row=0, column=0, sticky="w", padx=5, pady=2)

            ctk.CTkLabel(
                fila,
                text=str(valor),
                text_color="white",
                font=("Arial", 13),
                anchor="w",
                justify="left"
            ).grid(row=0, column=1, sticky="w", padx=5, pady=2)