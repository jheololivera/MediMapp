from src.usuario import Usuario
from src.medico import Medico
from src.sistema import SistemaCitas

def main():
    sistema = SistemaCitas()

    paciente1 = Usuario(1, "Juan Pérez", "paciente")
    sistema.agregar_usuario(paciente1)

    medico1 = Medico(101, "Carlos Flores", "Cardiología", 150, ["2025-08-01 10:00", "2025-08-01 15:00"])
    medico2 = Medico(102, "Laura Méndez", "Dermatología", 120, ["2025-08-02 11:00", "2025-08-02 16:00"])
    sistema.agregar_medico(medico1)
    sistema.agregar_medico(medico2)

    print("Bienvenido a MediMapp – Reservar Cita Médica")

    while True:
        print("\nSeleccione una opción:")
        print("1. Ver médicos disponibles")
        print("2. Reservar una cita")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            sistema.mostrar_medicos()

        elif opcion == "2":
            sistema.mostrar_medicos()
            try:
                indice_medico = int(input("Ingrese el número del médico: ")) - 1
                if indice_medico < 0 or indice_medico >= len(sistema.medicos):
                    print("Médico no válido.")
                    continue

                sistema.medicos[indice_medico].mostrar_disponibilidad()
                indice_horario = int(input("Seleccione el horario disponible: ")) - 1

                sistema.reservar_cita(paciente1.id_usuario, indice_medico, indice_horario)

            except ValueError:
                print("Entrada inválida. Intente de nuevo.")

        elif opcion == "3":
            print("¡Gracias por usar MediMapp!")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()