"""
    Funciones auxiliares para la interfaz de usuario
"""

import tkinter as tk
from tkinter import messagebox

from ui.components import AppStyles


class UIHelpers:
    @staticmethod
    def mostrar_mensaje_info(titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    @staticmethod
    def mostrar_mensaje_error(titulo, mensaje):
        messagebox.showerror(titulo, mensaje)

    @staticmethod
    def crear_boton_hover(contenedor_padre, texto, metodo, tipo_boton="primary"):
        boton = tk.Button(
            contenedor_padre,
            text=texto,
            command=metodo,
            **AppStyles.estilos_button(tipo_boton)
        )

        if boton == "danger":
            hover_color = AppStyles.ERROR_HOVER
            normal_color = AppStyles.ERROR_COLOR
        else:
            hover_color = AppStyles.PRIMARY_HOVER
            normal_color = AppStyles.PRIMARY_COLOR

        boton.bind("<Enter>", lambda e: boton.config(bg=hover_color))
        boton.bind("<Leave>", lambda e: boton.config(bg=normal_color))

        return boton

    @staticmethod
    def crear_separador(contenedor_padre):
        separador = tk.Frame(contenedor_padre, bg=AppStyles.BORDER_COLOR, height=2)
        separador.pack(fill="x", padx=15, pady=(0, 15))

        return separador

    @staticmethod
    def evento_enter(elemento_interfaz, metodo):
        elemento_interfaz.bind("<Enter>", lambda e: metodo())

    @staticmethod
    def cerrar_sesion(root):
        root.destroy()

        from ui.views.login_view import LoginView

        ventana = tk.Tk()
        LoginView(ventana)
        ventana.mainloop()

