from abc import ABC, abstractmethod

class LibroMalEstado(ABC):

    @abstractmethod
    def update(self):
        pass