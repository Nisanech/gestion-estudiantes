"""
    Clase Singleton que gestiona la conexión a la base de datos MySQL. Garantiza que solo exista una única instancia de conexión durante la ejecución del programa.
"""

import mysql.connector
from mysql.connector import Error


class ConexionBD:
    """
        Patrón de Diseño Singleton: Implementa el patrón Singleton para asegurar una única conexión a la base de datos en toda la aplicación, optimizando recursos y evitando múltiples conexiones innecesarias.
    """
    _instance = None  # Almacena la única instancia de la clase


    def __new__(cls):
        """
            Método que controla la creación de la instancia única de la clase.
            Retorna: La única instancia de ConexionBD
            Funcionamiento:
                Verifica si ya existe una instancia de la clase
                Si no existe, crea una nueva y la almacena en _instance
                Si ya existe, retorna la instancia existente
        """
        if cls._instance is None:
            cls._instance = super(ConexionBD, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """
            Constructor de la clase que inicializa los parámetros de conexión.
            Características:
                Solo se ejecuta una vez gracias al flag _initialized
                Configura los parámetros de conexión
                Inicializa el objeto de conexión como None
        """
        if self._initialized:
            return

        # Atributos de Instancia
        self.host = 'localhost' # Dirección del servidor de base de datos
        self.user = 'root' # Usuario de MySQL
        self.password = 'root' # Contraseña del usuario
        self.database = 'estudiantes_andap' # Nombre de la base de datos
        self.connection = None # Objeto de conexión a MySQL
        self._initialized = True # Bandera para controlar la inicialización


    def conectar(self):
        """
            Establece la conexión con la base de datos MySQL.
            Retorna:
                mysql.connector.connection.MySQLConnection: Objeto de conexión si es exitoso
                None: Si ocurre un error
            Funcionamiento:
                Verifica si ya existe una conexión activa
                Si no existe o está desconectada, crea una nueva conexión
                Retorna el objeto de conexión
            Manejo de Errores:
                Captura excepciones de tipo mysql.connector.Error
                Imprime mensaje de error
                Retorna None en caso de error
        """
        try:
            if self.connection is None or not self.connection.is_connected():
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
                print("🥸 Conectado a la base de datos")
            return self.connection

        except Error as e:
            print(f"👻 Error al conectar a la base de datos: {e}")
            return None


    def desconectar(self):
        """
            Cierra la conexión con la base de datos si está activa.
            Retorna: None
            Funcionamiento:
                Verifica que exista una conexión y que esté activa
                Cierra la conexión
                Imprime mensaje de confirmación
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("📛 Desconectado de la base de datos")