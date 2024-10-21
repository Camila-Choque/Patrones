from abc import ABC, abstractmethod

class TV(ABC):
    def __init__(self):  
        self.marca = ""
        self.pulgadas = 0
        self.color = ""
        self.descripcion = ""
        self.precio = 0

    