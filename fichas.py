class Ficha:

    def __init__(self, izquierda, derecha):

        self.izquierda = izquierda
        self.derecha = derecha

    def es_doble(self):

        return self.izquierda == self.derecha

    def valor(self):

        return self.izquierda + self.derecha

    def girar(self):

        self.izquierda, self.derecha = (
            self.derecha,
            self.izquierda
        )

    def __str__(self):

        return f"[{self.izquierda}|{self.derecha}]"

    def __repr__(self):

        return str(self)

    def __eq__(self, other):

        if not isinstance(other, Ficha):
            return False

        return (
            self.izquierda == other.izquierda
            and
            self.derecha == other.derecha
        )

    def __hash__(self):

        return hash((self.izquierda, self.derecha))