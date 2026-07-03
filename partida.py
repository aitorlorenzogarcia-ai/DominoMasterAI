class Partida:

    def __init__(self):

        self.modo = "Draw"

        self.numero_jugadores = 4

        self.jugador_local = 1

        self.jugador_inicial = 1

        self.turno_actual = 1

        self.fichas_mano = []

        self.historial = []

        self.extremo_izquierdo = None

        self.extremo_derecho = None

    def añadir_ficha(self, ficha):
        self.fichas_mano.append(ficha)