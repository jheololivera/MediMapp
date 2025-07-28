from src.usuario import Usuario
from src.medico import Medico
from src.cita import CitaMedica

class SistemaCitas:
    def __init__(self):
        self.usuarios = []
        self.medicos = []
        self.citas = []
        self.contador_citas = 1

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_medicos(self):
        print("\n--- Lista de Médicos Disponibles ---")
        for i, medico in enumerate(self.medicos):
            print(f"{i + 1}. Dr. {medico.nombre} - {medico.especialidad} - Bs {medico.tarifa}")

    def reservar_cita(self, id_paciente, indice_medico, indice_horario):
        paciente = next((u for u in self.usuarios if u.id_usuario == id_paciente), None)
        if paciente is None:
            print("Paciente no encontrado.")
            return

        medico = self.medicos[indice_medico]
        if indice_horario < 0 or indice_horario >= len(medico.disponibilidad):
            print("Horario no válido.")
            return

        horario = medico.disponibilidad[indice_horario]
        cita = CitaMedica(self.contador_citas, paciente, medico, horario)
        self.citas.append(cita)
        medico.eliminar_horario(horario)
        self.contador_citas += 1

        print("¡Cita reservada!")
        cita.mostrar_cita()