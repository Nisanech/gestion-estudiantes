"""
    Gestiona los estilos para toda la aplicación
"""

from tkinter import ttk


class AppStyles:
    # Paleta de Colores
    BG_COLOR = "#F8FAFC"
    HEADER_BG = "#1E293B"
    PRIMARY_COLOR = "#2563EB"
    PRIMARY_HOVER = "#1D4ED8"
    TEXT_COLOR = "#1E293B"
    TEXT_LIGHT = "#64748B"
    CARD_BG = "#FFFFFF"
    BORDER_COLOR = "#E2E8F0"
    ERROR_COLOR = "#EF4444"
    ERROR_HOVER = "#DC2626"

    # Tipo de fuente
    FONT_FAMILY = "Segoe UI"

    @classmethod
    def estilos_notebook(cls):
        # Configurar estilos para el Notebook y TreeView
        estilo = ttk.Style()
        estilo.theme_use('clam')

        # Estilo para las pestañas
        estilo.configure(
            "Custom.TNotebook",
            background=cls.BG_COLOR,
            borderwidth=0
        )
        estilo.configure(
            "Custom.TNotebook.Tab",
            background=cls.CARD_BG,
            foreground=cls.TEXT_COLOR,
            padding=[20, 10],
            font=(cls.FONT_FAMILY, 11, "bold"),
            borderwidth=1,
            relief="solid"
        )
        estilo.map(
            "Custom.TNotebook.Tab",
            background=[("selected", cls.PRIMARY_COLOR)],
            foreground=[("selected", "white")],
            expand=[("selected", [1, 1, 1, 0])]
        )

        # Estilo para Treeview
        estilo.configure(
            "Custom.Treeview",
            background=cls.CARD_BG,
            foreground=cls.TEXT_COLOR,
            fieldbackground=cls.CARD_BG,
            borderwidth=0,
            font=(cls.FONT_FAMILY, 10),
            rowheight=30
        )
        estilo.configure(
            "Custom.Treeview.Heading",
            background=cls.PRIMARY_COLOR,
            foreground="white",
            font=(cls.FONT_FAMILY, 11, "bold"),
            borderwidth=0,
            relief="flat"
        )
        estilo.map(
            "Custom.Treeview",
            background=[("selected", cls.PRIMARY_COLOR)],
            foreground=[("selected", "white")]
        )

        # Estilo para Combobox
        estilo.configure(
            "Custom.TCombobox",
            fieldbackground=cls.CARD_BG,
            background=cls.CARD_BG,
            foreground=cls.TEXT_COLOR,
            borderwidth=1,
            relief="solid"
        )

    @classmethod
    def estilos_entry(cls):
        """
            Retorna los estilos para los campos de entrada
        """
        return {
            "font": (cls.FONT_FAMILY, 10),
            "bg": cls.CARD_BG,
            "fg": cls.TEXT_COLOR,
            "relief": "solid",
            "borderwidth": 1,
            "highlightthickness": 1,
            "highlightbackground": cls.BORDER_COLOR,
            "highlightcolor": cls.PRIMARY_COLOR
        }

    @classmethod
    def estilos_button(cls, tipo_boton="primary"):
        """
            Retorna los estilos para los botones
        """
        configuracion = {
            "primary": {
                "font": (cls.FONT_FAMILY, 11, "bold"),
                "bg": cls.PRIMARY_COLOR,
                "fg": "white",
                "activebackground": cls.PRIMARY_HOVER,
                "activeforeground": "white",
                "relief": "flat",
                "cursor": "hand2",
                "padx": 30,
                "pady": 10
            },
            "danger": {
                "font": (cls.FONT_FAMILY, 11, "bold"),
                "bg": cls.ERROR_COLOR,
                "fg": "white",
                "activebackground": cls.ERROR_HOVER,
                "activeforeground": "white",
                "relief": "flat",
                "cursor": "hand2",
                "padx": 20,
                "pady": 8
            }
        }

        return configuracion.get(tipo_boton, configuracion["primary"])

    @classmethod
    def estilos_label(cls, tipo_etiqueta="normal"):
        """
            Retorna los estilos para las etiquetas
        """
        configuracion = {
            "normal": {
                "font": (cls.FONT_FAMILY, 10),
                "fg": cls.TEXT_COLOR,
                "bg": cls.CARD_BG
            },
            "titulo": {
                "font": (cls.FONT_FAMILY, 14, "bold"),
                "fg": cls.TEXT_COLOR,
                "bg": cls.CARD_BG
            },
            "seccion": {
                "font": (cls.FONT_FAMILY, 11, "bold"),
                "fg": cls.PRIMARY_COLOR,
                "bg": cls.CARD_BG
            },
            "encabezado": {
                "font": (cls.FONT_FAMILY, 18, "bold"),
                "fg": "white",
                "bg": cls.HEADER_BG
            },
            "subtitulo_encabezado": {
                "font": (cls.FONT_FAMILY, 10),
                "fg": "#94A3B8",
                "bg": cls.HEADER_BG
            }
        }

        return configuracion.get(tipo_etiqueta, configuracion["normal"])
