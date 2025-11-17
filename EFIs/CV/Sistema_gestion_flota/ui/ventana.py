import customtkinter as ctk
from ui.ventana_info import ANCHO_MONITOR, ALTO_MONITOR, VENTANA_ACTUAL
from ui.botones_principales import BotonesPrincipales
from ui.frames_principales.moviles import Moviles
from ui.frames_principales.agentes import Agentes
from ui.frames_principales.mantenimiento_frame import Mantenimiento

class VentanaPrincipal:
    def __init__(self):
        self.ventana = ctk.CTk(fg_color="black")
        self.ventana.title('SGIF')
        self.ventana.geometry(f'{ANCHO_MONITOR}x{ALTO_MONITOR}+0+0')

        self.frame_botones_principales = ctk.CTkFrame(
            self.ventana, width=ANCHO_MONITOR // 6, height=int(ALTO_MONITOR / 1.5), fg_color="#65768D"
        )
        self.frame_botones_principales.pack(side='left', padx=(ANCHO_MONITOR / 8, 10))
        self.frame_botones_principales.pack_propagate(False)

        BotonesPrincipales(self.frame_botones_principales, self)

        self.frame_contenido = None
        self.mostrar_contenido(VENTANA_ACTUAL)

    def mostrar_contenido(self, nombre_ventana):
        if self.frame_contenido is not None:
            self.frame_contenido.destroy()

        if nombre_ventana == 'moviles':
            self.frame_contenido = Moviles(self.ventana).frame_contenido
        elif nombre_ventana == 'agentes':
            self.frame_contenido = Agentes(self.ventana).frame_contenido
        elif nombre_ventana == 'mantenimiento':
            self.frame_contenido = Mantenimiento(self.ventana).frame_contenido