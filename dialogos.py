import tkinter as tk
from fichas import Ficha


class SelectorFichas(tk.Toplevel):

    def __init__(self, master, callback):

        super().__init__(master)

        self.callback = callback

        self.title("Selecciona una ficha")

        self.geometry("520x420")

        self.resizable(False, False)

        self.crear_botones()

    def crear_botones(self):

        fila = 0

        for izquierda in range(7):

            columna = 0

            for derecha in range(izquierda, 7):

                ficha = Ficha(derecha, izquierda)

                boton = tk.Button(
                    self,
                    text=str(ficha),
                    width=8,
                    height=2,
                    command=lambda f=ficha: self.seleccionar(f)
                )

                boton.grid(
                    row=fila,
                    column=columna,
                    padx=5,
                    pady=5
                )

                columna += 1

            fila += 1

    def seleccionar(self, ficha):

        self.callback(ficha)

        self.destroy()