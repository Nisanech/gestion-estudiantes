"""
    Capa de controlador que gestiona la lógica de negocio relacionada con usuarios. Implementa validaciones y orquesta las operaciones del modelo Usuario.
"""

from models.usuario import Usuario

class UsuarioController:
    @staticmethod
    def crear_usuario(correo, password, rol):
        """
            Crea un nuevo usuario con validaciones de negocio.
            Decorador: @staticmethod - No requiere instancia de la clase
            Parámetros:
                correo (str): Correo electrónico del usuario
                password (str): Contraseña del usuario
                rol (str): Rol del usuario
            Retorna:
                tuple: (usuario_id, None) si tiene éxito
                tuple: (None, mensaje_error) si falla
            Validaciones implementadas:
                Verifica que correo y contraseña no estén vacíos
                Verifica que el correo no esté ya registrado
            Funcionamiento:
                Valida que correo y password no sean vacíos
                Verifica si el correo ya existe usando Usuario.existe_correo()
                Si pasa las validaciones, crea el usuario con Usuario.crear()
                Retorna el ID del usuario creado o un mensaje de error
        """
        if not correo or not password:
            return None, "El correo y la contraseña son obligatorios"

        if Usuario.existe_correo(correo):
            return None, "El correo ya está registrado"

        usuario_id = Usuario.crear(correo, password, rol)

        if usuario_id:
            return usuario_id, None
        else:
            return None, "Error al crear el usuario"
