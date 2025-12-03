"""
    Clase que gestiona la relación muchos a muchos entre estudiantes y programas académicos. Permite asignar estudiantes a programas y realizar consultas sobre estas relaciones.
"""

from bd.conexion import ConexionBD

class EstudiantePrograma:
    @staticmethod
    def asignar(est_id, prog_id):
        """
            Asigna un estudiante a un programa académico específico, creando la relación en la tabla intermedia.
            Decorador: @staticmethod - No requiere instancia de la clase
            Parámetros:
                est_id (int): ID del estudiante a asignar
                prog_id (int): ID del programa al que se asignará el estudiante
            Retorna: None
            Funcionamiento:
                Establece conexión a la base de datos
                Crea un cursor
                Prepara consulta INSERT con parámetros
                Ejecuta la inserción con los IDs proporcionados
                Confirma la transacción con commit()
                Cierra el cursor
        """
        db = ConexionBD().conectar()
        cursor = db.cursor()

        consulta = "INSERT INTO estudiante_programa (estudiante_id, programa_id) VALUES (%s, %s)"
        valores = (est_id, prog_id)

        cursor.execute(consulta, valores)

        db.commit()
        cursor.close()


    @staticmethod
    def obtener_programas_de_estudiante(est_id):
        """
            Obtiene todos los programas académicos a los que está inscrito un estudiante específico.
            Decorador: @staticmethod - No requiere instancia de la clase
            Parámetros:
                est_id (int): ID del estudiante
            Retorna:
                list[str]: Lista con los nombres de los programas del estudiante
            Funcionamiento:
                Establece conexión a la base de datos
                Crea un cursor
                Ejecuta consulta JOIN entre las tablas programa y estudiante_programa
                Filtra por el ID del estudiante
                Recupera todos los resultados
                Cierra el cursor
                Transforma las tuplas en una lista de strings (nombres de programas)
        """
        db = ConexionBD().conectar()
        cursor = db.cursor()

        """
            Ejemplo flujo de consulta:
                1. Busca en estudiante_programa todos los registros donde estudiante_id = 5
                    Encuentra: programa_id = 1 y programa_id = 3
                2. Hace JOIN con programa para obtener los nombres completos
                    programa_id = 1 → "Ingeniería de Sistemas"
                    programa_id = 3 → "Derecho"
                3. Retorna solo los nombres de los programas (no los IDs)
        """
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
        """
            Obtiene todos los estudiantes inscritos en un programa académico específico.
            Decorador: @staticmethod - No requiere instancia de la clase
            Parámetros:
                prog_id (int): ID del programa
            Retorna:
                list[tuple]: Lista de tuplas con formato (id, nombre, edad) de los estudiantes
            Funcionamiento:
                Establece conexión a la base de datos
                Crea un cursor
                Ejecuta consulta JOIN entre las tablas estudiante y estudiante_programa
                Filtra por el ID del programa
                Recupera todos los resultados con información completa del estudiante
                Cierra el cursor
                Retorna la lista de estudiantes
        """
        db = ConexionBD().conectar()
        cursor = db.cursor()

        """
            Ejemplo flujo de consulta:
                1. Busca en estudiante_programa todos los registros donde programa_id = 1
                    Encuentra: estudiante_id = 5, estudiante_id = 8, estudiante_id = 12
                2. Hace JOIN con estudiante para obtener la información completa de cada estudiante
                    estudiante_id = 5 → (id=5, nombre="Juan Pérez", edad=20)
                    estudiante_id = 8 → (id=8, nombre="Ana López", edad=21)
                    estudiante_id = 12 → (id=12, nombre="Carlos Ruiz", edad=19)
                3. Retorna el ID, nombre y edad de todos los estudiantes inscritos en ese programa
        """
        consulta = """SELECT e.id, e.nombre, e.edad
                FROM estudiante e
                JOIN estudiante_programa ep ON e.id = ep.estudiante_id
                WHERE ep.programa_id = %s"""
        valores = (prog_id,)

        cursor.execute(consulta, valores)

        resultados = cursor.fetchall()
        cursor.close()

        return resultados