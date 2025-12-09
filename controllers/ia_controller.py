import numpy as np

from models.ia import IA
from models.programa import Programa


class IAController:
    @staticmethod
    def calcular_recomendaciones(estudiante_id):
        # Obtener respuestas del estudiante
        respuestas = IA.obtener_respuestas_estudiante(estudiante_id)

        if not respuestas:
            return False, "El estudiante no tiene respuestas registradas"

        # Agrupar valores por categoria
        categorias = {}

        for r in respuestas:
            cat = r["categoria_id"]
            categorias.setdefault(cat, []).append(r['valor_fuzzy'])

        afinidades = {}

        # Calcular afinidad difusa por categoria
        for categoria_id, valores in categorias.items():
            nivel = IAController._calcular_afinidad_categoria(valores)
            afinidades[categoria_id] = nivel

            IA.guardar_afinidad(estudiante_id, categoria_id, nivel)

        # Calcular recomendaciones segun programas y categorias
        programas = Programa.listar()

        ranking = []

        for p in programas:
            puntaje = IAController._puntuar_programa(p, afinidades)

            ranking.append({
                "programa_id": p["id"],
                "nombre": p["nombre_programa"],
                "puntaje": puntaje
            })

            IA.guardar_recomendacion(estudiante_id, p["id"], puntaje)

        ranking.sort(key=lambda x: x["puntaje"], reverse=True)

        return True, ranking

    @staticmethod
    def _calcular_afinidad_categoria(valores):
        # Promedio difuso
        valores = np.array(valores)
        nivel = np.mean(valores) # [0,1]

        return float(nivel)

    @staticmethod
    def _puntuar_programa(programa, afinidades):
        mapa = {
            1: [1, 2],  # Ingeniería de Software
            2: [5],  # Contabilidad
            3: [6],  # Diseño gráfico
            4: [5, 4],  # Administración
            5: [1, 2],  # Sistemas de Información
            6: [6, 7],  # Marketing Digital
            7: [1]  # Ingeniería Electrónica
        }

        categorias_programa = mapa.get(programa["id"], [])

        if not categorias_programa:
            return 0

        # Puntaje = promedio de afinidad de las categorias relevantes
        puntajes = [afinidades[c] for c in categorias_programa if c in afinidades]

        return float(np.mean(puntajes))