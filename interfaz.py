import tkinter as tk

from ui.menu import MenuPrincipal
from ui.seleccion_mano import SeleccionMano


class Interfaz:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title("Domino Master AI")

        self.ventana.geometry("1000x700")

        self.ventana.configure(bg="#1E1E1E")

        self.pantalla_actual = None

        self.menu()

        self.ventana.mainloop()

    def limpiar(self):

        if self.pantalla_actual:
            self.pantalla_actual.destroy()

    def menu(self):

        self.limpiar()

        self.pantalla_actual = MenuPrincipal(
            self.ventana,
            self.nueva_partida
        )

    def nueva_partida(self):

        self.limpiar()

        self.pantalla_actual = SeleccionMano(
            self.ventana,
            self.menu
        )


def iniciar():

    Interfaz()