from models.programa import Programa


class ProgramaController:
    @staticmethod
    def listar_programas():
        programas = Programa.listar()

        if programas is None:
            return None

        return programas