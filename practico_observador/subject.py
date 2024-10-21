from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self, observador):
        pass

    @abstractmethod
    def dettach(self, observador):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass