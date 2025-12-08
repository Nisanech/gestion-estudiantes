from controllers.test_vocacional_controller import TestVocacionalController
from ui.components import AppStyles, HeaderBuilder
from ui.helpers import UIHelpers
from controllers.estudiante_controller import EstudianteController
import tkinter as tk
from tkinter import ttk


class EstudianteView:
    def __init__(self, root, usuario_id):
        self.root = root
        self.estudiante = usuario_id
        self.respuestas = {}  # Almacenar respuestas del test

        self.root.title("Panel Estudiante")
        self.root.geometry("1200x1000")
        self.root.configure(bg=AppStyles.BG_COLOR)

        # Configurar estilos globales
        AppStyles.estilos_notebook()

        # Construir interfaz
        self._build_ui()

    def _build_ui(self):
        HeaderBuilder.crear_encabezado(self.root, "Test Vocacional", self.estudiante, self.cerrar_sesion)

        # Contenedor principal
        main_container = tk.Frame(self.root, bg=AppStyles.BG_COLOR)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Sección de datos del estudiante
        self._crear_seccion_datos_estudiante(main_container)

        # Crear tabs
        self._crear_tabs(main_container)

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

    def _crear_tabs(self, contenedor_padre):
        # Notebook con pestañas
        notebook = ttk.Notebook(contenedor_padre, style="Custom.TNotebook")
        notebook.pack(fill="both", expand=True)

        # Crear tabs
        self._crear_tab_test(notebook)
        self._crear_tab_resultados(notebook)

    def _crear_tab_test(self, notebook):
        """Crea la pestaña del Test Vocacional"""
        tab = tk.Frame(notebook, bg=AppStyles.CARD_BG)
        notebook.add(tab, text="📝 Test")

        # Canvas con scrollbar para el formulario
        canvas = tk.Canvas(tab, bg=AppStyles.CARD_BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=AppStyles.CARD_BG)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Instrucciones
        instrucciones_frame = tk.Frame(scrollable_frame, bg=AppStyles.CARD_BG)
        instrucciones_frame.pack(fill="x", padx=20, pady=(0, 20))

        # Obtener estructura del test
        test_data = TestVocacionalController.listar_preguntas_categorias()

        # Crear preguntas por categoría
        for categoria in test_data["categorias"]:
            self._crear_categoria(scrollable_frame, categoria)

        # Botón de enviar
        btn_frame = tk.Frame(scrollable_frame, bg=AppStyles.CARD_BG)
        btn_frame.pack(fill="x", padx=20, pady=20)

        tk.Button(
            btn_frame,
            text="Enviar Test",
            command=self.enviar_test,
            **AppStyles.estilos_button("primary")
        ).pack(side="left")

        # Empaquetar canvas y scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Habilitar scroll con rueda del mouse
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def _crear_categoria(self, contenedor, categoria):
        # Frame de categoría
        categoria_frame = tk.Frame(contenedor, bg=AppStyles.CARD_BG)
        categoria_frame.pack(fill="x", padx=20, pady=(0, 20))

        # Título de categoría
        tk.Label(
            categoria_frame,
            text=categoria["nombre"],
            font=(AppStyles.FONT_FAMILY, 12, "bold"),
            fg=AppStyles.PRIMARY_COLOR,
            bg=AppStyles.CARD_BG,
            anchor="w"
        ).pack(fill="x", pady=(0, 15))

        # Crear cada pregunta
        for pregunta in categoria["preguntas"]:
            self._crear_pregunta_radio(categoria_frame, pregunta)

    def _crear_pregunta_radio(self, contenedor, pregunta):
        """Crea una pregunta con radio buttons"""
        pregunta_id = pregunta["id"]
        texto_pregunta = pregunta["texto"]
        opciones = pregunta["opciones"]

        # Frame de la pregunta
        pregunta_frame = tk.Frame(contenedor, bg=AppStyles.CARD_BG)
        pregunta_frame.pack(fill="x", pady=(0, 20))

        # Texto de la pregunta
        tk.Label(
            pregunta_frame,
            text=f"{pregunta_id}. {texto_pregunta}",
            font=(AppStyles.FONT_FAMILY, 10),
            fg=AppStyles.TEXT_COLOR,
            bg=AppStyles.CARD_BG,
            wraplength=900,
            justify="left",
            anchor="w"
        ).pack(fill="x", pady=(0, 10))

        # Frame para las opciones
        opciones_frame = tk.Frame(pregunta_frame, bg=AppStyles.CARD_BG)
        opciones_frame.pack(fill="x", padx=20)

        # Variables para la respuesta:
        var_fuzzy = tk.DoubleVar(value=-1)
        var_opcion = tk.IntVar(value=-1)

        # Guardamos ambas variables
        self.respuestas[f"pregunta_{pregunta_id}"] = {
            "var_fuzzy": var_fuzzy,
            "var_opcion": var_opcion
        }

        # Crear radio buttons
        for opcion in opciones:
            rb = tk.Radiobutton(
                opciones_frame,
                text=opcion['texto'],
                variable=var_fuzzy,
                value=opcion['valor'],
                font=(AppStyles.FONT_FAMILY, 9),
                fg=AppStyles.TEXT_COLOR,
                bg=AppStyles.CARD_BG,
                activebackground=AppStyles.CARD_BG,
                selectcolor=AppStyles.CARD_BG,
                cursor="hand2",
                command=lambda opt=opcion, k=f"pregunta_{pregunta_id}":
                self.respuestas[k]["var_opcion"].set(opt["id"])
            )
            rb.pack(anchor="w", pady=2)

    def _crear_tab_resultados(self, notebook):
        """Crea la pestaña de Resultados"""
        tab = tk.Frame(notebook, bg=AppStyles.CARD_BG)
        notebook.add(tab, text="📊 Resultados")

        # Mensaje placeholder
        tk.Label(
            tab,
            text="Los resultados aparecerán aquí una vez completes el test",
            font=(AppStyles.FONT_FAMILY, 14),
            fg=AppStyles.TEXT_LIGHT,
            bg=AppStyles.CARD_BG
        ).pack(expand=True)

    def enviar_test(self):
        # Verificar que todas las preguntas estén respondidas
        sin_responder = []
        for pregunta_key, datos in self.respuestas.items():
            if datos["var_fuzzy"].get() == -1:
                sin_responder.append(pregunta_key)

        if sin_responder:
            UIHelpers.mostrar_mensaje_error(
                "Test incompleto",
                f"Por favor responde todas las preguntas. Faltan {len(sin_responder)} preguntas."
            )
            return

        # Formatear respuestas para el controlador
        respuestas_formateadas = []
        for pregunta_key, datos in self.respuestas.items():
            pregunta_id = int(pregunta_key.split("_")[1])
            valor_fuzzy = datos["var_fuzzy"].get()
            opcion_id = datos["var_opcion"].get()

            respuestas_formateadas.append({
                "pregunta_id": pregunta_id,
                "opcion_id": opcion_id,
                "valor_fuzzy": valor_fuzzy
            })

        # Enviar al controlador
        estudiante_id = self.estudiante['id']
        exito, error = TestVocacionalController.guardar_respuestas(
            estudiante_id,
            respuestas_formateadas
        )

        if exito:
            UIHelpers.mostrar_mensaje_info(
                "Test enviado",
                "El test ha sido enviado correctamente. Los resultados se procesarán pronto."
            )
        else:
            UIHelpers.mostrar_mensaje_error(
                "Error al guardar",
                f"Hubo un problema al guardar las respuestas: {error}"
            )

    def cerrar_sesion(self):
        UIHelpers.cerrar_sesion(self.root)
