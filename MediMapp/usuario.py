class Usuario:
    def __init__(self, id_usuario, nombre, tipo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.tipo = tipo  # 'paciente' o 'medico'

    def ver_perfil(self):
        print(f"ID: {self.id_usuario}")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
