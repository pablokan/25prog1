from ui.ventana import VentanaPrincipal

class App:
    def __init__(self):
        self.app = VentanaPrincipal()
        self.app.ventana.mainloop()

if __name__ == "__main__":
    App()