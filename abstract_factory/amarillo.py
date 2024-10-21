from color import Color
class Amarillo(Color):
    def __init__(self):
        self.esPrimario = None

    def colorea(self, tv):
        tv.color = "amarillo"
        print("Coloreado a amarillo")