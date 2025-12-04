"""
    Clase que implementa la interfaz gráfica de usuario (GUI) completa del sistema de gestión de estudiantes usando Tkinter. Maneja formularios, tablas, filtros y toda la interacción con el usuario.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from models.estudiante import Estudiante
from models.programa import Programa
from models.estudiante_programa import EstudiantePrograma


class InterfazApp:
    def __init__(self, root):
        """
         Inicializa la interfaz gráfica completa con todos sus componentes.
         Parámetros:
            root (tk.Tk): Ventana raíz de Tkinter
        Componentes creados:
            Formulario de registro de estudiantes
            Tabla de visualización (Treeview)
            Panel de filtros
        """
        self.root = root
        self.root.title("Gestión de Estudiantes")

        # -------- FORMULARIO --------
        frame_form = tk.LabelFrame(root, text="Registro de Estudiante", padx=10, pady=10) # Formulario de Registro
        frame_form.pack(fill="x", padx=10, pady=5)

        # Tipo estudiante (Nuevo o Existente)
        tk.Label(frame_form, text="Tipo:").grid(row=0, column=0)
        self.tipo = ttk.Combobox(frame_form, values=["Nuevo", "Existente"], state="readonly") # Selector "Nuevo" o "Existente"
        self.tipo.grid(row=0, column=1)
        self.tipo.current(0)
        self.tipo.bind("<<ComboboxSelected>>", self.cambiar_tipo)

        # Campos de nuevo estudiante
        tk.Label(frame_form, text="Nombre:").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(frame_form) # Campo de texto para nombre del nuevo estudiante
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(frame_form, text="Edad:").grid(row=2, column=0)
        self.entry_edad = tk.Entry(frame_form) # Campo numérico para edad del nuevo estudiante
        self.entry_edad.grid(row=2, column=1)

        # Select de estudiantes existentes
        tk.Label(frame_form, text="Estudiante existente:").grid(row=3, column=0)
        self.combo_estudiantes = ttk.Combobox(frame_form, state="disabled") # Selector de estudiantes existentes (inicialmente deshabilitado)
        self.combo_estudiantes.grid(row=3, column=1)

        # Programas
        tk.Label(frame_form, text="Programas:").grid(row=4, column=0)
        self.combo_programas = ttk.Combobox(frame_form, state="readonly") # Selector de programas académicos
        self.combo_programas.grid(row=4, column=1)

        # Cargar programas y estudiantes
        self.cargar_programas()
        self.cargar_estudiantes_en_select()

        tk.Button(
            frame_form, text="Guardar",
            command=self.guardar_estudiante
        ).grid(row=5, column=0, columnspan=2, pady=5) # Ejecuta guardar_estudiante()

        # -------- LISTA DE ESTUDIANTES --------
        frame_lista = tk.LabelFrame(root, text="Estudiantes Registrados")
        frame_lista.pack(fill="both", expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(frame_lista, columns=("ID", "Nombre", "Edad", "Programas"), show="headings") # Tabla de Estudiantes

        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Edad", text="Edad")
        self.tree.heading("Programas", text="Programas")
        self.tree.pack(fill="both", expand=True)

        # Refrescar lista al iniciar
        self.cargar_estudiantes()

        # -------- FILTROS --------
        frame_filtros = tk.LabelFrame(root, text="Filtros", padx=10, pady=10)
        frame_filtros.pack(fill="x", padx=10, pady=5)

        tk.Button(frame_filtros, text="Mayores de 18", command=self.filtrar_mayores).grid(row=0, column=0, padx=5) # Filtra estudiantes > 18 años

        tk.Label(frame_filtros, text="Filtrar por programa").grid(row=0, column=1)
        self.combo_filtrar_programa = ttk.Combobox(frame_filtros, state="readonly") # Selector de programas
        self.combo_filtrar_programa.grid(row=0, column=2)

        self.combo_filtrar_programa["values"] = ["Todos"] + [f"{p[0]} - {p[1]}" for p in Programa.listar()]
        self.combo_filtrar_programa.current(0)

        tk.Button(frame_filtros, text="Filtrar", command=self.filtrar_por_programa).grid(row=0, column=3, padx=5) # Aplica el filtro seleccionado

    # ====================================================================
    #             HABILITAR FORMULARIO - TIPO ESTUDIANTE
    # ====================================================================

    def cambiar_tipo(self, event=None):
        """
            Maneja el cambio entre modo "Nuevo estudiante" y "Estudiante existente".\
            Parámetros:
                event (Event, opcional): Evento de Tkinter (no utilizado directamente)
            Funcionamiento:
                Modo "Nuevo":
                    ✅ Habilita campos entry_nombre y entry_edad
                    ❌ Deshabilita combo_estudiantes
                Modo "Existente":
                    ❌ Deshabilita campos entry_nombre y entry_edad
                    ✅ Habilita combo_estudiantes
                    Recarga lista de estudiantes
        """
        tipo = self.tipo.get()

        if tipo == "Nuevo":
            self.entry_nombre.config(state="normal")
            self.entry_edad.config(state="normal")
            self.combo_estudiantes.config(state="disabled")

        else:
            self.entry_nombre.config(state="disabled")
            self.entry_edad.config(state="disabled")
            self.combo_estudiantes.config(state="readonly")
            self.cargar_estudiantes_en_select()


    def cargar_programas(self):
        """
            Carga todos los programas disponibles en el Combobox.
            Funcionamiento:
                Obtiene lista de programas usando Programa.listar()
                Formatea como "ID - Nombre" (ej: "1 - Ingeniería de Sistemas")
                Asigna valores al combo_programa
        """
        programas = Programa.listar()
        self.combo_programas["values"] = [f"{p[0]} - {p[1]}" for p in programas]


    def cargar_estudiantes_en_select(self):
        """
            Carga todos los estudiantes en el Combobox de estudiantes existentes.
            Funcionamiento:
                Obtiene lista de estudiantes usando Estudiante.listar()
                Formatea como "ID - Nombre" (ej: "5 - Juan Pérez")
                Asigna valores al combo_estudiantes
        """
        estudiantes = Estudiante.listar()
        self.combo_estudiantes["values"] = [f"{e[0]} - {e[1]}" for e in estudiantes]

    # ====================================================================
    #                         GUARDAR
    # ====================================================================

    def guardar_estudiante(self):
        """
            Guarda un nuevo estudiante o asigna un programa a uno existente según el modo seleccionado.
            Flujo de ejecución:
                Caso 1: Nuevo Estudiante
                    Extrae el ID del programa seleccionado
                    Obtiene nombre y edad de los campos
                    Crea instancia de Estudiante
                    Llama a crear() para insertar en BD (obtiene ID generado)
                    Asigna el programa usando EstudiantePrograma.asignar()
                    Muestra mensaje de confirmación
                    Recarga lista de estudiantes
                Caso 2: Estudiante Existente
                    Extrae el ID del programa seleccionado
                    Extrae el ID del estudiante seleccionado
                    Asigna el programa usando EstudiantePrograma.asignar()
                    Muestra mensaje de confirmación
                    Recarga lista de estudiantes
        """
        programa_id = int(self.combo_programas.get().split(" - ")[0])

        if self.tipo.get() == "Nuevo":
            nombre = self.entry_nombre.get() # Juan
            edad = int(self.entry_edad.get()) # 18

            est = Estudiante(None, nombre, edad)
            est_id = est.crear() # 7

            EstudiantePrograma.asignar(est_id, programa_id)

            messagebox.showinfo("OK", "Estudiante creado y asignado")

        else:
            est_id = int(self.combo_estudiantes.get().split(" - ")[0])
            EstudiantePrograma.asignar(est_id, programa_id)

            messagebox.showinfo("OK", "Programa asignado a estudiante existente")

        self.cargar_estudiantes()
        self.cargar_estudiantes_en_select()

    # ====================================================================
    #                       CARGAR LISTA
    # ====================================================================

    def cargar_estudiantes(self):
        """
            Carga y muestra todos los estudiantes en la tabla con sus programas.
            Funcionamiento:
                Limpia todas las filas existentes en el Treeview
                Obtiene lista completa de estudiantes
                Para cada estudiante:
                    Obtiene sus programas asignados
                    Une los nombres de programas con ", "
                    Inserta fila en la tabla
        """
        for row in self.tree.get_children():
            self.tree.delete(row)

        estudiantes = Estudiante.listar()

        for est in estudiantes:
            programas = EstudiantePrograma.obtener_programas_de_estudiante(est[0])
            self.tree.insert("", "end", values=(est[0], est[1], est[2], ", ".join(programas)))


    def filtrar_mayores(self):
        """
            Filtra y muestra solo los estudiantes mayores de 18 años.
            Funcionamiento:
                Limpia la tabla
                Obtiene estudiantes mayores de 18 usando Estudiante.listar_mayores_18()
                Para cada estudiante:
                    Obtiene sus programas
                    Inserta en la tabla
        """
        for row in self.tree.get_children():
            self.tree.delete(row)

        estudiantes = Estudiante.listar_mayores_18()

        for est in estudiantes:
            programas = EstudiantePrograma.obtener_programas_de_estudiante(est[0])
            self.tree.insert("", "end", values=(est[0], est[1], est[2], ", ".join(programas)))


    def filtrar_por_programa(self):
        """
            Filtra estudiantes inscritos en un programa específico o muestra todos.
            Funcionamiento:
                Caso "Todos":
                    Llama a cargar_estudiantes() para mostrar lista completa
                Caso programa específico:
                    Extrae el ID del programa seleccionado
                    Limpia la tabla
                    Obtiene estudiantes del programa usando EstudiantePrograma.filtrar_por_programa()
                Para cada estudiante:
                    Obtiene TODOS sus programas (no solo el filtrado)
                    Inserta en la tabla
        """
        seleccion = self.combo_filtrar_programa.get()

        if seleccion == "Todos":
            self.cargar_estudiantes()
            return

        programa_id = int(seleccion.split(" - ")[0])

        for row in self.tree.get_children():
            self.tree.delete(row)

        estudiantes = EstudiantePrograma.filtrar_por_programa(programa_id)

        for est in estudiantes:
            programas = EstudiantePrograma.obtener_programas_de_estudiante(est[0])
            self.tree.insert("", "end", values=(est[0], est[1], est[2], ", ".join(programas)))
