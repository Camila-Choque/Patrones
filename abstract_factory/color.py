from abc import ABC, abstractmethod

class Color(ABC):
    def __init__(self):
        self.descripcion = ""

    @abstractmethod
    def colorea(tv):
        pass
    
    