from triangulo import Triangulo

class Isosceles(Triangulo):
    
    def getDescripcion(self):
        print("Soy isosceles")

    def getSuperficie(self):
        return 0
    
    def dibujate(self):
        print("Dibujado")