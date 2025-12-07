from types import SimpleNamespace

from models.programa import Programa


class ProgramaController:
    @staticmethod
    def listar_programas():
        programas = Programa.listar()

        if programas is None:
            return None

        return programas

    @staticmethod
    def crear_programa(valores):
        print(valores)
        # Datos enviados desde el formulario
        datos = SimpleNamespace(**valores)

        if not datos.nombre_programa or not datos.descripcion:
            return None, "Todos los campos son obligatorios"

        # Crear programa
        programa_id = Programa.crear(datos.nombre_programa, datos.descripcion)

        if programa_id:
            return programa_id, None
        else:
            return None, "Error al crear el programa"