class Medico:
    def __init__(self, id_medico, nombre, especialidad, tarifa, disponibilidad):
        self.id_medico = id_medico
        self.nombre = nombre
        self.especialidad = especialidad
        self.tarifa = tarifa
        self.disponibilidad = disponibilidad 

    def mostrar_disponibilidad(self):
        print(f"\nDisponibilidad del Dr. {self.nombre}:")
        for i, horario in enumerate(self.disponibilidad):
            print(f"{i + 1}. {horario}")

    def eliminar_horario(self, horario):
        if horario in self.disponibilidad:
            self.disponibilidad.remove(horario)