class CitaMedica:
    def __init__(self, id_cita, paciente, medico, horario):
        self.id_cita = id_cita
        self.paciente = paciente 
        self.medico = medico     
        self.horario = horario
        self.estado = "Confirmada"

    def mostrar_cita(self):
        print("\n--- Cita Confirmada ---")
        print(f"ID Cita: {self.id_cita}")
        print(f"Paciente: {self.paciente.nombre}")
        print(f"Médico: Dr. {self.medico.nombre} ({self.medico.especialidad})")
        print(f"Horario: {self.horario}")
        print(f"Estado: {self.estado}")