from triangulo_factory_method import TrianguloFactoryMethod
from equilatero import Equilatero
from escaleno import Escaleno
from isosceles import Isosceles

class TrianguloFactory(TrianguloFactoryMethod):
    
    def createTriangulo(self, ladoA, ladoB, ladoC):
        if (ladoA==ladoB) and (ladoA == ladoC):
            equilatero = Equilatero()
            equilatero.ladoA = ladoA
            equilatero.ladoB = ladoB
            equilatero.ladoC = ladoC
            return equilatero
        elif (ladoA != ladoB) and (ladoA != ladoC) and (ladoB != ladoC):
            escaleno = Escaleno()
            escaleno.ladoA = ladoA
            escaleno.ladoB = ladoB
            escaleno.ladoC = ladoC
            return escaleno
        else:
            isosceles = Isosceles()
            isosceles.ladoA = ladoA
            isosceles.ladoB = ladoB
            isosceles.ladoC = ladoC
            return isosceles