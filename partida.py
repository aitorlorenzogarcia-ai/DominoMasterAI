from jugador import Jugador
from tablero import Tablero


class Partida:

    def __init__(self):

        self.jugadores = []

        self.turno = 0

        self.empieza = 0

        self.tablero = Tablero()

    def agregar_jugador(self, nombre):

        jugador = Jugador(nombre)

        self.jugadores.append(jugador)

        return jugador

    def jugador_actual(self):

        return self.jugadores[self.turno]

    def siguiente_turno(self):

        self.turno += 1

        if self.turno >= len(self.jugadores):

            self.turno = 0

    def total_jugadores(self):

        return len(self.jugadores)