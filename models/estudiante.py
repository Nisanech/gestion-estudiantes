"""
    Clase que representa la entidad Estudiante y gestiona todas las operaciones CRUD (Crear, Leer) relacionadas con estudiantes en la base de datos.
"""

from bd.conexion import ConexionBD


class Estudiante:
    # Crear nuevo estudiante
    @staticmethod
    def crear(usuario_id, nombre, apellido, edad, genero):
        """
            Crea un nuevo estudiante vinculado a un usuario existente.
            Decorador: @staticmethod - No requiere instancia de la clase
            Parámetros:
                usuario_id (int): ID del usuario al que pertenece el estudiante
                nombre (str): Nombre del estudiante
                apellido (str): Apellido del estudiante
                edad (int): Edad del estudiante
                genero (str): Género del estudiante
            Retorna:
                int: ID del estudiante recién creado
            Funcionamiento:
                Establece conexión a la base de datos
                Crea un cursor
                Prepara consulta INSERT con los datos del estudiante
                Ejecuta la inserción
                Confirma la transacción
                Obtiene el ID generado automáticamente
                Cierra el cursor
                Retorna el ID del estudiante
        """
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = """
            INSERT INTO estudiante (usuario_id, nombre, apellido, edad, genero) 
            VALUES (%s, %s, %s, %s, %s)"""
        valores = (usuario_id, nombre, apellido, edad, genero)

        cursor.execute(consulta, valores)

        db.commit()

        estudiante_id = cursor.lastrowid

        cursor.close()

        return estudiante_id

    # Listar todos los estudiantes
    @staticmethod
    def listar():
        """
            Obtiene todos los estudiantes con información de sus usuarios mediante JOIN.
            Decorador: @staticmethod - No requiere instancia de la clase
            Retorna:
                list[tuple]: Lista de tuplas con formato (correo, nombre, apellido, edad, genero)
            Funcionamiento:
                Establece conexión a la base de datos
                Crea un cursor
                Ejecuta consulta SELECT con INNER JOIN
                Recupera todos los resultados
                Cierra el cursor
                Retorna la lista de estudiantes
        """
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = """
            SELECT u.correo, e.nombre, e.apellido, e.edad, e.genero 
            FROM estudiante e
            INNER JOIN usuario u ON u.id = e.usuario_id
        """

        cursor.execute(consulta)

        resultados = cursor.fetchall()

        cursor.close()

        return resultados

    # Listar estudiantes mayores de 18
    @staticmethod
    def listar_mayores_18():
        """
            Obtiene todos los estudiantes mayores de 18 años.
            Decorador: @staticmethod - No requiere instancia de la clase
            Retorna:
                list[tuple]: Lista de tuplas con formato (id, nombre, edad) de estudiantes mayores de 18 años
            Funcionamiento:
                Establece conexión a la base de datos
                Crea un cursor
                Ejecuta consulta SELECT con filtro WHERE edad > 18
                Recupera todos los resultados con fetchall()
                Cierra el cursor
                Retorna la lista de estudiantes filtrados
        """
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = "SELECT id, nombre, edad FROM estudiante WHERE edad > 18"
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        cursor.close()
        return resultados

    # Listar estudiantes por id
    @staticmethod
    def listar_por_id(est_id):
        """
            Busca y retorna un estudiante específico por su ID.
            Decorador: @staticmethod - No requiere instancia de la clase
            Parámetros: est_id (int): ID del estudiante a buscar
            Retorna:
                tuple: Tupla con formato (id, nombre, edad) si encuentra el estudiante
                None: Si no existe un estudiante con ese ID
            Funcionamiento:
                Establece conexión a la base de datos
                Crea un cursor
                Ejecuta consulta SELECT con filtro WHERE id = est_id
                Recupera un solo resultado con fetchone()
                Cierra el cursor
                Retorna el estudiante o None
        """
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = "SELECT id, nombre, edad FROM estudiante WHERE id = %s"
        cursor.execute(consulta, (est_id,))

        resultado = cursor.fetchone()

        cursor.close()
        return resultado
