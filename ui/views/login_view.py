import tkinter as tk
from types import SimpleNamespace

from controllers.login_controller import LoginController
from ui.components import AppStyles, HeaderBuilder, FormBuilder
from ui.helpers import UIHelpers


class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("450x550")
        self.root.resizable(False, False)
        self.root.configure(bg=AppStyles.BG_COLOR)

        # Configurar estilos globales
        AppStyles.estilos_notebook()

        # Construir interfaz
        self._build_ui()

    def _build_ui(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg=AppStyles.BG_COLOR)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # -------- ENCABEZADO --------
        HeaderBuilder.crear_encabezado_login(main_frame, "Gestión de Estudiantes", "Inicia sesión para continuar")

        # -------- FORMULARIO --------
        self.form_builder = FormBuilder(main_frame)
        self.form_builder.crear_formulario_login(self.login)

    # -------- MÉTODOS --------
    def login(self):
        # Obtener datos del formulario
        valores = SimpleNamespace(**self.form_builder.obtener_valores())

        if not valores.correo or not valores.password:
            UIHelpers.mostrar_mensaje_error("Campos vacíos",
                                            "Por favor ingresa tu correo y contraseña")
            return

        # Validar credenciales por medio del controlador
        usuario = LoginController.login(valores.correo, valores.password)

        if usuario is None:
            UIHelpers.mostrar_mensaje_error("Error", "Credenciales incorrectas")
            return

        # Obtener datos del usuario
        rol = usuario['rol']

        # Eliminar la vista de login
        self.root.destroy()

        # Redirigir según el rol del usuario
        self._redirigir_por_rol(rol, usuario)

    def _redirigir_por_rol(self, rol, usuario):
        if rol == 'admin':
            from ui.views.admin_view import AdminView

            root_admin = tk.Tk()
            AdminView(root_admin, usuario)
            root_admin.mainloop()
        elif rol == 'estudiante':
            from ui.views.estudiante_view import EstudianteView

            root_estudiante = tk.Tk()
            EstudianteView(root_estudiante, usuario)
            root_estudiante.mainloop()
