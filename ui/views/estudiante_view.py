from ui.components import AppStyles, HeaderBuilder
from ui.helpers import UIHelpers
from controllers.estudiante_controller import EstudianteController
import tkinter as tk


class EstudianteView:
    def __init__(self, root, usuario_id):
        self.root = root
        self.estudiante = usuario_id

        self.root.title("Panel Estudiante")
        self.root.geometry("1200x1000")
        self.root.configure(bg=AppStyles.BG_COLOR)

        # Configurar estilos globales
        AppStyles.estilos_notebook()

        # Construir interfaz
        self._build_ui()

    def _build_ui(self):
        HeaderBuilder.crear_encabezado(self.root, "Test Vocacional", self.estudiante, self.cerrar_sesion)

        # Contenedor principal con scroll
        main_container = tk.Frame(self.root, bg=AppStyles.BG_COLOR)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Sección de datos del estudiante
        self._crear_seccion_datos_estudiante(main_container)

    def _crear_seccion_datos_estudiante(self, contenedor_padre):
        # Obtener datos del estudiante
        datos = EstudianteController.datos_estudiante(self.estudiante['id'])

        # Desempaquetar datos
        correo, nombre, apellido, edad, genero = datos

        # Frame contenedor de la tarjeta
        card_frame = tk.Frame(contenedor_padre, bg=AppStyles.CARD_BG, relief="solid", borderwidth=1)
        card_frame.pack(fill="x", pady=(0, 20))

        # Contenedor de datos
        datos_frame = tk.Frame(card_frame, bg=AppStyles.CARD_BG)
        datos_frame.pack(fill="x", padx=20, pady=20)

        # Crear grid de información
        info_items = [
            ("Nombre Completo:", f"{nombre} {apellido}"),
            ("Correo Electrónico:", correo),
            ("Edad:", f"{edad} años"),
            ("Género:", genero)
        ]

        # Crear dos columnas
        columna_izquierda = tk.Frame(datos_frame, bg=AppStyles.CARD_BG)
        columna_izquierda.pack(side="left", fill="both", expand=True, padx=(0, 10))

        columna_derecha = tk.Frame(datos_frame, bg=AppStyles.CARD_BG)
        columna_derecha.pack(side="left", fill="both", expand=True, padx=(10, 0))

        # Distribuir items en dos columnas
        for i, (etiqueta, valor) in enumerate(info_items):
            # Determinar en qué columna va
            contenedor = columna_izquierda if i % 2 == 0 else columna_derecha

            # Frame para cada campo
            campo_frame = tk.Frame(contenedor, bg=AppStyles.CARD_BG)
            campo_frame.pack(fill="x", pady=8)

            # Etiqueta
            tk.Label(
                campo_frame,
                text=etiqueta,
                anchor="w",
                **AppStyles.estilos_label("seccion")
            ).pack(anchor="w", pady=(0, 5))

            # Valor
            tk.Label(
                campo_frame,
                text=valor,
                anchor="w",
                **AppStyles.estilos_label("normal")
            ).pack(anchor="w")

    def cerrar_sesion(self):
        UIHelpers.cerrar_sesion(self.root)
