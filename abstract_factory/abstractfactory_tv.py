from abc import ABC, abstractmethod

class TvAbstractFactory(ABC):

    @abstractmethod
    def createTv(self):
        pass
    @abstractmethod
    def createColor(self):
        pass