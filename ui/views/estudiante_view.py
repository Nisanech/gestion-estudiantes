from controllers.ia_controller import IAController
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
        self.notebook = None  # Referencia al notebook
        self.resultados_container = None  # Contenedor de resultados

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
        self.notebook = ttk.Notebook(contenedor_padre, style="Custom.TNotebook")
        self.notebook.pack(fill="both", expand=True)

        # Crear tabs
        self._crear_tab_test(self.notebook)
        self._crear_tab_resultados(self.notebook)
        
        # Vincular evento de cambio de pestaña
        self.notebook.bind("<<NotebookTabChanged>>", self._on_tab_changed)

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
        
        # Guardar referencia al contenedor de resultados
        self.resultados_container = tab
        
        # Cargar resultados inicialmente
        self._cargar_resultados()
    
    def _on_tab_changed(self, event):
        """Evento que se dispara cuando se cambia de pestaña"""
        # Verificar si la pestaña seleccionada es la de resultados (index 1)
        if self.notebook.index(self.notebook.select()) == 1:
            self._cargar_resultados()
    
    def _cargar_resultados(self):
        """Carga o recarga los resultados en la pestaña"""
        # Limpiar contenido anterior
        for widget in self.resultados_container.winfo_children():
            widget.destroy()
        
        # Obtener resultados del controlador
        exito, resultados = IAController.calcular_recomendaciones(self.estudiante['id'])

        # Si no hay resultados (test no completado), mostrar mensaje
        if not exito:
            tk.Label(
                self.resultados_container,
                text="Los resultados aparecerán aquí una vez completes el test",
                font=(AppStyles.FONT_FAMILY, 14),
                fg=AppStyles.TEXT_LIGHT,
                bg=AppStyles.CARD_BG
            ).pack(expand=True)
            return

        # Contenedor principal con padding
        main_container = tk.Frame(self.resultados_container, bg=AppStyles.CARD_BG)
        main_container.pack(fill="both", expand=True, padx=30, pady=10)

        # Contenedor de dos columnas
        columnas_frame = tk.Frame(main_container, bg=AppStyles.CARD_BG)
        columnas_frame.pack(fill="both", expand=True)

        # COLUMNA 1: Programa principal (top score)
        columna_1 = tk.Frame(columnas_frame, bg=AppStyles.CARD_BG)
        columna_1.pack(side="left", fill="both", expand=True, padx=(0, 15))

        self._crear_programa_principal(columna_1, resultados[0] if resultados else None)

        # COLUMNA 2: Otros programas
        columna_2 = tk.Frame(columnas_frame, bg=AppStyles.CARD_BG)
        columna_2.pack(side="left", fill="both", expand=True, padx=(15, 0))

        self._crear_otros_programas(columna_2, resultados[1:] if len(resultados) > 1 else [])

    def _crear_programa_principal(self, contenedor, programa):

        # Título de la sección
        tk.Label(
            contenedor,
            text="Test completado",
            font=(AppStyles.FONT_FAMILY, 16, "bold"),
            fg=AppStyles.TEXT_COLOR,
            bg=AppStyles.CARD_BG,
            anchor="w"
        ).pack(fill="x", pady=(0, 10))

        # Descripción
        tk.Label(
            contenedor,
            text="Estos son los resultados basados en tus respuestas.",
            font=(AppStyles.FONT_FAMILY, 10),
            fg=AppStyles.TEXT_LIGHT,
            bg=AppStyles.CARD_BG,
            wraplength=400,
            justify="left",
            anchor="w"
        ).pack(fill="x", pady=(0, 25))

        if not programa:
            tk.Label(
                contenedor,
                text="No hay resultados disponibles",
                font=(AppStyles.FONT_FAMILY, 11),
                fg=AppStyles.TEXT_LIGHT,
                bg=AppStyles.CARD_BG
            ).pack(fill="x", pady=20)
            return

        # Card del programa principal
        card_frame = tk.Frame(
            contenedor,
            bg=AppStyles.PRIMARY_COLOR,
            relief="solid",
            borderwidth=0
        )
        card_frame.pack(fill="x", pady=(0, 10))

        # Contenido del card
        content_frame = tk.Frame(card_frame, bg=AppStyles.PRIMARY_COLOR)
        content_frame.pack(fill="x", padx=20, pady=20)

        # Frame para nombre y puntaje
        info_frame = tk.Frame(content_frame, bg=AppStyles.PRIMARY_COLOR)
        info_frame.pack(fill="x")

        # Nombre del programa
        tk.Label(
            info_frame,
            text=programa["nombre"],
            font=(AppStyles.FONT_FAMILY, 14, "bold"),
            fg="white",
            bg=AppStyles.PRIMARY_COLOR,
            anchor="w"
        ).pack(side="left", fill="x", expand=True)

        # Puntaje
        puntaje_porcentaje = f"{programa['puntaje'] * 100:.0f}%"
        tk.Label(
            info_frame,
            text=puntaje_porcentaje,
            font=(AppStyles.FONT_FAMILY, 18, "bold"),
            fg="white",
            bg=AppStyles.PRIMARY_COLOR,
            anchor="e"
        ).pack(side="right")

    def _crear_otros_programas(self, contenedor, programas):
        """Crea la sección de otros programas"""
        # Título de la sección
        tk.Label(
            contenedor,
            text="Afinidad con otros Programas",
            font=(AppStyles.FONT_FAMILY, 16, "bold"),
            fg=AppStyles.TEXT_COLOR,
            bg=AppStyles.CARD_BG,
            anchor="w"
        ).pack(fill="x", pady=(0, 10))

        # Descripción
        tk.Label(
            contenedor,
            text="Tu compatibilidad con diferentes áreas de estudio",
            font=(AppStyles.FONT_FAMILY, 10),
            fg=AppStyles.TEXT_LIGHT,
            bg=AppStyles.CARD_BG,
            wraplength=400,
            justify="left",
            anchor="w"
        ).pack(fill="x", pady=(0, 25))

        if not programas:
            tk.Label(
                contenedor,
                text="No hay otros programas disponibles",
                font=(AppStyles.FONT_FAMILY, 11),
                fg=AppStyles.TEXT_LIGHT,
                bg=AppStyles.CARD_BG
            ).pack(fill="x", pady=20)
            return

        # Lista de programas
        for programa in programas:
            self._crear_item_programa(contenedor, programa)

    def _crear_item_programa(self, contenedor, programa):
        """Crea un item individual de programa"""
        # Frame del item
        item_frame = tk.Frame(
            contenedor,
            bg="white",
            relief="solid",
            borderwidth=1,
            highlightbackground=AppStyles.BORDER_COLOR,
            highlightthickness=1
        )
        item_frame.pack(fill="x", pady=(0, 10))

        # Contenido del item
        content_frame = tk.Frame(item_frame, bg="white")
        content_frame.pack(fill="x", padx=15, pady=12)

        # Frame para nombre y puntaje
        info_frame = tk.Frame(content_frame, bg="white")
        info_frame.pack(fill="x")

        # Nombre del programa
        tk.Label(
            info_frame,
            text=programa["nombre"],
            font=(AppStyles.FONT_FAMILY, 11),
            fg=AppStyles.TEXT_COLOR,
            bg="white",
            anchor="w"
        ).pack(side="left", fill="x", expand=True)

        # Puntaje
        puntaje_porcentaje = f"{programa['puntaje'] * 100:.0f}%"
        tk.Label(
            info_frame,
            text=puntaje_porcentaje,
            font=(AppStyles.FONT_FAMILY, 12, "bold"),
            fg=AppStyles.PRIMARY_COLOR,
            bg="white",
            anchor="e"
        ).pack(side="right")

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
                "El test ha sido enviado correctamente. Puedes ver los resultados en la pestaña 'Resultados'."
            )
        else:
            UIHelpers.mostrar_mensaje_error(
                "Error al guardar",
                f"Hubo un problema al guardar las respuestas: {error}"
            )


    def cerrar_sesion(self):
        UIHelpers.cerrar_sesion(self.root)
