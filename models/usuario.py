"""
    Clase que gestiona la autenticación y registro de usuarios del sistema. Maneja las operaciones CRUD relacionadas con la tabla usuario.
"""

from bd.conexion import ConexionBD

class Usuario:
    @staticmethod
    def autenticar(correo, password):
        """
            Valida las credenciales de un usuario y retorna su información si son correctas.
            Decorador: @staticmethod - No requiere instancia de la clase
            Parámetros:
                correo (str): Correo electrónico del usuario
                password (str): Contraseña del usuario
            Retorna:
                dict: Diccionario con datos del usuario si las credenciales son válidas
                    Formato: {'id': int, 'correo': str, 'password': str, 'rol': str}
                None: Si las credenciales son incorrectas
            Funcionamiento:
                Establece conexión a la base de datos
                Crea un cursor con dictionary=True para obtener resultados como diccionarios
                Ejecuta consulta SELECT con filtro por correo y contraseña
                Recupera el primer resultado con fetchone()
                Cierra el cursor
                Retorna el usuario o None
        """
        db = ConexionBD().conectar()
        cursor = db.cursor(dictionary=True)

        consulta = """
            SELECT id, correo, password, rol 
            FROM usuario
            WHERE correo = %s AND password = %s
        """
        valores = (correo, password)

        cursor.execute(consulta, valores)

        usuario = cursor.fetchone()

        cursor.close()

        return usuario

    @staticmethod
    def existe_correo(correo):
        """
            Verifica si un correo electrónico ya está registrado en el sistema.
            Decorador: @staticmethod - No requiere instancia de la clase
            Parámetros:
                correo (str): Correo electrónico a verificar
            Retorna:
                bool: True si el correo existe, False si no existe
            Funcionamiento:
                Establece conexión a la base de datos
                Crea un cursor con dictionary=True
                Ejecuta consulta SELECT buscando el correo
                Recupera el resultado con fetchone()
                Cierra el cursor
                Retorna True si existe, False si no
        """
        db = ConexionBD().conectar()
        cursor = db.cursor(dictionary=True)

        consulta = "SELECT id FROM usuario WHERE correo = %s"

        cursor.execute(consulta, (correo,))

        existe = cursor.fetchone()

        cursor.close()

        return existe is not None

    @staticmethod
    def crear(correo, password, rol):
        """
            Crea un nuevo usuario en el sistema.
            Decorador: @staticmethod - No requiere instancia de la clase
            Parámetros:
                correo (str): Correo electrónico del usuario
                password (str): Contraseña del usuario
                rol (str): Rol del usuario en el sistema
            Retorna:
                int: ID del usuario recién creado (autoincremental de la BD)
            Funcionamiento:
                Establece conexión a la base de datos
                Crea un cursor
                Prepara la consulta INSERT con parámetros
                Ejecuta la inserción con los valores proporcionados
                Confirma la transacción con commit()
                Obtiene el ID generado automáticamente con lastrowid
                Cierra el cursor
                Retorna el ID del nuevo usuario
        """
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = "INSERT INTO usuario (correo, password, rol) VALUES (%s, %s, %s)"
        valores = (correo, password, rol)

        cursor.execute(consulta, valores)
        db.commit()

        usuario_id = cursor.lastrowid

        cursor.close()

        return usuario_id