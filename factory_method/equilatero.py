from triangulo import Triangulo

class Equilatero(Triangulo):
    
    def getDescripcion(self):
        print("Soy equilatero")

    def getSuperficie(self):
        return 0
    
    def dibujate(self):
        print("Dibujado")