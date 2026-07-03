import tkinter as tk


class ConfigJugadores(tk.Frame):

    def __init__(self, master, volver, siguiente):

        super().__init__(master, bg="#1E1E1E")

        self.pack(fill="both", expand=True)

        titulo = tk.Label(
            self,
            text="Paso 2 de 4\n\nNúmero de jugadores",
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 24, "bold")
        )

        titulo.pack(pady=30)

        self.numero = tk.IntVar(value=4)

        for cantidad in (2, 3, 4):

            rb = tk.Radiobutton(
                self,
                text=f"{cantidad} jugadores",
                variable=self.numero,
                value=cantidad,
                bg="#1E1E1E",
                fg="white",
                selectcolor="#2E2E2E",
                font=("Segoe UI", 13)
            )

            rb.pack(pady=5)

        tk.Button(
            self,
            text="Siguiente",
            width=20,
            command=lambda: siguiente(self.numero.get())
        ).pack(pady=20)

        tk.Button(
            self,
            text="Volver",
            width=20,
            command=volver
        ).pack()