from color import Color
class Azul(Color):
    def __init__(self):
        self.esPrimario = None

    def colorea(self, tv):
        tv.color = "azul"
        print("Coloreado a azul")