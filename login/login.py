import os
from clases.usuario import Usuario
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from clases.usuario import Usuario

# Carga el archivo registro.kv, que está en esta misma carpeta
Builder.load_file(os.path.join(os.path.dirname(__file__), "login.kv"))


# El nombre de esta clase (RegistroScreen) es el mismo que aparece entre < > en registro.kv.
# MDScreen es la clase de KivyMD que representa una pantalla completa.
class LoginScreen(MDScreen):
    # Se ejecuta cuando en el .kv se escribe root.volver()
    # "inicio" es el nombre con el que se agregó InicioScreen en app.py.
    def volver(self):
        self.manager.current = "inicio"

    # Se ejecuta cuando en el .kv se escribe root.registrar()
    def iniciar(self):
        # Por ahora no se guarda nada: cualquier dato entra.
        # En la clase 3 acá se va a guardar el usuario nuevo.
        self.manager.current = "home"

    def login(self):
        correo = self.ids.correo.tex
        contrasena = self.ids.contrasena.text
        if usuario.contraseña_correcta(contrasena):
            print("correo inexistente")
            return
        if contrasena
