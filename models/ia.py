from bd.conexion import ConexionBD


class IA:
    @staticmethod
    def obtener_respuestas_estudiante(estudiante_id):
        db = ConexionBD().conectar()
        cursor = db.cursor(dictionary=True)

        consulta = """
            SELECT r.pregunta_id, r.valor_fuzzy, p.categoria_id
            FROM respuesta_estudiante r
            INNER JOIN pregunta p ON r.pregunta_id = p.id
            WHERE r.estudiante_id = %s
        """

        cursor.execute(consulta, (estudiante_id,))

        resultados = cursor.fetchall()

        cursor.close()

        return resultados

    @staticmethod
    def guardar_afinidad(estudiante_id, categoria_id, nivel_fuzzy):
        db = ConexionBD().conectar()
        cursor = db.cursor()

        # Verificar si ya existe un registro
        consulta_existente = """
            SELECT id FROM afinidad_difusa
            WHERE estudiante_id = %s AND categoria_id = %s
        """

        cursor.execute(consulta_existente, (estudiante_id, categoria_id))

        existe = cursor.fetchone()

        if existe:
            consulta = """
                UPDATE afinidad_difusa
                SET nivel_fuzzy = %s
                WHERE estudiante_id = %s AND categoria_id = %s
            """

            valores = (nivel_fuzzy, estudiante_id, categoria_id)

        else:
            consulta = """
                INSERT INTO afinidad_difusa (estudiante_id, categoria_id, nivel_fuzzy)
                VALUES (%s, %s, %s)
            """

            valores = (estudiante_id, categoria_id, nivel_fuzzy)

        cursor.execute(consulta, valores)

        db.commit()

        cursor.close()

    @staticmethod
    def guardar_recomendacion(estudiante_id, programa_id, puntaje):
        db = ConexionBD().conectar()
        cursor = db.cursor()

        # Verificar si ya existe un registro
        consulta_existente = """
            SELECT id FROM recomendacion_programa
            WHERE estudiante_id = %s AND programa_id = %s
        """

        cursor.execute(consulta_existente, (estudiante_id, programa_id))

        existe = cursor.fetchone()

        if existe:
            consulta = """
                UPDATE recomendacion_programa
                SET puntaje = %s
                WHERE estudiante_id = %s AND programa_id = %s
            """

            valores = (puntaje, estudiante_id, programa_id)
        else:
            consulta = """
                INSERT INTO recomendacion_programa (estudiante_id, programa_id, puntaje)
                VALUES (%s, %s, %s)
            """

            valores = (estudiante_id, programa_id, puntaje)

        cursor.execute(consulta, valores)

        db.commit()

        cursor.close()