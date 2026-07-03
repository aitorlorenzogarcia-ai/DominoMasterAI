import tkinter as tk


class ConfigEmpieza(tk.Frame):

    def __init__(self, master, volver, siguiente, numero_jugadores):

        super().__init__(master, bg="#1E1E1E")

        self.pack(fill="both", expand=True)

        titulo = tk.Label(
            self,
            text="Paso 4 de 4\n\n¿Quién empieza?",
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 24, "bold")
        )

        titulo.pack(pady=30)

        self.empieza = tk.IntVar(value=1)

        for i in range(1, numero_jugadores + 1):

            rb = tk.Radiobutton(
                self,
                text=f"Jugador {i}",
                variable=self.empieza,
                value=i,
                bg="#1E1E1E",
                fg="white",
                selectcolor="#2E2E2E",
                font=("Segoe UI", 13)
            )

            rb.pack(pady=5)

        tk.Button(
            self,
            text="Crear partida",
            width=20,
            command=lambda: siguiente(self.empieza.get())
        ).pack(pady=20)

        tk.Button(
            self,
            text="Volver",
            width=20,
            command=volver
        ).pack()