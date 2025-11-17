import customtkinter as ctk

class CheckList:
    def __init__(self, master=None):
        self.resultado = None  
        self.ventana_check = ctk.CTkToplevel(master)
        self.ventana_check.geometry("400x350")
        self.ventana_check.title("Check List")
        self.ventana_check.attributes('-topmost', True)
        self.ventana_check.grab_set()  

        ctk.CTkLabel(self.ventana_check, text="CHECK LIST", font=('Impact', 25)).pack(pady=10)
        ctk.CTkLabel(self.ventana_check, text="Kilómetros recorridos:", text_color="white").pack(pady=5)

        self.km_entry = ctk.CTkEntry(self.ventana_check, width=200)
        self.km_entry.pack(pady=10)

        ctk.CTkButton(
            self.ventana_check,
            text="Guardar",
            fg_color="#5F6977",
            command=self.guardar
        ).pack(pady=15)

        self.ventana_check.wait_window()

    def guardar(self):
        try:
            km = float(self.km_entry.get())
        except ValueError:
            km = 0  
        self.resultado = km
        self.ventana_check.destroy()
