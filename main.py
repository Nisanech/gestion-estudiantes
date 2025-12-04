"""
    Punto de entrada de la aplicación. Inicializa la ventana principal de Tkinter y ejecuta la interfaz gráfica del sistema de gestión de estudiantes.
"""

import tkinter as tk
from views.interfaz import InterfazApp
from views.login_view import LoginView

"""
    Asegura que el código solo se ejecute cuando el archivo es ejecutado directamente, no cuando es importado como módulo.
"""
if __name__ == "__main__":
    root = tk.Tk() # Crea la ventana raíz (principal) de la aplicación Tkinter.

    app = LoginView(root) # Instancia la clase InterfazApp pasándole la ventana raíz como parámetro.

    root.mainloop() # Inicia el bucle principal de eventos de Tkinter.