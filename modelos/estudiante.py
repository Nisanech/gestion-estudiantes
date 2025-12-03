from bd.conexion import ConexionBD

class Estudiante:
    def __init__(self, id=None, nombre=None, edad=None):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.db = ConexionBD().conectar()


    # Crear nuevo estudiante
    def crear(self):
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
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = "SELECT id, nombre, edad FROM estudiante WHERE id = %s"
        cursor.execute(consulta, (est_id,))

        resultado = cursor.fetchone()

        cursor.close()
        return resultado
        
        



 
    
























