"""
    Clase para construir las tablas (TreeView)
"""

import tkinter as tk
from tkinter import ttk

from ui.components.styles import AppStyles


class TableBuilder:
    def __init__(self, contenedor_padre):
        self.contenedor_padre = contenedor_padre
        self.tree = None
        self.scrollbar = None

    def crear_tabla(self, columnas, ancho_columna=None):
        tabla_frame = tk.Frame(self.contenedor_padre, bg=AppStyles.BORDER_COLOR, padx=1, pady=1)
        tabla_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # Crear TreeView
        nombre_columnas = columnas

        self.tree = ttk.Treeview(
            tabla_frame,
            columns=nombre_columnas,
            show="headings",
            style="Custom.Treeview"
        )

        # Configurar columnas
        for col in nombre_columnas:
            self.tree.heading(col, text=col)

            if ancho_columna and col in ancho_columna:
                width = ancho_columna[col]
            else:
                width = 150

            self.tree.column(col, width=width, anchor="center")

        # Scrollbar para TreeView
        self.scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

        self.tree.pack(fill="both", expand=True)

        # Colores alternados en filas
        self.tree.tag_configure('oddrow', background="#F1F5F9")
        self.tree.tag_configure('evenrow', background=AppStyles.CARD_BG)

        return self.tree

    def cargar_datos(self, datos, limpiar=True):
        if limpiar:
            self.limpiar()

        for idx, fila in enumerate(datos):
            tag = 'evenrow' if idx % 2 == 0 else 'oddrow'

            # Insertar fila
            valores = fila

            self.tree.insert("", "end", values=valores, tags=(tag,))

    def limpiar(self):
        if self.tree:
            for item in self.tree.get_children():
                self.tree.delete(item)
