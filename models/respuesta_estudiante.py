from bd.conexion import ConexionBD


class RespuestaEstudiante:
    @staticmethod
    def guardar_respuesta(estudiante_id, pregunta_id, opcion_id, valor_fuzzy):
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta_existente = """
            SELECT id FROM respuesta_estudiante
            WHERE estudiante_id = %s AND pregunta_id = %s
        """

        cursor.execute(consulta_existente, (estudiante_id, pregunta_id))
        existe = cursor.fetchone()

        if existe:
            consulta = """
                UPDATE respuesta_estudiante
                SET opcion_id = %s, valor_fuzzy = %s
                WHERE estudiante_id = %s AND pregunta_id = %s
            """

            valores = (opcion_id, valor_fuzzy, estudiante_id, pregunta_id)
        else:
            consulta = """
                INSERT INTO respuesta_estudiante 
                (estudiante_id, pregunta_id, opcion_id, valor_fuzzy)
                VALUES (%s, %s, %s, %s)
            """

            valores = (estudiante_id, pregunta_id, opcion_id, valor_fuzzy)

        cursor.execute(consulta, valores)

        db.commit()

        cursor.close()

        return True