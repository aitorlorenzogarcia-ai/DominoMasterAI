class Jugador:

    def __init__(self, numero):

        self.numero = numero

        self.fichas = 7

        self.ha_pasado = False

        self.robos = 0

        self.jugadas = []

    def jugar(self, ficha):
        self.jugadas.append(ficha)
        self.fichas -= 1

    def robar(self):
        self.fichas += 1
        self.robos += 1