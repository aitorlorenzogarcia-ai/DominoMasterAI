class Tablero:

    def __init__(self):

        self.fichas = []

    def colocar_izquierda(self, ficha):

        self.fichas.insert(0, ficha)

    def colocar_derecha(self, ficha):

        self.fichas.append(ficha)

    def izquierda(self):

        if not self.fichas:
            return None

        return self.fichas[0]

    def derecha(self):

        if not self.fichas:
            return None

        return self.fichas[-1]

    def esta_vacio(self):

        return len(self.fichas) == 0