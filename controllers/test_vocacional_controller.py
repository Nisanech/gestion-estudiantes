from models.respuesta_estudiante import RespuestaEstudiante
from models.test_vocacional import TestVocacional


class TestVocacionalController:
    @staticmethod
    def listar_preguntas_categorias():
        filas = TestVocacional.listar_preguntas()
        categorias = {}

        for fila in filas:
            categoria_id = fila["categoria_id"]

            if categoria_id not in categorias:
                categorias[categoria_id] = {
                    "nombre": fila["categoria_nombre"],
                    "preguntas": {}
                }

            pregunta_id = fila["pregunta_id"]

            if pregunta_id not in categorias[categoria_id]["preguntas"]:
                categorias[categoria_id]["preguntas"][pregunta_id] = {
                    "id": pregunta_id,
                    "texto": fila["texto_pregunta"],
                    "opciones": []
                }

            categorias[categoria_id]["preguntas"][pregunta_id]["opciones"].append({
                "id": fila["opcion_id"],
                "texto": fila["texto_opcion"],
                "valor": float(fila["valor_fuzzy"])
            })

        resultado_final = {
            "categorias": []
        }

        for categoria in categorias.values():
            resultado_final["categorias"].append({
                "nombre": categoria["nombre"],
                "preguntas": list(categoria["preguntas"].values())
            })

        return resultado_final

    @staticmethod
    def guardar_respuestas(estudiante_id, respuestas):
        try:
            errores = []

            for item in respuestas:
                pregunta_id = item.get("pregunta_id")
                opcion_id = item.get("opcion_id")
                valor = item.get("valor_fuzzy")

                if pregunta_id is None or opcion_id is None or valor is None:
                    errores.append(f"Datos incompletos en {item}")
                    continue

                try:
                    RespuestaEstudiante.guardar_respuesta(
                        estudiante_id,
                        pregunta_id,
                        opcion_id,
                        valor
                    )
                except Exception as e:
                    errores.append(f"Error al guardar pregunta {pregunta_id}: {str(e)}")

            if errores:
                return False, errores

            return True, None

        except Exception as e:
            return False, str(e)