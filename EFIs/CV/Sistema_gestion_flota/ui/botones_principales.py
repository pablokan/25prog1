import customtkinter as ctk
from ui.ventana_info import ALTO_BOTONES_PRINCIPALES, ANCHO_BOTONES_PRINCIPALES

class BotonesPrincipales:
    def __init__(self, contenedor, ventana_principal):
        self.contenedor = contenedor
        self.ventana_principal = ventana_principal 

        self.boton_moviles = ctk.CTkButton(
            contenedor,
            text='Móviles',
            fg_color='white',
            width=ANCHO_BOTONES_PRINCIPALES,
            height=ALTO_BOTONES_PRINCIPALES,
            font=('Impact', 20),
            text_color='black',
            hover_color='#5F6977',
            command=lambda: self.actualizar_pantalla('moviles')
        )
        self.boton_moviles.pack(anchor='center', pady=(ALTO_BOTONES_PRINCIPALES / 1.5, 5))

        self.boton_agentes = ctk.CTkButton(
            contenedor,
            text='Agentes',
            fg_color='white',
            width=ANCHO_BOTONES_PRINCIPALES,
            height=ALTO_BOTONES_PRINCIPALES,
            font=('Impact', 20),
            text_color="#000000",
            hover_color='#5F6977',
            command=lambda: self.actualizar_pantalla('agentes')
        )
        self.boton_agentes.pack(anchor='center', pady=(ALTO_BOTONES_PRINCIPALES / 1.5, 5))

        self.boton_mantenimiento = ctk.CTkButton(
            contenedor,
            text='Mantenimiento',
            fg_color='white',
            width=ANCHO_BOTONES_PRINCIPALES,
            height=ALTO_BOTONES_PRINCIPALES,
            font=('Impact', 20),
            text_color='black',
            hover_color='#5F6977',
            command=lambda: self.actualizar_pantalla('mantenimiento'))
        self.boton_mantenimiento.pack(anchor='center', pady=(ALTO_BOTONES_PRINCIPALES / 1.5, 5))
    
    def actualizar_pantalla(self, actual):
        self.ventana_principal.mostrar_contenido(actual)