class Motor:

    def __init__(self, partida):

        self.partida = partida

    def jugadas_posibles(self, jugador):

        posibles = []

        tablero = self.partida.tablero

        if tablero.esta_vacio():

            return jugador.mano.copy()

        izquierda = tablero.izquierda().izquierda

        derecha = tablero.derecha().derecha

        for ficha in jugador.mano:

            if (
                ficha.izquierda == izquierda
                or ficha.derecha == izquierda
                or ficha.izquierda == derecha
                or ficha.derecha == derecha
            ):

                posibles.append(ficha)

        return posibles