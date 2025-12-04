import tkinter as tk
from tkinter import messagebox

from controllers.login_controller import LoginController

from views.admin_view import AdminView
from views.estudiante_view import EstudianteView


class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        # Paleta de Colores
        self.bg_color = "#F0F4F8"
        self.primary_color = "#2563EB"
        self.primary_hover = "#1D4ED8"
        self.text_color = "#1E293B"
        self.input_bg = "#FFFFFF"
        self.border_color = "#CBD5E1"

        # Tipo de fuente
        self.font = "Segoe UI"

        self.root.configure(bg=self.bg_color)

        # Frame principal
        main_frame = tk.Frame(root, bg=self.bg_color)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # -------- ENCABEZADO --------
        header_frame = tk.Frame(main_frame, bg=self.bg_color)
        header_frame.pack(pady=(0, 30))

        title_label = tk.Label(
            header_frame,
            text="Gestión de Estudiantes",
            font=(self.font, 24, "bold"),
            fg=self.text_color,
            bg=self.bg_color
        )
        title_label.pack()

        subtitle_label = tk.Label(
            header_frame,
            text="Inicia sesión para continuar",
            font=(self.font, 11),
            fg="#64748b",
            bg=self.bg_color
        )
        subtitle_label.pack(pady=(5, 0))

        # -------- FORMULARIO --------
        form_frame = tk.Frame(main_frame, bg=self.bg_color)
        form_frame.pack(pady=10)

        tk.Label(
            form_frame,
            text="Correo electrónico",
            font=(self.font, 10, "bold"),
            fg=self.text_color,
            bg=self.bg_color,
            anchor="w"
        ).pack(fill="x", pady=(0, 5))

        self.entry_correo = tk.Entry(
            form_frame,
            width=35,
            font=(self.font, 11),
            bg=self.input_bg,
            fg=self.text_color,
            relief="solid",
            borderwidth=1,
            highlightthickness=2,
            highlightbackground=self.border_color,
            highlightcolor=self.primary_color
        )
        self.entry_correo.pack(ipady=8, pady=(0, 20))

        tk.Label(
            form_frame,
            text="Contraseña",
            font=(self.font, 10, "bold"),
            fg=self.text_color,
            bg=self.bg_color,
            anchor="w"
        ).pack(fill="x", pady=(0, 5))

        self.entry_password = tk.Entry(
            form_frame,
            width=35,
            show="●",
            font=(self.font, 11),
            bg=self.input_bg,
            fg=self.text_color,
            relief="solid",
            borderwidth=1,
            highlightthickness=2,
            highlightbackground=self.border_color,
            highlightcolor=self.primary_color
        )
        self.entry_password.pack(ipady=8, pady=(0, 25))

        self.btn_login = tk.Button(
            form_frame,
            text="Ingresar",
            command=self.login,
            font=(self.font, 12, "bold"),
            bg=self.primary_color,
            fg="white",
            activebackground=self.primary_hover,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            width=32,
            pady=12
        )
        self.btn_login.pack(pady=(0, 10))

        # Efectos hover para el botón
        self.btn_login.bind("<Enter>", lambda e: self.btn_login.config(bg=self.primary_hover))
        self.btn_login.bind("<Leave>", lambda e: self.btn_login.config(bg=self.primary_color))

        # Evento: Tecla Enter para ingresar
        self.entry_password.bind("<Return>", lambda e: self.login())


    # -------- MÉTODOS --------
    def login(self):
        # Obtener datos del formulario
        correo = self.entry_correo.get()
        password = self.entry_password.get()

        # Validar credenciales por medio del controlador
        usuario = LoginController.login(correo, password)

        if usuario is None:
            messagebox.showerror("Error", "Credenciales incorrectas")
            return

        rol = usuario['rol']
        user_id = usuario['id']

        # Eliminar la vista de login
        self.root.destroy()

        # Redirigir según el rol del usuario
        if rol == 'admin':
            root_admin = tk.Tk()
            AdminView(root_admin, usuario)
            root_admin.mainloop()
        elif rol == 'estudiante':
            root_estudiante = tk.Tk()
            EstudianteView(root_estudiante, user_id)
            root_estudiante.mainloop()