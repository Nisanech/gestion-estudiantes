import tkinter as tk
from tkinter import ttk, messagebox

from controllers.estudiante_controller import EstudianteController
from controllers.programa_controller import ProgramaController
from controllers.usuario_controller import UsuarioController


class AdminView:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario

        self.root.title("Panel Administrador")
        self.root.geometry("1200x1000")
        
        # Paleta de Colores
        self.bg_color = "#F8FAFC"
        self.header_bg = "#1E293B"
        self.primary_color = "#2563EB"
        self.primary_hover = "#1D4ED8"
        self.text_color = "#1E293B"
        self.text_light = "#64748B"
        self.card_bg = "#FFFFFF"
        self.border_color = "#E2E8F0"

        # Tipo de fuente
        self.font = "Segoe UI"

        self.estilo_treeview = "Custom.Treeview"
        
        self.root.configure(bg=self.bg_color)
        
        # -------- HEADER --------
        header_frame = tk.Frame(self.root, bg=self.header_bg, height=100)
        header_frame.pack(fill="x", side="top")
        header_frame.pack_propagate(False)
        
        # Contenedor interno del header
        header_content = tk.Frame(header_frame, bg=self.header_bg)
        header_content.pack(fill="both", expand=True, padx=30, pady=15)
        
        # Título y usuario
        title_frame = tk.Frame(header_content, bg=self.header_bg)
        title_frame.pack(side="left")
        
        tk.Label(
            title_frame,
            text="Panel de Administración",
            font=(self.font, 18, "bold"),
            fg="white",
            bg=self.header_bg
        ).pack(anchor="w")
        
        tk.Label(
            title_frame,
            text=f"👤 {usuario['correo']}",
            font=(self.font, 10),
            fg="#94A3B8",
            bg=self.header_bg
        ).pack(anchor="w", pady=(5, 0))
        
        # Botón de cerrar sesión
        btn_cerrar_sesion = tk.Button(
            header_content,
            text="Cerrar Sesión",
            command=self.cerrar_sesion,
            font=(self.font, 10, "bold"),
            bg="#EF4444",
            fg="white",
            activebackground="#DC2626",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8
        )
        btn_cerrar_sesion.pack(side="right")

        # Efectos hover para el botón
        btn_cerrar_sesion.bind("<Enter>", lambda e: btn_cerrar_sesion.config(bg="#DC2626"))
        btn_cerrar_sesion.bind("<Leave>", lambda e: btn_cerrar_sesion.config(bg="#EF4444"))
        
        # -------- CONTENEDOR PRINCIPAL --------
        contenedor_principal = tk.Frame(self.root, bg=self.bg_color)
        contenedor_principal.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Configurar estilos para el Notebook
        estilos_notebook = ttk.Style()
        estilos_notebook.theme_use('clam')
        
        # Estilo para las pestañas
        estilos_notebook.configure(
            "Custom.TNotebook",
            background=self.bg_color,
            borderwidth=0
        )
        estilos_notebook.configure(
            "Custom.TNotebook.Tab",
            background=self.card_bg,
            foreground=self.text_color,
            padding=[20, 10],
            font=(self.font, 11, "bold"),
            borderwidth=1,
            relief="solid"
        )
        estilos_notebook.map(
            "Custom.TNotebook.Tab",
            background=[("selected", self.primary_color)],
            foreground=[("selected", "white")],
            expand=[("selected", [1, 1, 1, 0])]
        )
        
        # Estilo para Treeview
        estilos_notebook.configure(
            self.estilo_treeview,
            background=self.card_bg,
            foreground=self.text_color,
            fieldbackground=self.card_bg,
            borderwidth=0,
            font=(self.font, 10),
            rowheight=30
        )
        estilos_notebook.configure(
            "Custom.Treeview.Heading",
            background=self.primary_color,
            foreground="white",
            font=(self.font, 11, "bold"),
            borderwidth=0,
            relief="flat"
        )
        estilos_notebook.map(
            self.estilo_treeview,
            background=[("selected", self.primary_color)],
            foreground=[("selected", "white")]
        )
        
        # Notebook con pestañas
        notebook = ttk.Notebook(contenedor_principal, style="Custom.TNotebook")
        notebook.pack(fill="both", expand=True)

        # -------- TAB ESTUDIANTES --------
        tab_estudiante = tk.Frame(notebook, bg=self.card_bg)
        notebook.add(tab_estudiante, text="📚 Estudiantes")

        # -------- FORMULARIO CREAR ESTUDIANTE --------
        formulario_estudiante_frame = tk.Frame(tab_estudiante, bg=self.card_bg)
        formulario_estudiante_frame.pack(fill="x", padx=15, pady=15)
        
        # Título del formulario
        tk.Label(
            formulario_estudiante_frame,
            text="Crear Nuevo Estudiante",
            font=(self.font, 14, "bold"),
            fg=self.text_color,
            bg=self.card_bg
        ).pack(anchor="w", pady=(0, 15))
        
        # -------- DATOS DE USUARIO --------
        datos_usuario_frame = tk.Frame(formulario_estudiante_frame, bg=self.card_bg)
        datos_usuario_frame.pack(fill="x", pady=(0, 15))
        
        tk.Label(
            datos_usuario_frame,
            text="Datos de Usuario",
            font=(self.font, 11, "bold"),
            fg=self.primary_color,
            bg=self.card_bg
        ).pack(anchor="w", pady=(0, 10))
        
        # Contenedor para campos del formulario - Usuario
        campos_form_usuario_frame = tk.Frame(datos_usuario_frame, bg=self.card_bg)
        campos_form_usuario_frame.pack(fill="x")
        
        # Campo Correo
        correo_container = tk.Frame(campos_form_usuario_frame, bg=self.card_bg)
        correo_container.pack(side="left", padx=(0, 15), expand=True, fill="x")
        
        tk.Label(
            correo_container,
            text="Correo Electrónico:",
            font=(self.font, 10),
            fg=self.text_color,
            bg=self.card_bg
        ).pack(anchor="w")
        
        self.entry_correo = tk.Entry(
            correo_container,
            font=(self.font, 10),
            bg=self.card_bg,
            fg=self.text_color,
            relief="solid",
            borderwidth=1,
            highlightthickness=1,
            highlightbackground=self.border_color,
            highlightcolor=self.primary_color
        )
        self.entry_correo.pack(fill="x", ipady=5)
        
        # Campo Password
        password_container = tk.Frame(campos_form_usuario_frame, bg=self.card_bg)
        password_container.pack(side="left", padx=(0, 15), expand=True, fill="x")
        
        tk.Label(
            password_container,
            text="Contraseña:",
            font=(self.font, 10),
            fg=self.text_color,
            bg=self.card_bg
        ).pack(anchor="w")
        
        self.entry_password = tk.Entry(
            password_container,
            font=(self.font, 10),
            bg=self.card_bg,
            fg=self.text_color,
            relief="solid",
            borderwidth=1,
            highlightthickness=1,
            highlightbackground=self.border_color,
            highlightcolor=self.primary_color,
            show="*"
        )
        self.entry_password.pack(fill="x", ipady=5)
        
        # Campo Rol
        rol_container = tk.Frame(campos_form_usuario_frame, bg=self.card_bg)
        rol_container.pack(side="left", expand=True, fill="x")
        
        tk.Label(
            rol_container,
            text="Rol:",
            font=(self.font, 10),
            fg=self.text_color,
            bg=self.card_bg
        ).pack(anchor="w")
        
        self.entry_rol = tk.Entry(
            rol_container,
            font=(self.font, 10),
            bg="#F1F5F9",
            fg=self.text_light,
            relief="solid",
            borderwidth=1,
            highlightthickness=1,
            highlightbackground=self.border_color,
            state="readonly"
        )
        self.entry_rol.pack(fill="x", ipady=5)

        # Insertar valor por defecto
        self.entry_rol.config(state="normal")
        self.entry_rol.insert(0, "estudiante")
        self.entry_rol.config(state="readonly")
        
        # -------- DATOS DEL ESTUDIANTE --------
        datos_estudiante_frame = tk.Frame(formulario_estudiante_frame, bg=self.card_bg)
        datos_estudiante_frame.pack(fill="x", pady=(0, 15))
        
        tk.Label(
            datos_estudiante_frame,
            text="Datos del Estudiante",
            font=(self.font, 11, "bold"),
            fg=self.primary_color,
            bg=self.card_bg
        ).pack(anchor="w", pady=(0, 10))
        
        # Contenedor para campos del formulario - Estudiante
        campos_form_estudiante_frame = tk.Frame(datos_estudiante_frame, bg=self.card_bg)
        campos_form_estudiante_frame.pack(fill="x")
        
        # Campo Nombre
        nombre_container = tk.Frame(campos_form_estudiante_frame, bg=self.card_bg)
        nombre_container.pack(side="left", padx=(0, 15), expand=True, fill="x")
        
        tk.Label(
            nombre_container,
            text="Nombre:",
            font=(self.font, 10),
            fg=self.text_color,
            bg=self.card_bg
        ).pack(anchor="w")
        
        self.entry_nombre = tk.Entry(
            nombre_container,
            font=(self.font, 10),
            bg=self.card_bg,
            fg=self.text_color,
            relief="solid",
            borderwidth=1,
            highlightthickness=1,
            highlightbackground=self.border_color,
            highlightcolor=self.primary_color
        )
        self.entry_nombre.pack(fill="x", ipady=5)
        
        # Campo Apellido
        apellido_container = tk.Frame(campos_form_estudiante_frame, bg=self.card_bg)
        apellido_container.pack(side="left", padx=(0, 15), expand=True, fill="x")
        
        tk.Label(
            apellido_container,
            text="Apellido:",
            font=(self.font, 10),
            fg=self.text_color,
            bg=self.card_bg
        ).pack(anchor="w")
        
        self.entry_apellido = tk.Entry(
            apellido_container,
            font=(self.font, 10),
            bg=self.card_bg,
            fg=self.text_color,
            relief="solid",
            borderwidth=1,
            highlightthickness=1,
            highlightbackground=self.border_color,
            highlightcolor=self.primary_color
        )
        self.entry_apellido.pack(fill="x", ipady=5)
        
        # Campo Edad
        edad_container = tk.Frame(campos_form_estudiante_frame, bg=self.card_bg)
        edad_container.pack(side="left", padx=(0, 15), expand=True, fill="x")
        
        tk.Label(
            edad_container,
            text="Edad:",
            font=(self.font, 10),
            fg=self.text_color,
            bg=self.card_bg
        ).pack(anchor="w")
        
        self.entry_edad = tk.Entry(
            edad_container,
            font=(self.font, 10),
            bg=self.card_bg,
            fg=self.text_color,
            relief="solid",
            borderwidth=1,
            highlightthickness=1,
            highlightbackground=self.border_color,
            highlightcolor=self.primary_color
        )
        self.entry_edad.pack(fill="x", ipady=5)
        
        # Campo Género
        genero_container = tk.Frame(campos_form_estudiante_frame, bg=self.card_bg)
        genero_container.pack(side="left", expand=True, fill="x")
        
        tk.Label(
            genero_container,
            text="Género:",
            font=(self.font, 10),
            fg=self.text_color,
            bg=self.card_bg
        ).pack(anchor="w")
        
        # Estilo para el Combobox
        estilos_notebook.configure(
            "Custom.TCombobox",
            fieldbackground=self.card_bg,
            background=self.card_bg,
            foreground=self.text_color,
            borderwidth=1,
            relief="solid"
        )
        
        self.combo_genero = ttk.Combobox(
            genero_container,
            values=["F", "M", "Otro"],
            font=(self.font, 10),
            state="readonly",
            style="Custom.TCombobox"
        )
        self.combo_genero.pack(fill="x", ipady=5)
        self.combo_genero.set("F")  # Valor por defecto
        
        # Botón Guardar
        btn_guardar_frame = tk.Frame(formulario_estudiante_frame, bg=self.card_bg)
        btn_guardar_frame.pack(fill="x", pady=(10, 0))
        
        btn_guardar = tk.Button(
            btn_guardar_frame,
            text="Guardar Estudiante",
            command=self.crear_estudiante,
            font=(self.font, 11, "bold"),
            bg=self.primary_color,
            fg="white",
            activebackground=self.primary_hover,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=10
        )
        btn_guardar.pack(side="left")
        
        # Efectos hover para el botón
        btn_guardar.bind("<Enter>", lambda e: btn_guardar.config(bg=self.primary_hover))
        btn_guardar.bind("<Leave>", lambda e: btn_guardar.config(bg=self.primary_color))
        
        # Separador visual
        separator = tk.Frame(tab_estudiante, bg=self.border_color, height=2)
        separator.pack(fill="x", padx=15, pady=(0, 15))

        cols_estudiante = ("Correo", "Nombre", "Apellido", "Edad", "Género")

        # Frame para la tabla con borde
        tabla_estudiantes_frame = tk.Frame(tab_estudiante, bg=self.border_color, padx=1, pady=1)
        tabla_estudiantes_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        
        self.tree_estudiantes = ttk.Treeview(
            tabla_estudiantes_frame,
            columns=cols_estudiante,
            show="headings",
            style=self.estilo_treeview
        )

        for col in cols_estudiante:
            self.tree_estudiantes.heading(col, text=col)
            self.tree_estudiantes.column(col, width=150, anchor="center")

        # Scrollbar para estudiantes
        scrollbar_est = ttk.Scrollbar(tabla_estudiantes_frame, orient="vertical", command=self.tree_estudiantes.yview)
        self.tree_estudiantes.configure(yscrollcommand=scrollbar_est.set)
        scrollbar_est.pack(side="right", fill="y")
        
        self.tree_estudiantes.pack(fill="both", expand=True)
        
        # Colores alternados en filas
        self.tree_estudiantes.tag_configure('oddrow', background="#F1F5F9")
        self.tree_estudiantes.tag_configure('evenrow', background=self.card_bg)

        self.cargar_estudiantes()

        # -------- TAB PROGRAMAS --------
        tab_programa = tk.Frame(notebook, bg=self.card_bg)
        notebook.add(tab_programa, text="🎓 Programas")

        # -------- FORMULARIO CREAR PROGRAMA --------
        formulario_programa_frame = tk.Frame(tab_programa, bg=self.card_bg)
        formulario_programa_frame.pack(fill="x", padx=15, pady=15)

        # Título del formulario
        tk.Label(
            formulario_programa_frame,
            text="Crear Nuevo Programa",
            font=(self.font, 14, "bold"),
            fg=self.text_color,
            bg=self.card_bg
        ).pack(anchor="w", pady=(0, 15))

        # -------- DATOS DEL PROGRAMA --------
        datos_programa_frame = tk.Frame(formulario_programa_frame, bg=self.card_bg)
        datos_programa_frame.pack(fill="x", pady=(0, 15))

        tk.Label(
            datos_programa_frame,
            text="Datos del Programa",
            font=(self.font, 11, "bold"),
            fg=self.primary_color,
            bg=self.card_bg
        ).pack(anchor="w", pady=(0, 10))

        # Contenedor para campos del formulario
        campos_form_programa_frame = tk.Frame(datos_programa_frame, bg=self.card_bg)
        campos_form_programa_frame.pack(fill="x")

        # Campo Nombre del Programa
        programa_container = tk.Frame(campos_form_programa_frame, bg=self.card_bg)
        programa_container.pack(side="left", padx=(0, 15), expand=True, fill="x")

        tk.Label(
            programa_container,
            text="Nombre del Programa:",
            font=(self.font, 10),
            fg=self.text_color,
            bg=self.card_bg
        ).pack(anchor="w")

        self.entry_nombre_programa = tk.Entry(
            programa_container,
            font=(self.font, 10),
            bg=self.card_bg,
            fg=self.text_color,
            relief="solid",
            borderwidth=1,
            highlightthickness=1,
            highlightbackground=self.border_color,
            highlightcolor=self.primary_color
        )
        self.entry_nombre_programa.pack(fill="x", ipady=5)

        # Campo Descripcion Programa
        descripcion_container = tk.Frame(campos_form_programa_frame, bg=self.card_bg)
        descripcion_container.pack(side="left", padx=(0, 15), expand=True, fill="x")

        tk.Label(
            descripcion_container,
            text="Descripción del programa:",
            font=(self.font, 10),
            fg=self.text_color,
            bg=self.card_bg
        ).pack(anchor="w")

        self.entry_descripcion = tk.Entry(
            descripcion_container,
            font=(self.font, 10),
            bg=self.card_bg,
            fg=self.text_color,
            relief="solid",
            borderwidth=1,
            highlightthickness=1,
            highlightbackground=self.border_color,
            highlightcolor=self.primary_color,
            show="*"
        )
        self.entry_descripcion.pack(fill="x", ipady=5)

        # Botón Guardar
        btn_guardar_frame = tk.Frame(formulario_programa_frame, bg=self.card_bg)
        btn_guardar_frame.pack(fill="x", pady=(10, 0))

        btn_guardar = tk.Button(
            btn_guardar_frame,
            text="Guardar Programa",
            font=(self.font, 11, "bold"),
            bg=self.primary_color,
            fg="white",
            activebackground=self.primary_hover,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=10
        )
        btn_guardar.pack(side="left")

        # Efectos hover para el botón
        btn_guardar.bind("<Enter>", lambda e: btn_guardar.config(bg=self.primary_hover))
        btn_guardar.bind("<Leave>", lambda e: btn_guardar.config(bg=self.primary_color))

        # Separador visual
        separator = tk.Frame(tab_programa, bg=self.border_color, height=2)
        separator.pack(fill="x", padx=15, pady=(0, 15))

        cols_programa = ("ID", "Programa", "Descripción")

        # Frame para la tabla con borde
        tabla_programas_frame = tk.Frame(tab_programa, bg=self.border_color, padx=1, pady=1)
        tabla_programas_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        self.tree_programas = ttk.Treeview(
            tabla_programas_frame,
            columns=cols_programa,
            show="headings",
            style=self.estilo_treeview
        )

        for col in cols_programa:
            self.tree_programas.heading(col, text=col)
            if col == "Descripción":
                self.tree_programas.column(col, width=400, anchor="w")
            else:
                self.tree_programas.column(col, width=150, anchor="center")

        # Scrollbar para programas
        scrollbar_prog = ttk.Scrollbar(tabla_programas_frame, orient="vertical", command=self.tree_programas.yview)
        self.tree_programas.configure(yscrollcommand=scrollbar_prog.set)
        scrollbar_prog.pack(side="right", fill="y")
        
        self.tree_programas.pack(fill="both", expand=True)
        
        # Colores alternados en filas
        self.tree_programas.tag_configure('oddrow', background="#F1F5F9")
        self.tree_programas.tag_configure('evenrow', background=self.card_bg)

        self.cargar_programas()


    # -------- MÉTODOS --------
    def cargar_estudiantes(self):
        for row in self.tree_estudiantes.get_children():
            self.tree_estudiantes.delete(row)

        estudiantes = EstudianteController.listar_estudiantes()

        for idx, est in enumerate(estudiantes):
            tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
            self.tree_estudiantes.insert("", "end", values=est, tags=(tag,))


    def cargar_programas(self):
        for row in self.tree_programas.get_children():
            self.tree_programas.delete(row)

        programas = ProgramaController.listar_programas()

        for idx, prog in enumerate(programas):
            tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
            self.tree_programas.insert("", "end", values=prog, tags=(tag,))


    def cerrar_sesion(self):
        self.root.destroy()

        from views.login_view import LoginView

        ventana = tk.Tk()
        LoginView(ventana)
        ventana.mainloop()

    def crear_estudiante(self):
        # Obtener datos del formulario
        correo = self.entry_correo.get().strip()
        password = self.entry_password.get().strip()
        rol = self.entry_rol.get()

        nombre = self.entry_nombre.get().strip()
        apellido = self.entry_apellido.get().strip()
        edad = self.entry_edad.get().strip()
        genero = self.combo_genero.get()

        # Crear usuario
        usuario_id, error = UsuarioController.crear_usuario(correo, password, rol)

        if error:
            messagebox.showerror("Error", error)
            return

        # Crear estudiante asociado al usuario
        estudiante_id, error = EstudianteController.crear_estudiante(usuario_id, nombre, apellido, edad, genero)

        if error:
            messagebox.showerror("Error", error)
            return

        messagebox.showinfo("Éxito", "Estudiante creado correctamente")

        self.cargar_estudiantes()