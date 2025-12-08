"""
    Capa de controlador que gestiona la lógica de negocio relacionada con estudiantes.
"""
from types import SimpleNamespace

from controllers.usuario_controller import UsuarioController

from models.estudiante import Estudiante


class EstudianteController:
    @staticmethod
    def listar_estudiantes():
        """
            Obtiene la lista completa de estudiantes con manejo de errores.
            Decorador: @staticmethod - No requiere instancia de la clase
            Retorna:
                list[tuple]: Lista de estudiantes si tiene éxito
                None: Si ocurre algún error
            Funcionamiento:
                Llama a Estudiante.listar()
                Verifica si el resultado es None
                Retorna los estudiantes o None
        """
        estudiantes = Estudiante.listar()

        if estudiantes is None:
            return None

        return estudiantes

    @staticmethod
    def crear_estudiante(usuario_id, nombre, apellido, edad, genero):
        """
            Crea un nuevo estudiante.
            Decorador: @staticmethod - No requiere instancia de la clase
            Parámetros:
                usuario_id (int): ID del usuario
                nombre (str): Nombre del estudiante
                apellido (str): Apellido del estudiante
                edad (int): Edad del estudiante
                genero (str): Género del estudiante
            Retorna:
                tuple: (estudiante_id, None) si tiene éxito
                tuple: (None, mensaje_error) si falla
            Validaciones implementadas:
                Verifica que usuario_id exista
                Verifica que nombre y apellido no estén vacíos
            Funcionamiento:
                Valida que usuario_id no sea None
                Valida que nombre y apellido no estén vacíos
                Si pasa las validaciones, crea el estudiante
                Retorna el ID del estudiante o mensaje de error
        """
        if not usuario_id:
            return None, "El usuario es obligatorio"

        if not nombre or not apellido:
            return None, "El nombre y el apellido son obligatorios"

        estudiante_id = Estudiante.crear(usuario_id, nombre, apellido, edad, genero)

        if estudiante_id:
            return estudiante_id, None
        else:
            return None, "Error al crear el estudiante"

    @staticmethod
    def crear_estudiante_usuario(valores):
        # Extraer datos enviados desde el formulario
        datos = SimpleNamespace(**valores)

        # Crear usuario
        usuario_id, error = UsuarioController.crear_usuario(datos.correo, datos.password, datos.rol)

        if error:
            return None, error

        estudiante_id, error = EstudianteController.crear_estudiante(
            usuario_id,
            datos.nombre,
            datos.apellido,
            datos.edad,
            datos.genero
        )

        if error:
            return None, error
        return estudiante_id, None

    @staticmethod
    def datos_estudiante(est_id):
        return Estudiante.listar_por_id(est_id)
