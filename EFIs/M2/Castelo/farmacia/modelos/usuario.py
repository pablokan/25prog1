from textual.app import App, ComposeResult #salida en pantalla
from textual.widgets import Input, Button, Static
import os
class Registrar_usuario(App):
    def compose(self) -> ComposeResult: #Elemento a mostrar
        #ingreso de nombre completo
        yield Static('Para regisrarse en el sistema introduzca los siguientes datos solicitados')
        yield Static('ingrese su nombre completo: ') #widget textual
        self.nombre_completo_input = Input(placeholder = 'nombre completo')
        yield self.nombre_completo_input
        #ingreso de apellido
        yield Static('ingrese su apellido completo: ') #widget textual
        self.apellido_completo_input = Input(placeholder = 'apellido completo')
        yield self.apellido_completo_input
        #ingreso de contraseña
        yield Static('Ingrese la contraseña para registrarse')
        self.contraseña_input = Input(placeholder='ingrese la contraseña')
        yield self.contraseña_input
        
        self.boton = Button('Ingresar')
        yield self.boton
        
        self.resultado = Static('')
        yield self.resultado
        
    async def on_button_pressed(self, event: Button.Pressed) -> None:
            nombre = self.nombre_completo_input.value
            apellido = self.apellido_completo_input.value
            contraseña = self.contraseña_input.value
            inicial_nombre = nombre[0]
            correo = f'{inicial_nombre + '.'}{apellido.replace(' ', '')}@farmacia.org.ar.'.lower()
            archivo = os.path.join('datos', 'usuario.txt')
            with open(archivo, 'a', encoding= 'utf-8') as file: #almacena los datos registrados
                 file.write(f'Usuario:{nombre} {apellido} \nContraseña: {contraseña} \nCorreo: {correo}\n')
            self.resultado.update(f'Datos ingresados:\nUsuario:{nombre} {apellido} \nContraseña: {contraseña} \nCorreo: {correo}')

if __name__ == '__main__':
     app = Registrar_usuario()
     app.run()

        


