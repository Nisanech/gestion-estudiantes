from bd.conexion import ConexionBD

class EstudiantePrograma:
    @staticmethod
    def asignar(est_id, prog_id):
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = "INSERT INTO estudiante_programa (estudiante_id, programa_id) VALUES (%s, %s)"
        valores = (est_id, prog_id)

        cursor.execute(consulta, valores)

        db.commit()
        cursor.close()

    @staticmethod
    def obtener_programas_de_estudiante(est_id):
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = """SELECT p.nombre_programa 
            FROM programa p
            JOIN estudiante_programa ep ON p.id = ep.programa_id
            WHERE ep.estudiante_id = %s"""
        valores = (est_id,)

        cursor.execute(consulta, valores)

        resultados = cursor.fetchall()
        cursor.close()

        return [r[0] for r in resultados]

    @staticmethod
    def filtrar_por_programa(prog_id):
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = """SELECT e.id, e.nombre, e.edad
                FROM estudiante e
                JOIN estudiante_programa ep ON e.id = ep.estudiante_id
                WHERE ep.programa_id = %s"""
        valores = (prog_id,)

        cursor.execute(consulta, valores)

        resultados = cursor.fetchall()
        cursor.close()

        return resultados