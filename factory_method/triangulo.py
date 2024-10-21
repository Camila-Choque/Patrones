from abc import ABC, abstractmethod

class Triangulo(ABC):
    def __init__(self):
        self.ladoA = 0
        self.ladoB = 0
        self.ladoC = 0

    @abstractmethod
    def getDescripcion(self):
        pass

    @abstractmethod
    def getSuperficie(self):
        pass

    @abstractmethod
    def dibujate(self):
        pass