import tkinter as tk

from ui.components.styles import AppStyles


class HeaderBuilder:
    @staticmethod
    def crear_encabezado(contenedor_padre, usuario, metodo):
        encabezado_frame = tk.Frame(contenedor_padre, bg=AppStyles.HEADER_BG, height=100)
        encabezado_frame.pack(fill="x", side="top")
        encabezado_frame.pack_propagate(False)

        # Contenedor interno del header
        encabezado_contenedor = tk.Frame(encabezado_frame, bg=AppStyles.HEADER_BG)
        encabezado_contenedor.pack(fill="both", expand=True, padx=30, pady=15)

        # Título y usuario
        titulo_frame = tk.Frame(encabezado_contenedor, bg=AppStyles.HEADER_BG)
        titulo_frame.pack(side="left")

        tk.Label(
            titulo_frame,
            text="Panel de Administración",
            **AppStyles.estilos_label("encabezado")
        ).pack(anchor="w")

        tk.Label(
            titulo_frame,
            text=f"👤 {usuario['correo']}",
            **AppStyles.estilos_label("subtitulo_encabezado")
        ).pack(anchor="w", pady=(5, 0))

        # Botón de cerrar sesión
        btn_cerrar_sesion = tk.Button(
            encabezado_contenedor,
            text="Cerrar Sesión",
            command=metodo,
            **AppStyles.estilos_button("danger")
        )
        btn_cerrar_sesion.pack(side="right")

        # Efectos hover
        btn_cerrar_sesion.bind("<Enter>",
                               lambda e: btn_cerrar_sesion.config(bg=AppStyles.ERROR_HOVER))
        btn_cerrar_sesion.bind("<Leave>",
                               lambda e: btn_cerrar_sesion.config(bg=AppStyles.ERROR_COLOR))

        return encabezado_frame
