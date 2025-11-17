import customtkinter as ctk
from sgif.database.crud import Vehiculo

class EditarInformacion:
    def __init__(self, info_movil, columna, valor, ventana_principal=None):
        self.ventana_principal = ventana_principal  
        info_movil.destroy()
        self.columna = columna
        self.valor = valor

        self.ventana_habilitar = ctk.CTkToplevel()  
        self.ventana_habilitar.title('Editar Movil')
        self.ventana_habilitar.geometry('400x500')
        self.ventana_habilitar.attributes("-topmost", True)
        self.ventana_habilitar.configure(fg_color="#5F6977")
        
        self.bd = Vehiculo()
        self.datos_vehiculos = self.bd.obtener_datos(self.columna, self.valor)
        
        self.frame_campos = ctk.CTkScrollableFrame(self.ventana_habilitar, width=380, height=400)
        self.frame_campos.pack(pady=10, padx=10)
        
        self.entries = {}  

        for clave, valor in self.datos_vehiculos[0].items():
            if 'id' in clave.lower():
                continue
            fila = ctk.CTkFrame(self.frame_campos, fg_color="#6B7A8F", corner_radius=8)
            fila.pack(fill="x", pady=5, padx=5)
            
            label = ctk.CTkLabel(fila, text=f"{clave.replace('_', ' ').capitalize()}:", width=140, anchor="w", text_color="white")
            label.grid(row=0, column=0, padx=5, pady=5)
            
            entry = ctk.CTkEntry(fila, placeholder_text=str(valor), fg_color="white", text_color="black")
            entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
            
            fila.grid_columnconfigure(1, weight=1)
            self.entries[clave] = entry
        
        frame_botones = ctk.CTkFrame(self.ventana_habilitar, fg_color="#65768D")
        frame_botones.pack(pady=10, padx=10, fill="x")
        
        guardar_btn = ctk.CTkButton(frame_botones, text="Guardar", command=self.guardar_cambios)
        guardar_btn.pack(side="left", padx=10, pady=10)
        
        cancelar_btn = ctk.CTkButton(frame_botones, text="Cancelar", command=self.ventana_habilitar.destroy)
        cancelar_btn.pack(side="right", padx=10, pady=10)
        
    def guardar_cambios(self):
        nuevos_valores = {clave: entry.get() for clave, entry in self.entries.items()}
        for clave, valor in nuevos_valores.items():
            if valor != '':
                self.bd.actualizar(clave, valor, 'patente', self.valor)
        
        if self.ventana_principal:
            self.ventana_principal.refrescar_pantalla()

        self.ventana_habilitar.destroy()