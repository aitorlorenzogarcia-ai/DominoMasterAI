import tkinter as tk

from fichas import Ficha


class SeleccionMano(tk.Frame):

    def __init__(self, master, volver):

        super().__init__(master, bg="#1E1E1E")

        self.pack(fill="both", expand=True)

        self.volver = volver

        self.fichas = []

        titulo = tk.Label(
            self,
            text="Selecciona tu mano inicial",
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 24, "bold")
        )

        titulo.pack(pady=20)

        self.estado = tk.Label(
            self,
            text="0 / 7 fichas\n\nTe quedan 7 por elegir.",
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

        self.botones = {}

        for izquierda in range(7):

            for derecha in range(izquierda, 7):

                ficha = Ficha(derecha, izquierda)

                boton = tk.Button(
                    self.frame_selector,
                    text=str(ficha),
                    width=8,
                    command=lambda f=ficha: self.elegir(f)
                )

                boton.grid(
                    row=izquierda,
                    column=derecha - izquierda,
                    padx=3,
                    pady=3
                )

                self.botones[ficha] = boton

        self.boton_comenzar = tk.Button(
            self,
            text="Comenzar partida",
            width=22,
            height=2,
            font=("Segoe UI", 11, "bold"),
            state="disabled",
            command=self.comenzar_partida
        )

        self.boton_comenzar.pack(pady=10)

        self.boton_volver = tk.Button(
            self,
            text="Volver",
            width=22,
            command=self.volver
        )

        self.boton_volver.pack()

    def elegir(self, ficha):

        if len(self.fichas) >= 7:
            return

        if ficha in self.fichas:
            return

        self.fichas.append(ficha)

        self.botones[ficha].config(state="disabled")

        self.actualizar()

    def quitar(self, ficha):

        self.fichas.remove(ficha)

        self.botones[ficha].config(state="normal")

        self.actualizar()

    def actualizar(self):

        for widget in self.frame_mano.winfo_children():
            widget.destroy()

        self.fichas.sort(
            key=lambda ficha: (
                ficha.izquierda,
                ficha.derecha
            ),
            reverse=True
        )

        for ficha in self.fichas:

            boton = tk.Button(
                self.frame_mano,
                text=str(ficha),
                command=lambda f=ficha: self.quitar(f)
            )

            boton.pack(side="left", padx=4)

        quedan = 7 - len(self.fichas)

        if quedan == 0:

            texto = "7 / 7 fichas\n\n¡Mano completa!"

        elif quedan == 1:

            texto = "6 / 7 fichas\n\nSolo falta una ficha."

        else:

            texto = f"{len(self.fichas)} / 7 fichas\n\nTe quedan {quedan} por elegir."

        self.estado.config(text=texto)

        if len(self.fichas) == 7:
            self.boton_comenzar.config(state="normal")
        else:
            self.boton_comenzar.config(state="disabled")

    def comenzar_partida(self):

        print("Aquí comenzará la partida.")