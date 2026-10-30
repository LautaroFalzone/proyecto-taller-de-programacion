class Usuario():
    def __init__(self,nombre,edad,correo,contrasena):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.contrasena = contrasena


    def datos_completos(self):
        if self.nombre!="" and self.edad!=0 and self.correo!="" and self.contrasena!="":
            return True
        else:
            return False

    def correo_valido(self):
        if self.correo[len(self.correo)-13: len(self.correo)] == "@pioix.edu.ar":
            return True
        else:
            return False

    def nombre_valido(self):
        for caracter in self.nombre:
            if caracter in "0123456789":
                return False
        return True

    def contraseña_correcta(self,contrasena):
        if self.contrasena == contrasena:
            return True
        else:
            return False