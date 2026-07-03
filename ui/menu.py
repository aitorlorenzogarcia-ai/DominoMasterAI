import tkinter as tk


class MenuPrincipal(tk.Frame):

    def __init__(self, master, nueva_partida):

        super().__init__(master, bg="#1E1E1E")

        self.pack(fill="both", expand=True)

        titulo = tk.Label(
            self,
            text="DOMINO MASTER AI",
            bg="#1E1E1E",
            fg="white",
            font=("Segoe UI", 28, "bold")
        )

        titulo.pack(pady=(40, 20))

        version = tk.Label(
            self,
            text="Versión 0.5",
            bg="#1E1E1E",
            fg="lightgray",
            font=("Segoe UI", 12)
        )

        version.pack(pady=(0, 30))

        boton_nueva = tk.Button(
            self,
            text="Nueva partida",
            width=20,
            height=2,
            command=nueva_partida
        )

        boton_nueva.pack(pady=10)

        boton_salir = tk.Button(
            self,
            text="Salir",
            width=20,
            height=2,
            command=master.destroy
        )

        boton_salir.pack(pady=10)