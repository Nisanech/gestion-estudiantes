"""
    Clase que representa la entidad Programa y gestiona las operaciones de consulta relacionadas con los programas académicos en la base de datos.
"""

from bd.conexion import ConexionBD

class Programa:

    @staticmethod
    def listar():
        """
            Obtiene todos los programas académicos registrados en la base de datos.
            Decorador: @staticmethod - No requiere instancia de la clase
            Retorna:
                list[tuple]: Lista de tuplas con formato (id, nombre_programa) de todos los programas
            Funcionamiento:
                Establece conexión a la base de datos mediante ConexionBD()
                Crea un cursor para ejecutar la consulta
                Ejecuta consulta SELECT para obtener todos los programas
                Recupera todos los resultados con fetchall()
                Cierra el cursor
                Retorna la lista de programas
        """
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = "SELECT id, nombre_programa FROM programa"
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        cursor.close()
        return resultados