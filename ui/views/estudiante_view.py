import tkinter as tk

from models.estudiante import Estudiante

class EstudianteView:
    def __init__(self, root, usuario_id):
        self.root = root
        self.root.title("Panel Estudiante")

        tk.Label(root, text="Panel del Estudiante", font=("Arial", 14)).pack(pady=10)

        est = Estudiante.listar_por_id(usuario_id)

        tk.Label(root, text=f"ID: {est[0]}").pack()
        tk.Label(root, text=f"Nombre: {est[1]}").pack()
        tk.Label(root, text=f"Edad: {est[2]}").pack()

        tk.Label(root, text="Bienvenido al sistema 😊").pack(pady=20)