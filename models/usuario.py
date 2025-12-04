from bd.conexion import ConexionBD

class Usuario:
    @staticmethod
    def autenticar(correo, password):
        db = ConexionBD().conectar()
        cursor = db.cursor(dictionary=True)

        consulta = """
            SELECT id, correo, password, rol 
            FROM usuario
            WHERE correo = %s AND password = %s
        """
        valores = (correo, password)

        cursor.execute(consulta, valores)

        usuario = cursor.fetchone()

        cursor.close()

        return usuario