import tkinter as tk

from fichas import Ficha
from ui.componentes import FichaWidget


class SeleccionMano(tk.Frame):

    def __init__(self, master, volver):

        super().__init__(master, bg="#1E1E1E")

        self.pack(fill="both", expand=True)

        self.volver = volver

        self.fichas = []

        titulo = tk.Label(
            self,
            text="Selecciona tu mano",
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 24, "bold")
        )

        titulo.pack(pady=20)

        self.estado = tk.Label(
            self,
            text="0 / 7 fichas",
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 12)
        )

        self.estado.pack()

        self.frame_mano = tk.Frame(
            self,
            bg="#1E1E1E"
        )

        self.frame_mano.pack(pady=25)

        self.frame_selector = tk.Frame(
            self,
            bg="#1E1E1E"
        )

        self.frame_selector.pack()

        self.widgets_selector = {}

        fila = 0

        for izquierda in range(7):

            columna = 0

            for derecha in range(izquierda, 7):

                ficha = Ficha(derecha, izquierda)

                widget = FichaWidget(
                    self.frame_selector,
                    ficha,
                    self.elegir
                )

                widget.grid(
                    row=fila,
                    column=columna,
                    padx=4,
                    pady=4
                )

                self.widgets_selector[ficha] = widget

                columna += 1

            fila += 1

        self.boton_comenzar = tk.Button(
            self,
            text="Comenzar partida",
            width=20,
            state="disabled",
            command=self.comenzar_partida
        )

        self.boton_comenzar.pack(pady=10)

        self.boton_volver = tk.Button(
            self,
            text="Volver",
            width=20,
            command=self.volver
        )

        self.boton_volver.pack()

    def elegir(self, ficha):

        if ficha in self.fichas:
            return

        if len(self.fichas) >= 7:
            return

        self.fichas.append(ficha)

        self.widgets_selector[ficha].grid_remove()

        self.actualizar()

    def quitar(self, ficha):

        self.fichas.remove(ficha)

        self.widgets_selector[ficha].grid()

        self.actualizar()

    def actualizar(self):

        for widget in self.frame_mano.winfo_children():
            widget.destroy()

        self.fichas.sort(
            key=lambda f: (f.izquierda, f.derecha),
            reverse=True
        )

        for ficha in self.fichas:

            widget = FichaWidget(
                self.frame_mano,
                ficha,
                self.quitar
            )

            widget.pack(
                side="left",
                padx=5
            )

        self.estado.config(
            text=f"{len(self.fichas)} / 7 fichas"
        )

        if len(self.fichas) == 7:
            self.boton_comenzar.config(state="normal")
        else:
            self.boton_comenzar.config(state="disabled")

    def comenzar_partida(self):

        print("Aquí comenzará la partida.")