from bd.conexion import ConexionBD

class Programa:

    @staticmethod
    def listar():
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = "SELECT id, nombre_programa FROM programa"
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        cursor.close()
        return resultados