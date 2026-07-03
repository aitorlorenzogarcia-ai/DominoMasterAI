class Jugador:

    def __init__(self, nombre):

        self.nombre = nombre

        self.mano = []

    def añadir_ficha(self, ficha):

        self.mano.append(ficha)

    def quitar_ficha(self, ficha):

        self.mano.remove(ficha)

    def tiene_ficha(self, ficha):

        return ficha in self.mano

    def total_fichas(self):

        return len(self.mano)