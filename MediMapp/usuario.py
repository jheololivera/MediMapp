class Usuario:
    def __init__(self, id_usuario, nombre, tipo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.tipo = tipo  

    def ver_perfil(self):
        print(f"ID: {self.id_usuario}")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
