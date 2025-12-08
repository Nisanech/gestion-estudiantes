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