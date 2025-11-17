import customtkinter as ctk
from ui.ventana_info import ANCHO_MONITOR, ALTO_MONITOR

class Agentes():
    def __init__(self, ventana):
        self.ventana = ventana

        self.frame_contenido = ctk.CTkFrame(self.ventana ,width=ANCHO_MONITOR / 1.7, height= ALTO_MONITOR / 1.5, fg_color='#65768D')
        self.frame_contenido.pack(side='left')
        self.frame_contenido.pack_propagate(False)