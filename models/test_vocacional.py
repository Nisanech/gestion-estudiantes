from bd.conexion import ConexionBD


class TestVocacional:
    @staticmethod
    def listar_preguntas():
        db = ConexionBD().conectar()
        cursor = db.cursor(dictionary=True)

        consulta = """
            SELECT 
                c.id AS categoria_id,
                c.nombre AS categoria_nombre,
                p.id AS pregunta_id,
                p.texto_pregunta,
                o.id AS opcion_id,
                o.texto_opcion,
                o.valor_fuzzy
            FROM categoria c
            INNER JOIN pregunta p ON p.categoria_id = c.id
            INNER JOIN opcion_respuesta o ON o.pregunta_id = p.id
            ORDER BY c.id, p.id, o.valor_fuzzy;
        """

        cursor.execute(consulta)

        resultados = cursor.fetchall()

        cursor.close()

        return resultados

