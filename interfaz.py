import tkinter as tk

from ui.menu import MenuPrincipal
from ui.seleccion_mano import SeleccionMano
from ui.config_jugadores import ConfigJugadores
from ui.config_jugador import ConfigJugador
from ui.config_empieza import ConfigEmpieza


class Interfaz:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title("Domino Master AI")

        self.ventana.geometry("1000x700")

        self.ventana.configure(bg="#1E1E1E")

        self.pantalla_actual = None

        self.fichas = []
        self.numero_jugadores = 4
        self.mi_jugador = 1
        self.empieza = 1

        self.menu()

        self.ventana.mainloop()

    def limpiar(self):

        if self.pantalla_actual:
            self.pantalla_actual.destroy()

    def menu(self):

        self.limpiar()

        self.pantalla_actual = MenuPrincipal(
            self.ventana,
            self.seleccion_mano
        )

    def seleccion_mano(self):

        self.limpiar()

        self.pantalla_actual = SeleccionMano(
            self.ventana,
            self.menu
        )

        # sustituiremos esto en el siguiente paso
        self.pantalla_actual.comenzar_partida = self.ir_config_jugadores

    def ir_config_jugadores(self):

        self.fichas = self.pantalla_actual.fichas.copy()

        self.limpiar()

        self.pantalla_actual = ConfigJugadores(
            self.ventana,
            self.seleccion_mano,
            self.ir_config_jugador
        )

    def ir_config_jugador(self, numero):

        self.numero_jugadores = numero

        self.limpiar()

        self.pantalla_actual = ConfigJugador(
            self.ventana,
            self.ir_config_jugadores,
            self.ir_config_empieza,
            numero
        )

    def ir_config_empieza(self, jugador):

        self.mi_jugador = jugador

        self.limpiar()

        self.pantalla_actual = ConfigEmpieza(
            self.ventana,
            self.ir_config_jugador,
            self.crear_partida,
            self.numero_jugadores
        )

    def crear_partida(self, empieza):

        self.empieza = empieza

        print("===========")
        print("PARTIDA")
        print("===========")
        print("Fichas:", self.fichas)
        print("Jugadores:", self.numero_jugadores)
        print("Yo soy:", self.mi_jugador)
        print("Empieza:", self.empieza)

        # Aquí construiremos la Partida real
        # y abriremos la mesa.

def iniciar():

    Interfaz()