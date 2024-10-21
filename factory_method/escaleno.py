from triangulo import Triangulo

class Escaleno(Triangulo):
    
    def getDescripcion(self):
        print("Soy escaleno")

    def getSuperficie(self):
        return 0
    
    def dibujate(self):
        print("Dibujado")