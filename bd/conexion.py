import mysql.connector
from mysql.connector import Error


class ConexionBD:
    _instance = None  # Crear una unica instancia para la clase

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConexionBD, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """ Constructor de la clase """
        if self._initialized:
            return

        self.host = 'localhost'
        self.user = 'root'
        self.password = 'root'
        self.database = 'estudiantes_andap'
        self.connection = None
        self._initialized = True

    def conectar(self):
        """ Conectar a la base de datos """
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
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("📛 Desconectado de la base de datos")