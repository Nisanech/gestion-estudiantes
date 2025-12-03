"""
    Clase que representa la entidad Estudiante y gestiona todas las operaciones CRUD (Crear, Leer) relacionadas con estudiantes en la base de datos.
"""

from bd.conexion import ConexionBD


class Estudiante:
    def __init__(self, id=None, nombre=None, edad=None):
        """
            Constructor de la clase que inicializa un objeto Estudiante.
            Funcionamiento:
                Inicializa los atributos del estudiante
                Establece automáticamente la conexión a la base de datos mediante ConexionBD()
        """

        # Atributos de Instancia
        self.id = id  # Identificador único del estudiante (autoincremental)
        self.nombre = nombre  # Nombre completo del estudiante
        self.edad = edad  # Edad del estudiante
        self.db = ConexionBD().conectar()  # Conexión activa a la base de datos

    # Crear nuevo estudiante
    def crear(self):
        """
            Inserta un nuevo estudiante en la base de datos.
            Retorna:
                int: ID del estudiante recién creado (autoincremental de la base de datos)
            Funcionamiento:
                Crea un cursor para ejecutar la consulta
                Prepara la consulta INSERT con parámetros
                Ejecuta la consulta con los valores del estudiante
                Confirma la transacción con commit()
                Obtiene el ID generado automáticamente
                Cierra el cursor
                Retorna el ID del nuevo estudiante
        """
        cursor = self.db.cursor()

        consulta = "INSERT INTO estudiante (nombre, edad) VALUES (%s, %s)"
        valores = (self.nombre, self.edad)

        cursor.execute(consulta, valores)

        self.db.commit()
        self.id = cursor.lastrowid

        cursor.close()

        return self.id

    # Listar todos los estudiantes
    @staticmethod
    def listar():
        """
            Obtiene todos los estudiantes registrados en la base de datos.
            Decorador: @staticmethod - No requiere instancia de la clase
            Retorna:
                list[tuple]: Lista de tuplas con formato (id, nombre, edad) de todos los estudiantes
            Funcionamiento:
                Establece conexión a la base de datos
                Crea un cursor
                Ejecuta consulta SELECT para obtener todos los registros
                Recupera todos los resultados con fetchall()
                Cierra el cursor
                Retorna la lista de estudiantes
        """
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = "SELECT id, nombre, edad FROM estudiante"
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
