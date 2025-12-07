import tkinter as tk
from tkinter import ttk

from controllers.estudiante_controller import EstudianteController
from controllers.programa_controller import ProgramaController

from ui.components import AppStyles, HeaderBuilder, FormBuilder, TableBuilder
from ui.helpers import UIHelpers


class AdminView:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario

        self.root.title("Panel Administrador")
        self.root.geometry("1200x1000")
        self.root.configure(bg=AppStyles.BG_COLOR)

        # Configurar estilos globales
        AppStyles.estilos_notebook()

        # Construir interfaz
        self._build_ui()

    def _build_ui(self):
        HeaderBuilder.crear_encabezado(self.root, self.usuario, self.cerrar_sesion)

        # Contenedor Principal
        contenedor_principal = tk.Frame(self.root, bg=AppStyles.BG_COLOR)
        contenedor_principal.pack(fill="both", expand=True, padx=30, pady=15)

        # Notebook con pestañas
        notebook = ttk.Notebook(contenedor_principal, style="Custom.TNotebook")
        notebook.pack(fill="both", expand=True)

        # Crear tabs
        self._crear_estudiantes_tab(notebook)
        self._crear_programas_tab(notebook)

    def _crear_estudiantes_tab(self, notebook):
        tab = tk.Frame(notebook, bg=AppStyles.CARD_BG)
        notebook.add(tab, text="📚 Estudiantes")

        # Formulario
        form = FormBuilder(tab)
        self.estudiante_fields = form.crear_formulario(
            titulo="Crear Nuevo Estudiante",
            secciones=[
                {
                    "titulo": "Datos de Usuario",
                    "campos": [
                        {
                            "nombre": "correo",
                            "etiqueta": "Correo Electrónico:",
                            "tipo": "entry"
                        },
                        {
                            "nombre": "password",
                            "etiqueta": "Contraseña:",
                            "tipo": "password"
                        },
                        {
                            "nombre": "rol",
                            "etiqueta": "Rol:",
                            "tipo": "readonly",
                            "default": "estudiante"
                        }
                    ]
                },
                {
                    "titulo": "Datos del Estudiante",
                    "campos": [
                        {
                            "nombre": "nombre",
                            "etiqueta": "Nombre:",
                            "tipo": "entry"
                        },
                        {
                            "nombre": "apellido",
                            "etiqueta": "Apellido:",
                            "tipo": "entry"
                        },
                        {
                            "nombre": "edad",
                            "etiqueta": "Edad:",
                            "tipo": "entry"
                        },
                        {
                            "nombre": "genero",
                            "etiqueta": "Género:",
                            "tipo": "combobox",
                            "opciones": ["F", "M", "Otro"],
                            "default": "F"
                        }
                    ]
                }
            ]
        )

        form.agregar_btn_guardar("Guardar Estudiante", self.crear_estudiante)
        form.agregar_separador()

        # Tabla
        self.tabla_estudiantes = TableBuilder(tab)
        self.tabla_estudiantes.crear_tabla(
            columnas=["Correo", "Nombre", "Apellido", "Edad", "Género"]
        )

        # Cargar datos
        self.cargar_estudiantes()

    def _crear_programas_tab(self, notebook):
        """Crea la pestaña de programas"""
        tab = tk.Frame(notebook, bg=AppStyles.CARD_BG)
        notebook.add(tab, text="🎓 Programas")

        # Formulario
        form = FormBuilder(tab)
        self.programa_fields = form.crear_formulario(
            titulo="Crear Nuevo Programa",
            secciones=[
                {
                    "titulo": "Datos del Programa",
                    "campos": [
                        {
                            "nombre": "nombre_programa",
                            "etiqueta": "Nombre del Programa:",
                            "tipo": "entry"
                        },
                        {
                            "nombre": "descripcion",
                            "etiqueta": "Descripción del programa:",
                            "tipo": "entry"
                        }
                    ]
                }
            ]
        )

        form.agregar_btn_guardar("Guardar Programa", self.crear_programa)
        form.agregar_separador()

        # Tabla
        self.tabla_programas = TableBuilder(tab)
        self.tabla_programas.crear_tabla(
            columnas=["Programa", "Descripción"]
        )

        # Cargar datos
        self.cargar_programas()

    # -------- MÉTODOS --------
    def crear_estudiante(self):
        # Obtener datos del formulario
        valores = {
            name: widget.get()
            for name, widget in self.estudiante_fields.items()
        }

        _resultado, error = EstudianteController.crear_estudiante_usuario(valores)

        if error:
            UIHelpers.mostrar_mensaje_error("Error", error)
            return

        UIHelpers.mostrar_mensaje_info("OK", "Estudiante creado exitosamente")

        self.cargar_estudiantes()

        FormBuilder.limpiar_formulario(self.estudiante_fields)

    def cargar_estudiantes(self):
        estudiantes = EstudianteController.listar_estudiantes()

        self.tabla_estudiantes.cargar_datos(estudiantes)

    def cargar_programas(self):
        programas = ProgramaController.listar_programas()

        self.tabla_programas.cargar_datos(programas)

    def crear_programa(self):
        # Obtener datos del formulario
        valores = {
            name: widget.get()
            for name, widget in self.programa_fields.items()
        }

        _resultado, error = ProgramaController.crear_programa(valores)

        if error:
            UIHelpers.mostrar_mensaje_error("Error", error)
            return

        UIHelpers.mostrar_mensaje_info("OK", "Programa creado exitosamente")

        self.cargar_programas()

        FormBuilder.limpiar_formulario(self.programa_fields)

    def cerrar_sesion(self):
        self.root.destroy()

        from ui.views.login_view import LoginView

        ventana = tk.Tk()
        LoginView(ventana)
        ventana.mainloop()
