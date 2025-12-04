import tkinter as tk
from tkinter import ttk

from controllers.estudiante_controller import EstudianteController
from controllers.programa_controller import ProgramaController


class AdminView:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario

        self.root.title("Panel Administrador")
        self.root.geometry("1000x650")
        
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
        btn_logout = tk.Button(
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
        btn_logout.pack(side="right")

        # Efectos hover para el botón
        btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="#DC2626"))
        btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="#EF4444"))
        
        # -------- CONTENEDOR PRINCIPAL --------
        main_container = tk.Frame(self.root, bg=self.bg_color)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Configurar estilos para el Notebook
        style = ttk.Style()
        style.theme_use('clam')
        
        # Estilo para las pestañas
        style.configure(
            "Custom.TNotebook",
            background=self.bg_color,
            borderwidth=0
        )
        style.configure(
            "Custom.TNotebook.Tab",
            background=self.card_bg,
            foreground=self.text_color,
            padding=[20, 10],
            font=(self.font, 11, "bold"),
            borderwidth=1,
            relief="solid"
        )
        style.map(
            "Custom.TNotebook.Tab",
            background=[("selected", self.primary_color)],
            foreground=[("selected", "white")],
            expand=[("selected", [1, 1, 1, 0])]
        )
        
        # Estilo para Treeview
        style.configure(
            self.estilo_treeview,
            background=self.card_bg,
            foreground=self.text_color,
            fieldbackground=self.card_bg,
            borderwidth=0,
            font=(self.font, 10),
            rowheight=30
        )
        style.configure(
            "Custom.Treeview.Heading",
            background=self.primary_color,
            foreground="white",
            font=(self.font, 11, "bold"),
            borderwidth=0,
            relief="flat"
        )
        style.map(
            self.estilo_treeview,
            background=[("selected", self.primary_color)],
            foreground=[("selected", "white")]
        )
        
        # Notebook con pestañas
        notebook = ttk.Notebook(main_container, style="Custom.TNotebook")
        notebook.pack(fill="both", expand=True)

        # -------- TAB ESTUDIANTES --------
        tab_estudiante = tk.Frame(notebook, bg=self.card_bg)
        notebook.add(tab_estudiante, text="📚 Estudiantes")

        cols_estudiante = ("ID", "Nombre", "Apellido", "Edad", "Género")

        # Frame para la tabla con borde
        table_frame_est = tk.Frame(tab_estudiante, bg=self.border_color, padx=1, pady=1)
        table_frame_est.pack(fill="both", expand=True, padx=15, pady=15)
        
        self.tree_estudiantes = ttk.Treeview(
            table_frame_est,
            columns=cols_estudiante,
            show="headings",
            style=self.estilo_treeview
        )

        for col in cols_estudiante:
            self.tree_estudiantes.heading(col, text=col)
            self.tree_estudiantes.column(col, width=150, anchor="center")

        # Scrollbar para estudiantes
        scrollbar_est = ttk.Scrollbar(table_frame_est, orient="vertical", command=self.tree_estudiantes.yview)
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

        cols_programa = ("ID", "Programa", "Descripción")

        # Frame para la tabla con borde
        table_frame_prog = tk.Frame(tab_programa, bg=self.border_color, padx=1, pady=1)
        table_frame_prog.pack(fill="both", expand=True, padx=15, pady=15)
        
        self.tree_programas = ttk.Treeview(
            table_frame_prog,
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
        scrollbar_prog = ttk.Scrollbar(table_frame_prog, orient="vertical", command=self.tree_programas.yview)
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
