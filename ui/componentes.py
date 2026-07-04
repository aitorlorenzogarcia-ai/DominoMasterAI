import tkinter as tk


class FichaWidget(tk.Canvas):

    def __init__(self, master, ficha, comando=None):

        super().__init__(
            master,
            width=60,
            height=100,
            bg="#1E1E1E",
            highlightthickness=0
        )

        self.ficha = ficha
        self.comando = comando

        self.dibujar()

        self.bind("<Button-1>", self.click)

    def dibujar(self):

        self.create_rectangle(
            5,
            5,
            55,
            95,
            fill="white",
            outline="black",
            width=2
        )

        self.create_line(
            5,
            50,
            55,
            50,
            width=2
        )

        self.create_text(
            30,
            25,
            text=str(self.ficha.izquierda),
            font=("Segoe UI", 18, "bold")
        )

        self.create_text(
            30,
            75,
            text=str(self.ficha.derecha),
            font=("Segoe UI", 18, "bold")
        )

    def click(self, event):

        if self.comando:
            self.comando(self.ficha)