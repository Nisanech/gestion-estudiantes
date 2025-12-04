from models.estudiante import Estudiante


class EstudianteController:
    @staticmethod
    def listar_estudiantes():
        estudiantes = Estudiante.listar()

        if estudiantes is None:
            return None

        return estudiantes