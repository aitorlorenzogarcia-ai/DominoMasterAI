class Tablero:

    def __init__(self):

        self.izquierda = None

        self.derecha = None

        self.jugadas = []

    def esta_vacio(self):
        return self.izquierda is None and self.derecha is None

    def colocar_primera_ficha(self, ficha):

        self.izquierda = ficha.izquierda
        self.derecha = ficha.derecha

        self.jugadas.append(ficha)