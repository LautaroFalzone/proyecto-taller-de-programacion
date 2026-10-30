import os

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from clases.usuario import Usuario
# Carga el archivo registro.kv, que está en esta misma carpeta
Builder.load_file(os.path.join(os.path.dirname(__file__), "registro.kv"))


# El nombre de esta clase (RegistroScreen) es el mismo que aparece entre < > en registro.kv.
# MDScreen es la clase de KivyMD que representa una pantalla completa.
class RegistroScreen(MDScreen):
    # Se ejecuta cuando en el .kv se escribe root.volver()
    # "inicio" es el nombre con el que se agregó InicioScreen en app.py.
    def volver(self):
        self.manager.current = "inicio"

    # Se ejecuta cuando en el .kv se escribe root.registrar()
    def registrar(self):
        app = MDApp.get_running_app()
        # Por ahora no se guarda nada: cualquier dato entra.
        # En la clase 3 acá se va a guardar el usuario nuevo.
        #Crear un obj usuario
        usuario1 = Usuario(self.ids.nombre.text,self.ids.edad.text,self.ids.correo.text,self.ids.contrasena.text)
        if usuario1.datos_completos() == False:
            print("complete los datos")
            return 

        if usuario1.correo_valido() == False:
            print("el correo esta mal escrito boludo")
            return

        if usuario1.nombre_valido() == False:
            print("nombre invalido")
            return 

        if usuario1.datos_completos() and usuario1.correo_valido() and usuario1.nombre_valido() == True:
            app.lista.append(usuario1)
        
        #si usuario correcto: agregar a la lista


        self.manager.current = "login"
