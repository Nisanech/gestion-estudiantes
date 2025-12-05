"""
    Clase para construir los formularios
"""

import tkinter as tk
from tkinter import ttk

from ui.components.styles import AppStyles


class FormBuilder:
    def __init__(self, contenedor_padre):
        self.contenedor_padre = contenedor_padre
        self.campos = {}
        self.formulario_frame = None

    def crear_formulario(self, titulo, secciones):
        self.formulario_frame = tk.Frame(self.contenedor_padre, bg=AppStyles.CARD_BG)
        self.formulario_frame.pack(fill="x", padx=15, pady=15)

        # Titulo
        tk.Label(
            self.formulario_frame,
            text=titulo,
            **AppStyles.estilos_label("titulo")
        ).pack(anchor="w", pady=(0, 15))

        # Crear secciones
        for seccion in secciones:
            self._crear_seccion(seccion)

        return self.campos

    def _crear_seccion(self, seccion):
        seccion_frame = tk.Frame(self.formulario_frame, bg=AppStyles.CARD_BG)
        seccion_frame.pack(fill="x", pady=(0, 15))

        # Título de la seccion
        tk.Label(
            seccion_frame,
            text=seccion["titulo"],
            **AppStyles.estilos_label("seccion")
        ).pack(anchor="w", pady=(0, 15))

        # Contenedor para los campos
        campos_contenedor = tk.Frame(seccion_frame, bg=AppStyles.CARD_BG)
        campos_contenedor.pack(fill="x")

        # Crear campos
        for campo in seccion["campos"]:
            self._crear_campo(campos_contenedor, campo)

    def _crear_campo(self, contenedor_padre, configuracion_campo):
        """
            Crea un campo individual del formulario
            Argumentos:
                contenedor_padre: Contenedor padre para el campo
                configuracion_campo: Configuración del campo con estructura:
                    {
                        "nombre": "correo",
                        "etiqueta": "Correo Electrónico:",
                        "tipo": "entry",  # entry, password, readonly, combobox
                        "default": "",
                        "opciones": [],  # Para combobox
                    }
        """
        nombre_campo = configuracion_campo["nombre"]
        tipo_campo = configuracion_campo.get("tipo", "entry")

        # Contenedor del campo
        campo_frame = tk.Frame(contenedor_padre, bg=AppStyles.CARD_BG)
        campo_frame.pack(side="left", padx=(0, 15), expand=True, fill="x")

        # Label
        tk.Label(
            campo_frame,
            text=configuracion_campo["etiqueta"],
            **AppStyles.estilos_label("normal")
        ).pack(anchor="w")

        # Widget de entrada según el tipo
        if tipo_campo == "combobox":
            widget = ttk.Combobox(
                campo_frame,
                values=configuracion_campo.get("opciones", []),
                font=(AppStyles.FONT_FAMILY, 10),
                state="readonly",
                style="Custom.TCombobox"
            )
            widget.pack(fill="x", ipady=5)
            if "default" in configuracion_campo:
                widget.set(configuracion_campo["default"])

        elif tipo_campo == "readonly":
            widget = tk.Entry(
                campo_frame,
                font=(AppStyles.FONT_FAMILY, 10),
                bg="#F1F5F9",
                fg=AppStyles.TEXT_LIGHT,
                relief="solid",
                borderwidth=1,
                highlightthickness=1,
                highlightbackground=AppStyles.BORDER_COLOR,
                state="readonly"
            )
            widget.pack(fill="x", ipady=5)
            if "default" in configuracion_campo:
                widget.config(state="normal")
                widget.insert(0, configuracion_campo["default"])
                widget.config(state="readonly")

        elif tipo_campo == "password":
            widget = tk.Entry(
                campo_frame,
                **AppStyles.estilos_entry(),
                show="*"
            )
            widget.pack(fill="x", ipady=5)

        else:  # entry por defecto
            widget = tk.Entry(
                campo_frame,
                **AppStyles.estilos_entry()
            )
            widget.pack(fill="x", ipady=5)
            if "default" in configuracion_campo:
                widget.insert(0, configuracion_campo["default"])

        self.campos[nombre_campo] = widget

    def agregar_btn_guardar(self, texto, metodo):
        btn_frame = tk.Frame(self.formulario_frame, bg=AppStyles.CARD_BG)
        btn_frame.pack(fill="x", pady=(10, 0))

        btn_submit = tk.Button(
            btn_frame,
            text=texto,
            command=metodo,
            **AppStyles.estilos_button("primary")
        )
        btn_submit.pack(side="left")

        # Efectos hover
        btn_submit.bind("<Enter>",
                        lambda e: btn_submit.config(bg=AppStyles.PRIMARY_HOVER))
        btn_submit.bind("<Leave>",
                        lambda e: btn_submit.config(bg=AppStyles.PRIMARY_COLOR))

        return btn_submit

    def agregar_separador(self):
        separator = tk.Frame(self.contenedor_padre, bg=AppStyles.BORDER_COLOR, height=2)
        separator.pack(fill="x", padx=15, pady=(0, 15))

    def obtener_valores(self):
        valores = {}

        for campo, widget in self.campos.items():
            if isinstance(widget, ttk.Combobox):
                valores[campo] = widget.get()
            else:
                valores[campo] = widget.get()

        return valores

    @staticmethod
    def limpiar_formulario(campos):
        for widget in campos.values():
            if isinstance(widget, ttk.Combobox):
                widget.set("")
            elif widget.cget("state") != "readonly":
                widget.delete(0, tk.END)